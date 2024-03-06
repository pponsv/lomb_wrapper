from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.uic.load_ui import loadUiType

from lib import TJII_data_acquisition as da

Ui_Dialog, QtBaseClass = loadUiType("ui/ListDialog.ui")
CLEAR_RED = QtGui.QColor(255, 0, 0, 80)


class DAQ_dialog(QtWidgets.QDialog):
    def __init__(self, shot, names):
        super(DAQ_dialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.shot = shot
        self.names = names

        self.ui.daqTableWidget.setColumnCount(4)
        self.ui.daqTableWidget.setHorizontalHeaderLabels(
            ["SHOT", "SIGNAL", "NDAT", "IERR"]
        )
        self.ui.daqTableWidget.setSortingEnabled(True)

        self.ui.okButton.clicked.connect(self.close)

        self.show()
        self.get_info()
        self.disp_info()

        self.ui.daqTableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection
        )
        self.ui.daqTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.ui.daqTableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)

    def get_info(self):
        self.daq_list = []
        for name in self.names:
            ndat, nvent, ierr = da.py_dimens(self.shot, name)
            self.daq_list.append([self.shot, name, ndat, ierr])

    def disp_info(self):
        self.ui.daqTableWidget.setRowCount(len(self.names))
        for ridx, daq_item in enumerate(self.daq_list):
            for cidx, item in enumerate(daq_item):
                self.ui.daqTableWidget.setItem(
                    ridx, cidx, QtWidgets.QTableWidgetItem(str(item))
                )
                if daq_item[3] != 0:
                    self.ui.daqTableWidget.item(ridx, cidx).setBackground(CLEAR_RED)
        self.ui.daqTableWidget.sortByColumn(3, QtCore.Qt.SortOrder.DescendingOrder)
