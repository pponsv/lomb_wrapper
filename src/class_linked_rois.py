import numpy as np
import pyqtgraph as pg


class Linked_ROIS:
    def __init__(self, ax_signal, ax_spgram):
        self.ax_signal = ax_signal
        self.ax_spgram = ax_spgram
        self.xlim = []
        self.ylim = []
        self.add_roi_signal()
        self.add_roi_spgram()
    
    def get_lims(self):
        x0, x1 = self.ax_signal.viewRange()[0]
        y0, y1 = self.ax_spgram.viewRange()[1]
        self.xlim = [x0 + (x1-x0)/3, x0 + 2*(x1-x0)/3]
        self.ylim = [y0 + (y1-y0)/3, y0 + 2*(y1-y0)/3]


    def add_roi_signal(self):
        self.roi_signal = pg.LinearRegionItem(values=self.xlim)
        self.roi_signal.setZValue(10)
        self.ax_signal.addItem(self.roi_signal)
        # self.roi_signal.setBounds(self.xlim)
    
    def add_roi_spgram(self):
        self.roi_spgram = pg.RectROI(pos=(self.xlim[0], self.ylim[1]), 
                                     size=(self.xlim[1]-self.xlim[0], 
                                           self.ylim[1]-self.ylim[0]),)
        self.ax_spgram.addItem(self.roi_spgram)

    # def update_signal(self):
    #     pass



