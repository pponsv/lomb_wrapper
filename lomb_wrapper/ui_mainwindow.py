# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1496, 882)
        MainWindow.setMinimumSize(QSize(1280, 800))
        self.actionSave_figure = QAction(MainWindow)
        self.actionSave_figure.setObjectName(u"actionSave_figure")
        self.actionCheck_DAQ = QAction(MainWindow)
        self.actionCheck_DAQ.setObjectName(u"actionCheck_DAQ")
        self.actionSet_configuration_folder = QAction(MainWindow)
        self.actionSet_configuration_folder.setObjectName(u"actionSet_configuration_folder")
        self.actionMake_DMUSIC = QAction(MainWindow)
        self.actionMake_DMUSIC.setObjectName(u"actionMake_DMUSIC")
        self.actionLoad_DMUSIC = QAction(MainWindow)
        self.actionLoad_DMUSIC.setObjectName(u"actionLoad_DMUSIC")
        self.actionSave_Mirnov = QAction(MainWindow)
        self.actionSave_Mirnov.setObjectName(u"actionSave_Mirnov")
        self.actionSet_boozer_angles = QAction(MainWindow)
        self.actionSet_boozer_angles.setObjectName(u"actionSet_boozer_angles")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.topwidget = QWidget(self.centralwidget)
        self.topwidget.setObjectName(u"topwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topwidget.sizePolicy().hasHeightForWidth())
        self.topwidget.setSizePolicy(sizePolicy)
        self.topwidget.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_2 = QGridLayout(self.topwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.polarizationButton = QPushButton(self.topwidget)
        self.polarizationButton.setObjectName(u"polarizationButton")

        self.gridLayout_2.addWidget(self.polarizationButton, 0, 15, 1, 1)

        self.signalsLabel = QLabel(self.topwidget)
        self.signalsLabel.setObjectName(u"signalsLabel")

        self.gridLayout_2.addWidget(self.signalsLabel, 0, 17, 1, 1)

        self.label_8 = QLabel(self.topwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 8, 1, 1)

        self.filterFMin = QLineEdit(self.topwidget)
        self.filterFMin.setObjectName(u"filterFMin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filterFMin.sizePolicy().hasHeightForWidth())
        self.filterFMin.setSizePolicy(sizePolicy1)
        self.filterFMin.setMinimumSize(QSize(50, 0))
        self.filterFMin.setMaximumSize(QSize(50, 16777215))
        self.filterFMin.setBaseSize(QSize(40, 0))

        self.gridLayout_2.addWidget(self.filterFMin, 0, 9, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 6, 1, 1)

        self.shotNumberInput = QLineEdit(self.topwidget)
        self.shotNumberInput.setObjectName(u"shotNumberInput")
        self.shotNumberInput.setMaximumSize(QSize(80, 22))

        self.gridLayout_2.addWidget(self.shotNumberInput, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 16, 1, 1)

        self.label_9 = QLabel(self.topwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 10, 1, 1)

        self.saveAllDataButton = QPushButton(self.topwidget)
        self.saveAllDataButton.setObjectName(u"saveAllDataButton")

        self.gridLayout_2.addWidget(self.saveAllDataButton, 0, 5, 1, 1)

        self.signalArraySelector = QComboBox(self.topwidget)
        self.signalArraySelector.addItem("")
        self.signalArraySelector.addItem("")
        self.signalArraySelector.setObjectName(u"signalArraySelector")
        self.signalArraySelector.setEditable(True)

        self.gridLayout_2.addWidget(self.signalArraySelector, 0, 18, 1, 1)

        self.loadAllDataButton = QPushButton(self.topwidget)
        self.loadAllDataButton.setObjectName(u"loadAllDataButton")

        self.gridLayout_2.addWidget(self.loadAllDataButton, 0, 4, 1, 1)

        self.filterFMax = QLineEdit(self.topwidget)
        self.filterFMax.setObjectName(u"filterFMax")
        sizePolicy1.setHeightForWidth(self.filterFMax.sizePolicy().hasHeightForWidth())
        self.filterFMax.setSizePolicy(sizePolicy1)
        self.filterFMax.setMinimumSize(QSize(50, 0))
        self.filterFMax.setMaximumSize(QSize(50, 16777215))
        self.filterFMax.setBaseSize(QSize(40, 0))

        self.gridLayout_2.addWidget(self.filterFMax, 0, 11, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 14, 1, 1)

        self.label = QLabel(self.topwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.loadDataButton = QPushButton(self.topwidget)
        self.loadDataButton.setObjectName(u"loadDataButton")

        self.gridLayout_2.addWidget(self.loadDataButton, 0, 2, 1, 1)

        self.label_10 = QLabel(self.topwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 12, 1, 1)

        self.refreshButton = QPushButton(self.topwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.gridLayout_2.addWidget(self.refreshButton, 0, 19, 1, 1)

        self.filterButton = QPushButton(self.topwidget)
        self.filterButton.setObjectName(u"filterButton")

        self.gridLayout_2.addWidget(self.filterButton, 0, 7, 1, 1)

        self.lastShotButton = QPushButton(self.topwidget)
        self.lastShotButton.setObjectName(u"lastShotButton")

        self.gridLayout_2.addWidget(self.lastShotButton, 0, 3, 1, 1)

        self.getFlimButton = QPushButton(self.topwidget)
        self.getFlimButton.setObjectName(u"getFlimButton")

        self.gridLayout_2.addWidget(self.getFlimButton, 0, 13, 1, 1)


        self.gridLayout.addWidget(self.topwidget, 0, 0, 1, 1)

        self.bottomwidget = QWidget(self.centralwidget)
        self.bottomwidget.setObjectName(u"bottomwidget")
        sizePolicy.setHeightForWidth(self.bottomwidget.sizePolicy().hasHeightForWidth())
        self.bottomwidget.setSizePolicy(sizePolicy)
        self.bottomwidget.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_3 = QGridLayout(self.bottomwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.resizeROIButton = QPushButton(self.bottomwidget)
        self.resizeROIButton.setObjectName(u"resizeROIButton")

        self.gridLayout_3.addWidget(self.resizeROIButton, 1, 3, 1, 1)

        self.label_2 = QLabel(self.bottomwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 8, 1, 1)

        self.spgramNoverlap = QLineEdit(self.bottomwidget)
        self.spgramNoverlap.setObjectName(u"spgramNoverlap")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spgramNoverlap.sizePolicy().hasHeightForWidth())
        self.spgramNoverlap.setSizePolicy(sizePolicy2)
        self.spgramNoverlap.setMinimumSize(QSize(50, 22))
        self.spgramNoverlap.setMaximumSize(QSize(70, 22))
        self.spgramNoverlap.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.spgramNoverlap, 1, 24, 1, 1)

        self.helicalBaseComboBox = QComboBox(self.bottomwidget)
        self.helicalBaseComboBox.addItem("")
        self.helicalBaseComboBox.addItem("")
        self.helicalBaseComboBox.addItem("")
        self.helicalBaseComboBox.setObjectName(u"helicalBaseComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.helicalBaseComboBox.sizePolicy().hasHeightForWidth())
        self.helicalBaseComboBox.setSizePolicy(sizePolicy3)
        self.helicalBaseComboBox.setMinimumSize(QSize(90, 0))
        self.helicalBaseComboBox.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_3.addWidget(self.helicalBaseComboBox, 1, 10, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 16, 1, 1)

        self.fftButton = QPushButton(self.bottomwidget)
        self.fftButton.setObjectName(u"fftButton")
        self.fftButton.setMinimumSize(QSize(50, 0))
        self.fftButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.fftButton, 1, 1, 1, 1)

        self.removeLastRegionButton = QPushButton(self.bottomwidget)
        self.removeLastRegionButton.setObjectName(u"removeLastRegionButton")

        self.gridLayout_3.addWidget(self.removeLastRegionButton, 1, 5, 1, 1)

        self.upperTLim = QLineEdit(self.bottomwidget)
        self.upperTLim.setObjectName(u"upperTLim")
        self.upperTLim.setMinimumSize(QSize(70, 22))
        self.upperTLim.setMaximumSize(QSize(70, 22))
        self.upperTLim.setBaseSize(QSize(70, 22))
        self.upperTLim.setAlignment(Qt.AlignCenter)
        self.upperTLim.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.upperTLim, 1, 20, 1, 1)

        self.spgramNperseg = QLineEdit(self.bottomwidget)
        self.spgramNperseg.setObjectName(u"spgramNperseg")
        self.spgramNperseg.setMinimumSize(QSize(50, 0))
        self.spgramNperseg.setMaximumSize(QSize(80, 22))
        self.spgramNperseg.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.spgramNperseg, 1, 22, 1, 1)

        self.label_5 = QLabel(self.bottomwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 19, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 7, 1, 1)

        self.label_7 = QLabel(self.bottomwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 23, 1, 1)

        self.makeLombButton = QPushButton(self.bottomwidget)
        self.makeLombButton.setObjectName(u"makeLombButton")

        self.gridLayout_3.addWidget(self.makeLombButton, 1, 13, 1, 1)

        self.integrateDataButton = QPushButton(self.bottomwidget)
        self.integrateDataButton.setObjectName(u"integrateDataButton")

        self.gridLayout_3.addWidget(self.integrateDataButton, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.helicalOrientationComboBox = QComboBox(self.bottomwidget)
        self.helicalOrientationComboBox.addItem("")
        self.helicalOrientationComboBox.addItem("")
        self.helicalOrientationComboBox.addItem("")
        self.helicalOrientationComboBox.setObjectName(u"helicalOrientationComboBox")
        self.helicalOrientationComboBox.setMinimumSize(QSize(50, 0))
        self.helicalOrientationComboBox.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.helicalOrientationComboBox, 1, 12, 1, 1)

        self.label_4 = QLabel(self.bottomwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 11, 1, 1)

        self.lowerTLim = QLineEdit(self.bottomwidget)
        self.lowerTLim.setObjectName(u"lowerTLim")
        sizePolicy2.setHeightForWidth(self.lowerTLim.sizePolicy().hasHeightForWidth())
        self.lowerTLim.setSizePolicy(sizePolicy2)
        self.lowerTLim.setMinimumSize(QSize(70, 22))
        self.lowerTLim.setMaximumSize(QSize(70, 22))
        self.lowerTLim.setBaseSize(QSize(70, 22))
        self.lowerTLim.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lowerTLim, 1, 18, 1, 1)

        self.label_3 = QLabel(self.bottomwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 17, 1, 1)

        self.label_6 = QLabel(self.bottomwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 21, 1, 1)

        self.addRegionButton = QPushButton(self.bottomwidget)
        self.addRegionButton.setObjectName(u"addRegionButton")

        self.gridLayout_3.addWidget(self.addRegionButton, 1, 4, 1, 1)

        self.saveLombCheckBox = QCheckBox(self.bottomwidget)
        self.saveLombCheckBox.setObjectName(u"saveLombCheckBox")

        self.gridLayout_3.addWidget(self.saveLombCheckBox, 1, 14, 1, 1)

        self.plotLombCheckBox = QCheckBox(self.bottomwidget)
        self.plotLombCheckBox.setObjectName(u"plotLombCheckBox")

        self.gridLayout_3.addWidget(self.plotLombCheckBox, 1, 15, 1, 1)


        self.gridLayout.addWidget(self.bottomwidget, 2, 0, 1, 1)

        self.figLayout = GraphicsLayoutWidget(self.centralwidget)
        self.figLayout.setObjectName(u"figLayout")
        self.figLayout.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.figLayout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout.addWidget(self.figLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1496, 19))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuDMUSIC = QMenu(self.menubar)
        self.menuDMUSIC.setObjectName(u"menuDMUSIC")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuDMUSIC.menuAction())
        self.menuArchivo.addAction(self.actionSave_figure)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSet_configuration_folder)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSave_Mirnov)
        self.menuArchivo.addAction(self.actionSet_boozer_angles)
        self.menuDMUSIC.addAction(self.actionMake_DMUSIC)
        self.menuDMUSIC.addAction(self.actionLoad_DMUSIC)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lomb periodogram helper", None))
        self.actionSave_figure.setText(QCoreApplication.translate("MainWindow", u"Save figure", None))
        self.actionCheck_DAQ.setText(QCoreApplication.translate("MainWindow", u"Check DAQ", None))
        self.actionSet_configuration_folder.setText(QCoreApplication.translate("MainWindow", u"Set configuration folder", None))
        self.actionMake_DMUSIC.setText(QCoreApplication.translate("MainWindow", u"Make DMUSIC", None))
        self.actionLoad_DMUSIC.setText(QCoreApplication.translate("MainWindow", u"Load DMUSIC", None))
        self.actionSave_Mirnov.setText(QCoreApplication.translate("MainWindow", u"Save Mirnov", None))
        self.actionSet_boozer_angles.setText(QCoreApplication.translate("MainWindow", u"Set boozer angles", None))
        self.polarizationButton.setText(QCoreApplication.translate("MainWindow", u"See polarization", None))
        self.signalsLabel.setText(QCoreApplication.translate("MainWindow", u"Signal: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>f<span style=\" vertical-align:sub;\">min</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>f<span style=\" vertical-align:sub;\">max</span></p></body></html>", None))
        self.saveAllDataButton.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
        self.signalArraySelector.setItemText(0, QCoreApplication.translate("MainWindow", u"MIR5C", None))
        self.signalArraySelector.setItemText(1, QCoreApplication.translate("MainWindow", u"H1P01", None))

        self.loadAllDataButton.setText(QCoreApplication.translate("MainWindow", u"Load All", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shot:", None))
        self.loadDataButton.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>[kHz]</p></body></html>", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.lastShotButton.setText(QCoreApplication.translate("MainWindow", u"Last shot", None))
        self.getFlimButton.setText(QCoreApplication.translate("MainWindow", u"Get flim", None))
        self.resizeROIButton.setText(QCoreApplication.translate("MainWindow", u"Resize ROI", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Helical - Base:", None))
        self.spgramNoverlap.setText(QCoreApplication.translate("MainWindow", u"1020", None))
        self.spgramNoverlap.setPlaceholderText(QCoreApplication.translate("MainWindow", u"noverlap", None))
        self.helicalBaseComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Booz_sup", None))
        self.helicalBaseComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Booz_sub", None))
        self.helicalBaseComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Design", None))

        self.fftButton.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.removeLastRegionButton.setText(QCoreApplication.translate("MainWindow", u"Remove Region", None))
        self.upperTLim.setText(QCoreApplication.translate("MainWindow", u"1250", None))
        self.upperTLim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Upper limit [ms]", None))
        self.spgramNperseg.setText(QCoreApplication.translate("MainWindow", u"1024", None))
        self.spgramNperseg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nperseg", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"t<sub>1</sub>:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"noverlap:", None))
        self.makeLombButton.setText(QCoreApplication.translate("MainWindow", u"Make Periodograms", None))
        self.integrateDataButton.setText(QCoreApplication.translate("MainWindow", u"Integrate", None))
        self.helicalOrientationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"T", None))
        self.helicalOrientationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"P", None))
        self.helicalOrientationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"R", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Orientation:", None))
        self.lowerTLim.setText(QCoreApplication.translate("MainWindow", u"1050", None))
        self.lowerTLim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lower limit [ms]", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"t<sub>0</sub>:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"nperseg:", None))
        self.addRegionButton.setText(QCoreApplication.translate("MainWindow", u"Add Region", None))
        self.saveLombCheckBox.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.plotLombCheckBox.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.menuDMUSIC.setTitle(QCoreApplication.translate("MainWindow", u"DMUSIC", None))
    # retranslateUi

