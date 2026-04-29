from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

import TJII_mirnov_array as tma
from TJII_mirnov_array.src.utils.data import (
    bandpass_filter_vec,
    normalize_to_env,
)

from .class_linked_rois import Region
from .class_lomb import BASE_TRANSLATION, ORIENTATION_TRANSLATION


class Polarization:
    def __init__(
        self, coilarr: tma.TJII_Mirnov_Arrays, roi: Region, base: str
    ):
        self.coilarr = coilarr
        self.roi = roi
        self.make_signal_arrays(base)

    def make_signal_arrays(self, base: str):
        orientations = ORIENTATION_TRANSLATION[base]
        self.base = BASE_TRANSLATION[base]
        self.sigs = {}
        for ori in combinations(orientations, 2):
            self.sigs[ori] = self.make_polarization_arrays(
                self.roi.tlim, self.roi.flim, self.base, ori
            )

    def plot(self):
        figs = {}
        axes = {}
        for ori in self.sigs:
            figs[ori]["upper"], axes[ori]["upper"] = plt.subplots(
                5,
                7,
                constrained_layout=True,
                figsize=(12, 9),
                sharex=True,
                sharey=True,
                subplot_kw=dict(box_aspect=1),
            )
            figs[ori]["lower"], axes[ori]["lower"] = plt.subplots(
                5,
                7,
                constrained_layout=True,
                figsize=(12, 9),
                sharex=True,
                sharey=True,
                subplot_kw=dict(box_aspect=1),
            )
            for subarr in figs[ori]:
                figs[ori][subarr].suptitle(
                    f"Shot {self.coilarr.shot}, helical, {self.base}, {ori}, {subarr}"
                )
            for idx, key in enumerate(self.sigs):
                print(key)
                axes[ori][subarr].plot(
                    self.sigs[key][ori[0]],
                    self.sigs[key][ori[1]],
                    ".k",
                )
                axes[ori][subarr].set(title=key.icoil)
            # axes[0, 0].set_aspect("equal")
            plt.show(block=False)

    def make_polarization_arrays(
        self, tlim, flim, base_str: str, orientation: tuple[str, str]
    ):
        sigs = {}
        for coil in self.coilarr.torarr.coils:
            if (not coil.is_good) or (coil.ierr != 0):
                continue
            print(coil.icoil, coil.coils[0].name)
            mask = (coil.time > tlim[0]) & (coil.time < tlim[1])
            dt = np.mean(np.diff(coil.time)).item()
            sigs[coil] = {}
            if (not coil.is_good) or (coil.ierr != 0):
                continue
            for ori in orientation:
                coil.get_base_pert(base_str, ori)
                sigs[coil][ori] = normalize_to_env(
                    bandpass_filter_vec(coil.base_pert, flim, dt)[mask]
                )
        return sigs
