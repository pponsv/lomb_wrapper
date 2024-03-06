from PyQt6 import QtCore
import pyqtgraph as pg

from auxfiles.signal_names import LAYOUT_SIZE

from .class_signals import Signal
from .qt_workers import Worker
from .class_window_info import WindowInfo
from .utils import PEN_BLACK, COLORMAP


class SignalArray:
    def __init__(
        self,
        shot,
        names,
        fig: pg.GraphicsLayoutWidget,
        threadpool: QtCore.QThreadPool,
        info: WindowInfo,
    ):
        self.shot = shot
        self.signals = {name: Signal(shot, name) for name in names}
        self.fig = fig
        self.ax = {}
        self.threadpool = threadpool
        self.info = info

    def read_seq(self):
        for name, signal in self.signals.items():
            signal.read_data()

    def read_parallel(self, printer):
        workers = []
        for name, signal in self.signals.items():
            workers.append(Worker(signal.read_data, printer))
            self.threadpool.start(workers[-1])
        self.threadpool.waitForDone()
        printer("Done")

    def make_axes(self, signals, sharex=False, sharey=False):
        numx, numy = LAYOUT_SIZE.get(len(signals), (1, len(signals)))
        self.fig.clear()
        self.ax = {}
        for i in range(numy):
            for j in range(numx):
                self.ax[(i, j)] = self.fig.addPlot(i, j)
                if sharex is True:
                    self.ax[(i, j)].setXLink(self.ax[(0, 0)])
                if sharey is True:
                    self.ax[(i, j)].setYLink(self.ax[(0, 0)])
                self.ax[(i, j)].setDefaultPadding(0.0)
                self.ax[(i, j)].enableAutoRange(enable=True)
                self.ax[(i, j)].getAxis("left").setWidth(40)
                self.ax[(i, j)].getAxis("right").setWidth(0)
                self.ax[(i, j)].getAxis("bottom").setHeight(20)
                self.ax[(i, j)].getAxis("top").setHeight(0)

    def make_spectrograms(self, printer=print):
        workers = {}
        for signal, pltidx in zip(self.signals.values(), self.ax):
            workers[pltidx] = Worker(
                signal.spectrogram,
                tlim=self.info.tlim,
                nperseg=self.info.nperseg,
                noverlap=self.info.noverlap,
            )
            self.threadpool.start(workers[pltidx])
        self.threadpool.waitForDone()

    def plot_spectrograms(self):
        self.make_axes(self.signals, sharex=True, sharey=True)
        for sig_key, iax in zip(self.signals, self.ax):
            self.signals[sig_key].plot_spec(self.ax[iax], COLORMAP)

    def plot_spec_alone(self, name):
        self.make_axes({name: self.signals[name]})
        self.signals[name].spectrogram(
            self.info.tlim, nperseg=self.info.nperseg, noverlap=self.info.noverlap
        )
        self.signals[name].plot_spec(self.ax[(0, 0)], COLORMAP)

    def plot_signals(self):
        self.make_axes(self.signals, sharex=True, sharey=False)
        for sig_key, pltidx in zip(self.signals, self.ax):
            self.signals[sig_key].plot(
                self.ax[pltidx],
                ds=self.info.downsample,
                dsFactor=self.info.downsampleFactor,
                filt=self.info.filt,
                flim=self.info.flim,
                pen=PEN_BLACK,
            )

    def plot_integrated(self):
        self.make_axes(self.signals, sharex=True, sharey=False)
        for sig_key, pltidx in zip(self.signals, self.ax):
            self.signals[sig_key].plot_integrated(
                self.ax[pltidx],
                ds=self.info.downsample,
                dsFactor=self.info.downsampleFactor,
                pen=PEN_BLACK,
            )

    def plot_alone(self, key):
        self.make_axes({key: self.signals[key]})
        self.signals[key].plot(
            ax=self.ax[(0, 0)],
            ds=self.info.downsample,
            dsFactor=self.info.downsampleFactor,
            filt=self.info.filt,
            flim=self.info.flim,
            pen=PEN_BLACK,
        )
