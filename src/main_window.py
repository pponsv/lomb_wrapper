from PySide6 import QtGui, QtCore, QtWidgets

from auxfiles.signal_names import SIGNAL_NAMES
from . import qt_workers
from . import utils
from . import class_signal_arrays
from .ui.ui_mainwindow import Ui_MainWindow
from .class_window_info import WindowInfo


DOUBLE_VALIDATOR = QtGui.QRegularExpressionValidator(
    QtCore.QRegularExpression("^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$")
)
INT_VALIDATOR = QtGui.QRegularExpressionValidator(
    QtCore.QRegularExpression("[1-9][0-9]*")
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #   Threading
        self.threadpool = QtCore.QThreadPool().globalInstance()
        self.threadpool.setMaxThreadCount(5)

        #   UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.populate_boxes()

        #   Window info
        self.info = WindowInfo(self.ui)

        #   DAQ dialog
        self.daq_dialog = QtWidgets.QDialog()
        self.show()

    def init_ui(self):
        #   Figure Widget
        self.ui.figLayout.setBackground("w")

        #   Validators
        self.ui.lowerTLim.setValidator(DOUBLE_VALIDATOR)
        self.ui.upperTLim.setValidator(DOUBLE_VALIDATOR)
        self.ui.filterFMax.setValidator(DOUBLE_VALIDATOR)
        self.ui.filterFMin.setValidator(DOUBLE_VALIDATOR)
        self.ui.shotNumberInput.setValidator(INT_VALIDATOR)
        self.ui.spgramNperseg.setValidator(INT_VALIDATOR)
        self.ui.spgramNoverlap.setValidator(INT_VALIDATOR)

        #   Connections
        self.ui.shotNumberInput.returnPressed.connect(self.loadData)
        self.ui.refreshButton.clicked.connect(self.refresh_plots)
        self.ui.lastShotButton.clicked.connect(self.get_last_shot)
        self.ui.loadDataButton.clicked.connect(self.loadData)
        self.ui.fftButton.clicked.connect(self.makeFfts)
        self.ui.integrateDataButton.clicked.connect(self.integrateData)
        self.ui.loadDmusicButton.clicked.connect(self.load_dmusic)
        self.ui.addRegionButton.clicked.connect(self.add_region)

        #   Menu bar
        self.ui.actionSave_figure.triggered.connect(self.savefig)

    def get_last_shot(self):
        def write_shot(info):
            self.ui.shotNumberInput.setText(str(info[0]))

        worker = qt_workers.Worker(utils.da.py_lastshot)
        worker.signaler.result.connect(write_shot)
        self.threadpool.start(worker, priority=0)

    def populate_boxes(self):
        self.ui.signalArraySelector.addItems(SIGNAL_NAMES)
        self.get_last_shot()

    def savefig(self):
        utils.save_figure(self.ui.figLayout.scene(), self.info)

    def make_array(self):
        self.info.refresh()
        name = self.info.array
        if hasattr(self, "array"):
            if self.info.shot == self.array.shot:
                if name == self.array.signal.name:
                    return
        self.array = class_signal_arrays.Signal_Spgram(
            shot=self.info.shot,
            name=name,
            fig=self.ui.figLayout,
            threadpool=self.threadpool,
            info=self.info,
        )

    def loadData(self):
        self.make_array()
        self.array.read_seq()
        self.refresh_plots()

    def integrateData(self):
        self.array.plot_integrated()

    def refresh_plots(self):
        self.info.refresh()
        self.array.make_spectrograms()
        self.array.plot_signals()

    def makeFfts(self):
        self.refresh_plots()
        for key in self.array.ax:
            self.array.ax[key].ctrl.fftCheck.setChecked(True)
            self.array.ax[key].ctrl.logXCheck.setChecked(True)
            self.array.ax[key].ctrl.logYCheck.setChecked(True)

    def load_dmusic(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Open File",
            dir=f"{QtCore.QDir.homePath()}/MEGA/00_doctorado/research/experiments/2022_spatial_periodicity_nbi_driven_ae/Analysis/DMUSIC/hdfs",
            filter="HDF5 files (*.h5, *.hdf5);;All Files (*.*)",
            selectedFilter="All Files (*.*)",
        )[0]
        self.make_array()
        self.array.from_dmusic(path)
        self.array.plot_signals()

    def add_region(self):
        bounds = [self.array.linked_rois.xlim, self.array.linked_rois.ylim]
        print(bounds)
