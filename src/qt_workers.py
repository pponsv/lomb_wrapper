from PyQt6 import QtCore


class Worker(QtCore.QRunnable):
    def __init__(self, fun, *args, **kwargs):
        super(Worker, self).__init__()
        self.fun = fun
        self.args = args
        self.kwargs = kwargs
        self.signaler = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        try:
            result = self.fun(*self.args, **self.kwargs)
            self.signaler.result.emit(result)
        except Exception as e:
            self.signaler.error.emit((e,))
            print("Errored: ", e)
        finally:
            self.signaler.finished.emit()


class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
