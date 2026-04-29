import numpy as np
import py_dmusic
import pyqtgraph as pg
from PySide6 import QtCore, QtWidgets

from .class_linked_rois import Linked_ROIS
from .class_signals import Signal
from .class_window_info import WindowInfo
from .qt_workers import Worker
from .utils import COLORMAP, PEN_BLACK


class Signal_Spgram:
    ax: dict[str, pg.PlotItem]

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
        self.linked_rois = Linked_ROIS(self.ax["signal"], self.ax["spgram"])

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
        self.add_roi()

    def plot_spectrogram(self):
        self.signal.plot_spec(self.ax["spgram"], COLORMAP)

    def plot_signal(self):
        self.signal.plot(
            self.ax["signal"],
            pen=PEN_BLACK,
        )

    def plot_filt_signal(self):
        self.ax["signal"].clear()
        self.signal.plot_filt(
            self.ax["signal"],
            self.info.flim,
            pen=PEN_BLACK,
        )
        self.ax["signal"].enableAutoRange(enable=True, y=True, x=False)
        self.ax["signal"].addItem(self.linked_rois.roi_signal)

    def plot_integrated(self):
        self.ax["signal"].clear()
        self.signal.plot_integrated(
            self.ax["signal"],
            pen=PEN_BLACK,
        )
        self.ax["signal"].enableAutoRange(enable=True, y=True, x=False)
        self.ax["signal"].addItem(self.linked_rois.roi_signal)

    def from_dmusic(self, path):
        self.dmusic = py_dmusic.DMusic.load_dmusic_class(path)
        self.signal.t = np.array(self.dmusic.t)
        self.signal.x = np.array(self.dmusic.y)
        self.signal.spec_freqs = self.dmusic.fs
        self.signal.spec_times = self.dmusic.ts
        self.signal.spec_vals = self.dmusic.ps
        self.signal.dt = self.signal.t[1] - self.signal.t[0]

    def make_dmusic(self, filedir):
        mask = (self.signal.t > self.linked_rois.xlim[0]) & (
            self.signal.t < self.linked_rois.xlim[1]
        )
        self.dmusic = py_dmusic.DMusic(
            t=self.signal.t[mask],
            y=self.signal.x[mask],
            poverlap=0.98,
            N=500,
            J=250,
            K=35,
            flim=self.linked_rois.ylim,
        )
        self.dmusic.spgram_dmusic()
        self.dmusic.save_dmusic(
            shot=self.info.shot,
            savefile="tmp.h5",
            savedir=filedir,  # type: ignore
        )
