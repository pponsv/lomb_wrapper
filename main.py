from PySide6.QtWidgets import QApplication
import sys  # We need sys so that we can pass argv to QApplication
from src.main_window import MainWindow
import matplotlib.pyplot as plt


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    plt.close("all")
