from PySide6 import QtGui, QtCore, QtWidgets

from auxfiles.signal_names import SIGNAL_NAMES
from . import paths
from . import qt_workers
from . import utils
from . import class_signal_arrays
from .ui.ui_mainwindow import Ui_MainWindow
from .class_window_info import WindowInfo
from .class_lomb import Lomb, ORIENTATION_TRANSLATION, BASE_TRANSLATION
from .class_polarization import Polarization

import TJII_mirnov_array as tma
import vmec_utils as vl


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

        #   Init paths
        paths.set_config_folder(paths.CONFIG_PATH)

    def init_ui(self):
        #   Figure Widget
        self.ui.figLayout.setBackground("w")
        self.populate_helical_orientation()

        #   Validators
        self.ui.lowerTLim.setValidator(DOUBLE_VALIDATOR)
        self.ui.upperTLim.setValidator(DOUBLE_VALIDATOR)
        self.ui.filterFMax.setValidator(DOUBLE_VALIDATOR)
        self.ui.filterFMin.setValidator(DOUBLE_VALIDATOR)
        self.ui.shotNumberInput.setValidator(INT_VALIDATOR)
        self.ui.spgramNperseg.setValidator(INT_VALIDATOR)
        self.ui.spgramNoverlap.setValidator(INT_VALIDATOR)

        #   Button Connections
        self.ui.refreshButton.clicked.connect(self.refresh_plots)
        self.ui.lastShotButton.clicked.connect(self.get_last_shot)
        self.ui.loadDataButton.clicked.connect(self.loadData)
        self.ui.fftButton.clicked.connect(self.makeFfts)
        self.ui.integrateDataButton.clicked.connect(self.integrateData)
        self.ui.addRegionButton.clicked.connect(self.add_region)
        self.ui.removeLastRegionButton.clicked.connect(self.remove_last_region)
        self.ui.resizeROIButton.clicked.connect(self.resize_roi)
        self.ui.filterButton.clicked.connect(self.plot_filtered)
        self.ui.makeLombButton.clicked.connect(self.make_lomb)
        self.ui.loadAllDataButton.clicked.connect(self.load_all_data)
        self.ui.saveAllDataButton.clicked.connect(self.save_all_data)
        self.ui.polarizationButton.clicked.connect(
            self.make_polarization_plots
        )
        self.ui.helicalBaseComboBox.currentIndexChanged.connect(
            self.populate_helical_orientation
        )
        #   Keypress Connections
        self.ui.shotNumberInput.returnPressed.connect(self.loadData)
        #   Menu bar
        self.ui.actionSave_figure.triggered.connect(self.savefig)
        self.ui.actionLoad_DMUSIC.triggered.connect(self.load_dmusic)
        self.ui.actionMake_DMUSIC.triggered.connect(self.make_dmusic)
        self.ui.actionSet_configuration_folder.triggered.connect(
            self.set_config_folder
        )

    def populate_helical_orientation(self):
        self.ui.helicalOrientationComboBox.clear()
        self.ui.helicalOrientationComboBox.addItems(
            ORIENTATION_TRANSLATION[self.ui.helicalBaseComboBox.currentText()]
        )

    def set_config_folder(self):
        folder = str(
            QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select Directory", dir=paths.CONFIG_PATH
            )
        )
        paths.set_config_folder(folder)

    def make_polarization_plots(self):
        self.info.refresh()
        pol_obj = Polarization(
            self.coilarr,
            self.array.linked_rois.regions[-1],
            self.ui.helicalBaseComboBox.currentText(),
        ).plot()

    def make_lomb(self):
        lomb = Lomb(self.coilarr, self.array.linked_rois.regions)
        lomb.make_lomb(
            self.ui.helicalBaseComboBox.currentText(),
            self.ui.helicalOrientationComboBox.currentText(),
        )
        if self.ui.saveLombCheckBox.isChecked():
            lomb.save(paths.LOMB_OUTPUT_PATH())

    def save_all_data(self):
        self.coilarr.write_hdf5(
            f"{paths.DATA_PATH()}/.mirnov__{self.info.shot}.hdf5"
        )

    def load_all_data(self):
        self.info.refresh()
        if self.info.shot is None:
            return
        self.coilarr = tma.TJII_Mirnov_Arrays(self.info.shot)
        boozfile = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select Boozmn file",
            dir=paths.BOOZER_PATH(),
            filter="Boozmn files (*.nc)",
            selectedFilter="Boozmn files (*.nc)",
        )[0]
        self.booz = vl.Booz(boozfile)
        try:
            self.coilarr.read_hdf5(
                filename=f"{paths.DATA_PATH()}/mirnov__{self.info.shot}.hdf5"
            )
        except:
            try:
                self.coilarr.read_hdf5(initialdir=paths.DATA_PATH())
                self.ui.shotNumberInput.setText(str(self.coilarr.shot))
            except:
                self.coilarr = self.coilarr.load_rawdata(self.info.shot)
        self.coilarr.calculate_bases(self.booz)  # type: ignore

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
        self.array.ax["signal"].ctrl.fftCheck.setChecked(True)
        self.array.ax["signal"].ctrl.logXCheck.setChecked(True)
        self.array.ax["signal"].ctrl.logYCheck.setChecked(True)

    def load_dmusic(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select DMUSIC file",
            dir=paths.DMUSIC_PATH(),
            filter="All Files (*.*);;HDF5 files (*.h5 *.hdf5)",
            selectedFilter="HDF5 files (*.h5 *.hdf5)",
        )[0]
        self.make_array()
        self.array.from_dmusic(path)
        self.array.plot_signals()

    def add_region(self):
        self.array.linked_rois.add_region()

    def remove_last_region(self):
        self.array.linked_rois.remove_last_region()

    def resize_roi(self):
        self.array.linked_rois.resize_roi()

    def plot_filtered(self):
        self.info.refresh()
        self.array.plot_filt_signal()

    def make_dmusic(self):
        filedir = str(
            QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select DMUSIC directory", dir=paths.DMUSIC_PATH()
            )
        )
        print(filedir)
        self.array.make_dmusic(filedir=filedir)
