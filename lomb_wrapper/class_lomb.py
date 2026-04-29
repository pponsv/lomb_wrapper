import os

import lomb_periodogram as lp
import matplotlib.pyplot as plt
import numpy as np
import TJII_mirnov_array as tma

from . import paths
from .class_linked_rois import Region

NMAX = 15
MMAX = 15
NS = np.arange(-NMAX, NMAX + 1)
MS = np.arange(-MMAX, MMAX + 1)

BASE_TRANSLATION = {
    "Booz_sup": "sup",
    "Booz_sub": "sub",
    "Design": "normal_th",
}

ORIENTATION_TRANSLATION = {
    "Booz_sup": ["s", "th", "ph"],
    "Booz_sub": ["th", "ph", "s"],
    "Design": ["T", "P", "R"],
}


class Lomb:
    lombs: list[tuple[lp.Lomb_vec, lp.Lomb_vec]]

    def __init__(
        self,
        coilarr: tma.TJII_Mirnov_Arrays,
        roilist: list[Region],
        plot=False,
    ):
        self.coilarr = coilarr
        self.roilist = roilist
        self.coilarr.polarr.get_calfacs(paths.POLOIDAL_CALIBRATION_PATH())
        self.coilarr.torarr.get_calfacs(paths.HELICAL_CALIBRATION_PATH())
        self.lombs = []
        self.plot = plot

    def make_lomb(self, base_str: str, orientation):
        base_str = BASE_TRANSLATION[base_str]
        for roi in self.roilist:
            lomb_pol = self.make_lomb_poloidal(roi)
            lomb_hel = self.make_lomb_helical(roi, base_str, orientation)
            self.lombs.append((lomb_pol, lomb_hel))
            prod_mapa = self.lomb_product(lomb_hel, lomb_pol)
            if self.plot is True:
                fig, ax = plt.subplots(1, 1, figsize=(5, 5))
                lp.plots.plotmapa_alone_ax(prod_mapa, NS, MS, ax=ax)
        plt.show(block=False)

    def make_lomb_poloidal(self, roi: Region):
        times, signals, thetas, phis = self.coilarr.polarr.make_lomb_arrays(
            tlim=roi.tlim, flim=roi.flim
        )
        title = f"Shot {self.coilarr.shot}, poloidal, f0 = {roi.f0:.2f} kHz, tlim=({roi.tlim[0]:.2f}, {roi.tlim[1]:.2f})"
        lomb = self.make_lomb_wrap(
            times, signals, thetas, phis, roi.f0, title, plot=self.plot
        )
        return lomb

    def make_lomb_helical(self, roi: Region, base_str: str, orientation: str):
        times, signals, thetas, phis = self.coilarr.torarr.make_lomb_arrays(
            tlim=roi.tlim,
            flim=roi.flim,
            base_str=base_str,
            orientation=orientation,
        )
        title = f"Shot {self.coilarr.shot}, helical {base_str} {orientation}, f0 = {roi.f0:.2f} kHz, tlim=({roi.tlim[0]:.2f}, {roi.tlim[1]:.2f})"
        lomb = self.make_lomb_wrap(
            times, signals, thetas, phis, roi.f0, title, plot=self.plot
        )
        return lomb

    @staticmethod
    def make_lomb_wrap(times, signals, thetas, phis, f0, title, plot=False):
        lomb = lp.Lomb_vec(
            time=times,
            thetas=thetas,
            phis=phis,
            sigs=signals,
            nmax=NMAX,
            mmax=MMAX,
        )
        lomb.easylomb3_difftimes(f0)
        if plot is True:
            fig, ax = plt.subplots(1, 2, figsize=(10, 5))
            ax[0].plot(times, signals + 10 * thetas, "-", ms=1, lw=0.1)  # type: ignore
            lomb.plotmapa(ax[1])  # type: ignore
            fig.suptitle(title)
        return lomb

    @staticmethod
    def lomb_product(lomb1: lp.Lomb_vec, lomb2: lp.Lomb_vec):
        assert (lomb1.ns == lomb2.ns).all(), "Different ns"
        assert (lomb1.ms == lomb2.ms).all(), "Different ms"
        return lomb1.mapa * lomb2.mapa

    def save(self, datapath: str):
        os.makedirs(f"{datapath}/{self.coilarr.shot}", exist_ok=True)
        for (l_pol, l_hel), roi in zip(self.lombs, self.roilist):
            l_pol.to_hdf(
                f"{datapath}/{self.coilarr.shot}/lomb_pol__{l_pol.f0:.2f}__{roi.tlim[0]:.2f}_{roi.tlim[1]:.2f}.hdf5"
            )
            l_hel.to_hdf(
                f"{datapath}/{self.coilarr.shot}/lomb_hel__{l_hel.f0:.2f}__{roi.tlim[0]:.2f}_{roi.tlim[1]:.2f}.hdf5"
            )
