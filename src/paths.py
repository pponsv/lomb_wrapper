import os

CONFIG_PATH = "/home/pedro/MEGA/00_doctorado/research/experiments/2022_spatial_periodicity_nbi_driven_ae/Analysis/DATA"

DMUSIC_PATH = lambda: f"{CONFIG_PATH}/dmusic_hdfs"
POLOIDAL_CALIBRATION_PATH = (
    lambda: f"{CONFIG_PATH}/calibration/poloidal_calibration.yaml"
)
HELICAL_CALIBRATION_PATH = (
    lambda: f"{CONFIG_PATH}/calibration/helical_calibration.yaml"
)
DATA_PATH = lambda: f"{CONFIG_PATH}/mirnov_hdfs"
LOMB_OUTPUT_PATH = lambda: f"{CONFIG_PATH}/lomb_output"
BOOZER_PATH = lambda: f"{CONFIG_PATH}/boozer/"


def set_config_folder(folder):
    global CONFIG_PATH
    CONFIG_PATH = folder
    assert os.path.isdir(
        DMUSIC_PATH()
    ), f"DMUSIC path {DMUSIC_PATH()} not found"
    assert os.path.isdir(DATA_PATH()), f"DATA path {DATA_PATH()} not found"
    assert os.path.isdir(
        LOMB_OUTPUT_PATH()
    ), f"LOMB path {LOMB_OUTPUT_PATH()} not found"
    assert os.path.isfile(
        POLOIDAL_CALIBRATION_PATH()
    ), f"Poloidal calibration file {POLOIDAL_CALIBRATION_PATH()} not found"
    assert os.path.isfile(
        HELICAL_CALIBRATION_PATH()
    ), f"Helical calibration file {HELICAL_CALIBRATION_PATH()} not found"
