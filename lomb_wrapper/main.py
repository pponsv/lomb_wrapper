import sys  # We need sys so that we can pass argv to QApplication

import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication

from .main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    plt.close("all")
