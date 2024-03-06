from lib import TJII_data_acquisition as da


import numpy as np
import pyqtgraph as pg
from scipy.integrate import cumulative_trapezoid
from scipy.signal import spectrogram
from .utils import bandpass_filter_vec, PEN_BLACK, COLORMAP


class Signal:
    def __init__(self, shot, name):
        self.shot = shot
        self.name = name

    def read_data(self, printer=print):
        t, x, ierr = da.py_lectur(self.shot, self.name)
        if ierr == 0:
            self.t = t
            self.x = x
            self.dt = t[1] - t[0]
        else:
            print(f"{self.shot} {self.name} - Error {ierr}:")
            self.t = np.array([0])
            self.x = np.array([0])
            self.dt = 1
        self.ierr = ierr
        printer(f"{self.shot} {self.name} - Done")
        if printer is not print:
            print(f"{self.shot} {self.name} - Done")
        return self.shot, self.name

    def plot(self, ax, ds, dsFactor, filt, flim, pen=PEN_BLACK):
        ax.clear()
        ax.setLabels(left=self.name)
        if self.ierr != 0:
            return
        if filt is True:
            x = self.filter(flim)
        else:
            x = self.x
        skip = dsFactor if ds else 1
        ax.plot(self.t[::skip], x[::skip], pen=pen)

    def plot_integrated(self, ax, ds, dsFactor, pen):
        ax.clear()
        nx = cumulative_trapezoid(self.x - np.mean(self.x), self.t, initial=0)
        if ds is True:
            ax.plot(self.t[::dsFactor], nx[::dsFactor], pen=pen)
        else:
            ax.plot(self.t, nx, pen=pen)
        ax.setLabels(left=self.name)
        axis = ax.getAxis("left")
        axis.setWidth(40)

    def spectrogram(self, tlim, nperseg, noverlap):
        if self.ierr != 0:
            return
        dt = np.mean(np.diff(self.t)).item()
        mask = (self.t > tlim[0]) & (self.t < tlim[1])
        self.spec_freqs, self.spec_times, sxx = spectrogram(
            self.x[mask],
            fs=round(1.0 / dt),
            window="hamming",
            nperseg=nperseg,
            noverlap=noverlap,
            return_onesided=True,
        )
        self.spec_vals = 10 * np.log10(sxx / sxx.max())
        self.spec_times += self.t[mask][0]
        print(f"Spgram {self.name} done - {tlim} - {nperseg} - {noverlap}")

    def plot_spec(self, ax, colormap):
        ax.clear()
        ax.setLabels(left=self.name)
        if self.ierr != 0:
            return
        if hasattr(self, "spec_freqs"):
            x0, y0 = self.spec_times[0], self.spec_freqs[0]
            w = self.spec_times[-1] - x0
            h = self.spec_freqs[-1] - y0
            img = pg.ImageItem(
                image=self.spec_vals.T, levels=(-40, 0), rect=[x0, y0, w, h]
            )
            ax.addItem(img)
            ax.setXRange(x0, x0 + w)
            ax.setYRange(y0, y0 + h)
            cbar = ax.addColorBar(img, colorMap=colormap, values=(-40, 0), width=0.25)
            cbar.getAxis("right").setWidth(25)

    def filter(self, flim):
        return bandpass_filter_vec(self.x, flim, self.dt)
