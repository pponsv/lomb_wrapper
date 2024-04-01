import numpy as np
import matplotlib.pyplot as plt

from lib import lomb_periodogram as lp
from lib import TJII_mirnov_array as tma
from .class_linked_rois import Region


class Lomb:
    def __init__(
        self,
        coilarr: tma.TJII_Mirnov_Arrays,
        roilist: list[Region],
    ):
        self.coilarr = coilarr
        self.roilist = roilist

    def make_lomb(self):
        for roi in self.roilist:
            self.make_lomb_poloidal(roi)

    def make_lomb_poloidal(self, roi: Region):
        NMAX = 15
        MMAX = 15
        NS = np.arange(-NMAX, NMAX + 1)
        MS = np.arange(-MMAX, MMAX + 1)

        times, signals, thetas, phis = self.coilarr.polarr.make_lomb_arrays(
            tlim=roi.tlim, flim=roi.flim
        )

        plt.plot(times, signals + 10 * thetas, "-", ms=1, lw=0.1)

        mapa = lp.easylomb3_difftimes(
            times, thetas, phis, signals, roi.f0, NS, MS
        )
        fig, ax = plt.subplots(1, 1)
        title = f"Shot {self.coilarr.shot}, poloidal, f0 = {roi.f0} kHz"
        lp.plotmapa_alone_new(mapa, NS, MS, ax, title=title)
        plt.show()
