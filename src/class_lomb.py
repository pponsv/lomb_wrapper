import numpy as np
import matplotlib.pyplot as plt

from lib import lomb_periodogram as lp
from lib import TJII_mirnov_array as tma
from .class_linked_rois import Region
from . import paths


class Lomb:
    def __init__(
        self,
        coilarr: tma.TJII_Mirnov_Arrays,
        roilist: list[Region],
    ):
        self.coilarr = coilarr
        self.roilist = roilist
        self.coilarr.polarr.get_calfacs(paths.POLOIDAL_CALIBRATION_PATH)

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

        mapa = lp.easylomb3_difftimes(
            times, thetas, phis, signals, roi.f0, NS, MS
        )
        fig, ax = plt.subplots(1, 2)
        title = f"Shot {self.coilarr.shot}, poloidal, f0 = {roi.f0:.2f} kHz, tlim=({roi.tlim[0]:.2f}, {roi.tlim[1]:.2f})"
        ax[0].plot(times, signals + 10 * thetas, "-", ms=1, lw=0.1)
        lp.plotmapa_alone_new(mapa, NS, MS, ax[1], title=title)
        plt.show()
