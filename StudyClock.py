from unittest import skip

from PyQt5 import QtWidgets, QtCore
import sys

from PyQt5.QtCore import QPauseAnimation

from generatedUI import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # State variables
        self.remaining_time = 0
        self.timer = None
        # Connect buttons
        self.ui.StartTimer.clicked.connect(self.start_timer)
        self.ui.ResetTimer.clicked.connect(self.reset_timer)
        self.ui.PauseTimer.clicked.connect(self.pause_timer)
        self.ui.ContinueTimer.clicked.connect(self.continue_timer)
        self.ui.timeEdit.setDisplayFormat("hh:mm:ss")
        self.ui.timeEdit_2.setDisplayFormat("hh:mm:ss")
    def continue_timer(self):
        skip()

    def start_timer(self):
        self.ui.ContinueTimer.setEnabled(False)
        self.ui.AppView.setCurrentWidget(self.ui.TimerView)

        # Prevent multiple timers
        if self.timer is not None and self.timer.isActive():
            return

        total_seconds = (self.ui.timeEdit.time().hour() * 3600 +
                         self.ui.timeEdit.time().minute() * 60 +
                         self.ui.timeEdit.time().second())
        if total_seconds == 0:
            return


        self.ui.timeEdit_2.setTime(self.ui.timeEdit.time())

        self.remaining_time = total_seconds


        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            h = self.remaining_time // 3600
            m = (self.remaining_time % 3600) // 60
            s = self.remaining_time % 60
            self.ui.timeEdit_2.setTime(QtCore.QTime(h, m, s))
        else:
            self.timer.stop()
            self.timer = None
            QtWidgets.QMessageBox.information(self, "Info", "Time's up!")

    def reset_timer(self):
        if self.timer is not None:
            self.timer.stop()
            self.timer = None
        self.remaining_time = 0
        QtWidgets.QMessageBox.information(self, "Info", "Reset Timer clicked!")
    def pause_timer(self):
        if self.timer is not None:
            self.timer.stop()
            QtWidgets.QMessageBox.information(self, "Info", "Timer stopped!")
            self.ui.PauseTimer.setEnabled(False)
            self.ui.ContinueTimer.setEnabled(True)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
