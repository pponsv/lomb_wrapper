from PySide6 import QtCore
import pyqtgraph as pg

from .class_signals import Signal
from .qt_workers import Worker
from .class_window_info import WindowInfo
from .utils import PEN_BLACK, COLORMAP


class Signal_Spgram:
    def __init__(
        self,
        shot,
        name,
        fig: pg.GraphicsLayoutWidget,
        threadpool: QtCore.QThreadPool,
        info: WindowInfo,
    ):
        self.shot = shot
        self.signal = Signal(shot, name)
        self.fig = fig
        self.ax = {}
        self.threadpool = threadpool
        self.info = info

    def read_seq(self):
        self.signal.read_data()

    def add_roi(self, event):
        print(self.fig.mousePressEvent)

    def make_axes(self, signals, sharex=False, sharey=False):
        numx, numy = 1, 2
        self.fig.clear()
        self.ax = {}
        self.ax["spgram"] = self.fig.addPlot(row=0, col=0)
        self.ax["signal"] = self.fig.addPlot(row=1, col=0)
        self.ax["signal"].setXLink(self.ax["spgram"])
        for key in self.ax:
            self.ax[key].setDefaultPadding(0.0)
            self.ax[key].enableAutoRange(enable=True)
            self.ax[key].getAxis("left").setWidth(40)
            self.ax[key].getAxis("right").setWidth(0)
            self.ax[key].getAxis("bottom").setHeight(20)
            self.ax[key].getAxis("top").setHeight(0)
        # self.roi_sig = pg.RectROI([0, 0], [0, 0], pen=PEN_BLACK)

    def make_spectrograms(self, printer=print):
        self.signal.spectrogram(
            tlim=self.info.tlim,
            nperseg=self.info.nperseg,
            noverlap=self.info.noverlap,
        )

    def plot_spectrograms(self):
        self.make_axes(self.signal, sharex=True, sharey=True)
        self.signal.plot_spec(self.ax["spgram"], COLORMAP)

    def plot_signals(self):
        self.make_axes(self.signal, sharex=True, sharey=False)
        self.signal.plot(
            self.ax["signal"],
            filt=self.info.filt,
            flim=self.info.flim,
            pen=PEN_BLACK,
        )
        self.signal.plot_spec(self.ax["spgram"], COLORMAP)

    def plot_integrated(self):
        self.make_axes(self.signal, sharex=True, sharey=False)
        self.signal.plot_integrated(
            self.ax["signal"],
            pen=PEN_BLACK,
        )
