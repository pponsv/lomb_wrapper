import numpy as np
import matplotlib.pyplot as plt

import lomb_periodogram as lp
import TJII_mirnov_array as tma
from .class_linked_rois import Region
from . import paths

NMAX = 15
MMAX = 15
NS = np.arange(-NMAX, NMAX + 1)
MS = np.arange(-MMAX, MMAX + 1)

BASE_TRANSLATION = {
    "Booz_sup": "sup",
    "Booz_sub": "sub",
    "Design": "normals_th",
}

ORIENTATION_TRANSLATION = {
    "Booz_sup": ["ph", "th", "s"],
    "Booz_sub": ["ph", "th", "s"],
    "Design": ["T", "P", "R"],
}


class Lomb:
    def __init__(
        self,
        coilarr: tma.TJII_Mirnov_Arrays,
        roilist: list[Region],
    ):
        self.coilarr = coilarr
        self.roilist = roilist
        self.coilarr.polarr.get_calfacs(paths.POLOIDAL_CALIBRATION_PATH())
        self.coilarr.torarr.get_calfacs(paths.HELICAL_CALIBRATION_PATH())

    def make_lomb(self, base_str: str, orientation):
        base_str = BASE_TRANSLATION[base_str]
        for roi in self.roilist:
            self.make_lomb_poloidal(roi)
            self.make_lomb_helical(roi, base_str, orientation)
        plt.show(block=False)

    def make_lomb_poloidal(self, roi: Region):
        times, signals, thetas, phis = self.coilarr.polarr.make_lomb_arrays(
            tlim=roi.tlim, flim=roi.flim
        )
        title = f"Shot {self.coilarr.shot}, poloidal, f0 = {roi.f0:.2f} kHz, tlim=({roi.tlim[0]:.2f}, {roi.tlim[1]:.2f})"
        self.make_lomb_wrap(times, signals, thetas, phis, roi.f0, title)

    def make_lomb_helical(self, roi: Region, base_str: str, orientation: str):
        times, signals, thetas, phis = self.coilarr.torarr.make_lomb_arrays(
            tlim=roi.tlim,
            flim=roi.flim,
            base_str=base_str,
            orientation=orientation,
        )
        title = f"Shot {self.coilarr.shot}, helical {base_str} {orientation}, f0 = {roi.f0:.2f} kHz, tlim=({roi.tlim[0]:.2f}, {roi.tlim[1]:.2f})"
        self.make_lomb_wrap(times, signals, thetas, phis, roi.f0, title)

    @staticmethod
    def make_lomb_wrap(times, signals, thetas, phis, f0, title):
        lomb = lp.Lomb_vec(
            time=times,
            thetas=thetas,
            phis=phis,
            sigs=signals,
            nmax=NMAX,
            mmax=MMAX,
        )
        lomb.easylomb3_difftimes(f0)
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        ax[0].plot(times, signals + 10 * thetas, "-", ms=1, lw=0.1)
        lomb.plotmapa(ax[1])
        fig.suptitle(title)
