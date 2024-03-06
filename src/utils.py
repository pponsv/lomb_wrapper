import os
import numpy as np
import pyqtgraph as pg
from pyqtgraph.exporters import ImageExporter
from auxfiles.signal_names import SIGNAL_NAMES

from scipy.signal import buttord, butter, sosfilt
from lib import TJII_data_acquisition as da


PEN_BLACK = pg.mkPen(color="#000000", width=1)
COLORMAP = pg.colormap.get("CET-R4")


def get_names(arr_text: str):
    if arr_text in SIGNAL_NAMES.keys():
        names = SIGNAL_NAMES[arr_text]
    else:
        names = arr_text.strip("[]").split(", ")
    print("Names: ", names)
    return names


def getLastShot(lineedit, printer=print):
    shot, ierr = da.py_lastshot()
    if ierr == 0:
        lineedit.clear()
        lineedit.insert(f"{shot}")
    else:
        printer("Error reading last shot: {ierr}")


def save_figure(scene, info):
    os.makedirs("./figs", exist_ok=True)
    exporter = ImageExporter(scene)
    exporter.parameters()["width"] = 3000
    figname = f"figs/{info.shot}__{info.array}.png"
    exporter.export(figname)


def bandpass_filter_vec(vec, flim, dt=0.001):
    if flim == (None, None):
        return vec
    fnyq = 1 / (2 * dt)
    try:
        if (flim[0] is None) or (flim[0] == 0):
            ord, wn = buttord(
                wp=flim[1], ws=1.1 * flim[1], gpass=3, gstop=20, fs=1 / dt
            )
            sos = butter(ord, wn, btype="lowpass", output="sos", fs=1 / dt)
        elif (flim[1] is None) or (flim[1] >= fnyq):
            ord, wn = buttord(
                wp=flim[0], ws=0.9 * flim[0], gpass=3, gstop=20, fs=1 / dt
            )
            sos = butter(ord, wn, btype="highpass", output="sos", fs=1 / dt)
        else:
            ord, wn = buttord(
                wp=flim, ws=[0.9 * flim[0], 1.1 * flim[1]], gpass=3, gstop=20, fs=1 / dt
            )
            sos = butter(ord, wn, btype="bandpass", output="sos", fs=1 / dt)
    except Exception as e:
        print(e)
        print("Butterworth filter error - using FFT filter")
        return bandpass_filter_fft(vec, flim, dt)
    return sosfilt(sos, vec)


def bandpass_filter_fft(vec, flim, dt=0.001):
    if None in flim:
        return vec
    ff = np.fft.fft(vec)
    fr = np.fft.fftfreq(len(vec), dt)
    mask = (np.abs(fr) <= flim[1]) & (np.abs(fr) >= flim[0])
    ff -= ff * (~mask)
    nsig = np.fft.ifft(ff, len(vec))
    return nsig.real


def get_value_from_field(field, kind):
    try:
        out = kind(field.text())
    except:
        out = None
    return out
