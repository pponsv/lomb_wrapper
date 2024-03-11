from .utils import get_value_from_field
from .ui.ui_mainwindow import Ui_MainWindow


class WindowInfo:
    def __init__(self, UiClass: Ui_MainWindow):
        self.ui = UiClass
        self.refresh()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def refresh(self):
        self.array = self.ui.signalArraySelector.currentText()
        self.shot = get_value_from_field(self.ui.shotNumberInput, int)

        self.filter_info()
        self.spgram_info()

    def filter_info(self):
        self.flim = (
            get_value_from_field(self.ui.filterFMin, float),
            get_value_from_field(self.ui.filterFMax, float),
        )

    def spgram_info(self):
        self.tlim = (
            get_value_from_field(self.ui.lowerTLim, float),
            get_value_from_field(self.ui.upperTLim, float),
        )
        self.nperseg = get_value_from_field(self.ui.spgramNperseg, int)
        self.noverlap = get_value_from_field(self.ui.spgramNoverlap, int)

        print(self.tlim, self.nperseg, self.noverlap)
