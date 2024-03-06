import numpy as np
from .TJII_data_acquisition_f import tjii_data_acquisition as tf
import datetime


def py_lastshot():
    lshot, ierr = tf.f_lastshot()
    return lshot, ierr


def py_sigtype(sig: str):
    tipo, ierr = tf.f_sigtype(sig)
    return tipo, ierr


def py_lectur(shot: int, sig: str):
    ndat, nvent, ierr = py_dimens(shot, sig)
    x, y, ierr = tf.f_lectur(shot, sig, ndat, nvent)
    return x.astype(np.float64), y.astype(np.float64), ierr


def py_lectc(shot: int, sig: str):
    ndat, nvent, ierr = tf.f_dimens(shot, sig)
    x, y, ierr = tf.f_lectc(shot, sig, ndat, nvent)
    return x.astype(np.float64), y.astype(np.int64), ierr


def py_dimens(shot: int, sig: str):
    ndat, nvent, ierr = tf.f_dimens(shot, sig)
    return ndat, nvent, ierr


def py_dimenp(shot: int, sig: str):
    nper, npunt, ierr = tf.f_dimenp(shot, sig)
    return nper, npunt, ierr


def py_leep(shot: int, sig: str):
    nper, npunt, ierr = py_dimenp(shot, sig)
    t, r, y, ierr = tf.f_leep(shot, sig, nper, npunt)
    return t.astype(np.float64).T, r.astype(np.float64).T, y.astype(np.float64).T, ierr


def py_ertxt(ierr: int):
    tf.f_ertxt(ierr)


def py_fecha(shot: int):
    tfecha, ierr = tf.f_fecha(shot)
    fecha = datetime.datetime(*tfecha)
    return fecha, ierr


def py_getq(shot: int, signal: str):
    idx, ierr = tf.f_getq(shot, signal)
    keys = {
        0: "Sin clasificar",
        1: "Datos validados",
        2: "No usar",
        3: "Usar con reservas",
    }
    return idx, keys, ierr


def py_nums(shot: int):
    ns, ierr = tf.f_nums(shot)
    return ns, ierr


def py_listas(shot: int):
    ns, ierr = tf.f_nums(shot)
    if ierr == 0:
        lista, ierr = tf.f_listas(shot, ns)
        return _dcd(lista), ierr
    return ierr


def py_numshots(fecha: datetime.datetime):
    year = fecha.year
    month = fecha.month
    day = fecha.day
    nshots, ierr = tf.f_numshots(year, month, day)
    return nshots, ierr


def py_paramn(shot: int, sig: str):
    np, ierr = tf.f_paramn(shot, sig)
    return np, ierr


def py_params(shot: int, sig: str):
    np, ierr = py_paramn(shot, sig)
    params, vals, ierr = tf.f_params(shot, sig, np)
    return _dcd(params), vals, ierr


def py_shotlist(fecha: datetime.datetime):
    year = fecha.year
    month = fecha.month
    day = fecha.day
    nshots, ierr = py_numshots(fecha)
    shots, ierr = tf.f_shotlist(year, month, day, nshots)
    return shots, ierr


def _dcd(lista):
    # ~ lista = np.asarray(lista).flatten()
    # return [''.join([a.decode('UTF-8') for a in i]) for i in lista]
    return [a.decode("UTF-8") for a in lista]
