from PySide6 import QtCore
import pyqtgraph as pg

from .class_signals import Signal
from .qt_workers import Worker
from .class_window_info import WindowInfo
from .utils import PEN_BLACK, COLORMAP
from lib import py_dmusic


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

    def add_roi(self):
        bounds = (*self.ax["signal"].viewRange()[0],)
        self.roi = pg.LinearRegionItem(values=bounds)
        self.roi.setZValue(10)
        self.ax["signal"].addItem(self.roi)
        print(bounds)
        self.roi.setBounds(bounds)
        self.roi.setSpan

    def make_axes(self):
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

    def plot_signals(self):
        self.make_axes()
        self.plot_signal()
        self.plot_spectrogram()

    def plot_spectrogram(self):
        self.signal.plot_spec(self.ax["spgram"], COLORMAP)

    def plot_signal(self):
        self.signal.plot(
            self.ax["signal"],
            filt=self.info.filt,
            flim=self.info.flim,
            pen=PEN_BLACK,
        )
        self.signal.plot_spec(self.ax["spgram"], COLORMAP)
        self.add_roi()

    def plot_integrated(self):
        self.make_axes()
        self.signal.plot_integrated(
            self.ax["signal"],
            pen=PEN_BLACK,
        )

    def load_dmusic(self, path):
        self.dmusic = py_dmusic.DMusic.load_dmusic_class(path)

    def plot_dmusic(self):
        self.ax["spgram"].clear()
        self.ax["spgram"].setLabels(left=self.signal)
        x0, y0 = self.dmusic.ts[0], self.dmusic.fs[0]
        w = self.dmusic.ts[-1] - x0
        h = self.dmusic.fs[-1] - y0
        img = pg.ImageItem(
            image=self.dmusic.ps, levels=(-40, 0), rect=[x0, y0, w, h]
        )
        self.ax["spgram"].addItem(img)
        self.ax["spgram"].setXRange(x0, x0 + w)
        self.ax["spgram"].setYRange(y0, y0 + h)
        cbar = self.ax["spgram"].addColorBar(
            img, colorMap=COLORMAP, values=(-40, 0), width=0.25
        )
        cbar.getAxis("right").setWidth(25)
