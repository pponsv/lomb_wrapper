import numpy as np
import pyqtgraph as pg


class Linked_ROIS:
    xlim: tuple[float, float]
    ylim: tuple[float, float]
    ax_signal: pg.PlotItem
    ax_spgram: pg.PlotItem
    roi_signal: pg.LinearRegionItem
    roi_spgram: pg.RectROI
    regions: list[tuple[tuple[float, float], float]]

    def __init__(self, ax_signal: pg.PlotItem, ax_spgram: pg.PlotItem):
        self.regions = []
        self.ax_signal = ax_signal
        self.ax_spgram = ax_spgram
        #   Get initial limits
        self.resize_roi()
        #   Add ROIs
        self.add_roi_signal()
        self.add_roi_spgram()
        #   Connect signals
        self.roi_signal.sigRegionChanged.connect(self.update_spgram)
        self.roi_spgram.sigRegionChanged.connect(self.update_signal)
        self.ax_signal.sigRangeChanged.connect(self.update_signal_range)

    def resize_roi(self):
        x0, x1 = self.ax_signal.viewRange()[0]
        y0, y1 = self.ax_spgram.viewRange()[1]
        self.xlim = (x0 + (x1 - x0) / 3, x0 + 2 * (x1 - x0) / 3)
        self.ylim = (y0 + (y1 - y0) / 3, y0 + 2 * (y1 - y0) / 3)

    def add_roi_signal(self):
        self.roi_signal = pg.LinearRegionItem(values=self.xlim)
        self.roi_signal.setZValue(10)
        self.ax_signal.addItem(self.roi_signal)

    def add_roi_spgram(self):
        self.roi_spgram = pg.RectROI(
            pos=(self.xlim[0], self.ylim[0]),
            size=(self.xlim[1] - self.xlim[0], self.ylim[1] - self.ylim[0]),
            centered=False,
            sideScalers=True,
        )
        self.roi_spgram.addScaleHandle([1, 0], [0, 1])
        self.roi_spgram.addScaleHandle([0, 1], [1, 0])
        self.roi_spgram.addScaleHandle([0, 0], [1, 1])
        self.roi_spgram.addScaleHandle([0.5, 0], [0.5, 1])
        self.roi_spgram.addScaleHandle([0, 0.5], [1, 0.5])
        self.roi_spgram.setZValue(100)
        self.ax_spgram.addItem(self.roi_spgram)
        print(self.roi_spgram.pos(), self.roi_spgram.size())

    def redraw_rois(self):
        self.roi_signal.setRegion(self.xlim)
        self.roi_spgram.setPos((self.xlim[0], self.ylim[0]), finish=False)
        self.roi_spgram.setSize(
            (self.xlim[1] - self.xlim[0], self.ylim[1] - self.ylim[0]),  # type: ignore
            finish=False,
        )

    def update_signal(self):
        pos_spgram = self.roi_spgram.pos()
        size_spgram = self.roi_spgram.size()
        self.xlim = (pos_spgram[0], pos_spgram[0] + size_spgram[0])
        self.ylim = (pos_spgram[1], pos_spgram[1] + size_spgram[1])
        print("update_signal", self.xlim)
        self.redraw_rois()

    def update_spgram(self):
        self.xlim = self.roi_signal.getRegion()  # type: ignore
        print("update_spgram", self.xlim)
        self.redraw_rois()

    def update_signal_range(self):
        x0, x1 = self.ax_signal.viewRange()[0]
        y0, y1 = self.ax_spgram.viewRange()[1]
        self.xlim = (max(x0, self.xlim[0]), min(x1, self.xlim[1]))
        self.ylim = (max(y0, self.ylim[0]), min(y1, self.ylim[1]))

        self.roi_signal.setRegion(self.xlim)
        self.roi_spgram.setPos((self.xlim[0], self.ylim[0]), finish=False)
        self.roi_spgram.setSize(
            (self.xlim[1] - self.xlim[0], self.ylim[1] - self.ylim[0]),  # type: ignore
            finish=False,
        )
        print("update_signal_range", self.xlim, self.ylim)

    def add_region(self):
        self.regions.append(
            (
                self.xlim,
                min(self.ylim[0], self.ylim[1])
                + abs(self.ylim[1] - self.ylim[0]) / 2,
            )
        )
        self.ax_spgram.plot(
            [self.regions[-1][0][0], self.regions[-1][0][1]],
            [self.regions[-1][1], self.regions[-1][1]],
            pen=pg.mkPen("r", width=2),
        )

        print(self.regions[-1])

    def remove_last_region(self):
        try:
            self.regions.pop()
        except IndexError:
            return
        self.ax_spgram.removeItem(self.ax_spgram.items[-1])
