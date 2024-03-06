from .utils import get_value_from_field


class WindowInfo:
    def __init__(self, UiClass):
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
        self.downsampleFactor = get_value_from_field(self.ui.downsampleFactorBox, int)

        self.downsample = self.ui.downsampleBox.isChecked()
        self.selectedCoil = self.ui.coilDataRetrievalSelector.currentText()
        self.filter_info()
        self.spgram_info()

    def filter_info(self):
        self.filt = self.ui.filterCheckbox.isChecked()
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
