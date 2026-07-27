from PyQt5 import QtWidgets
import sys
from generatedUI import Ui_MainWindow

timer_id = None
remaining_time = 0
current_session = None


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # create the ui object
        self.ui.setupUi(self)  # apply it to this window

        # Connect buttons
        self.ui.StartTimer.clicked.connect(self.start_timer)
        self.ui.ResetTimer.clicked.connect(self.reset_timer)
        self.ui.timeEdit.setDisplayFormat("hh:mm:ss")
        self.ui.timeEdit_2.setDisplayFormat("hh:mm:ss")

    def start_timer(self):
        self.ui.AppView.setCurrentWidget(self.ui.TimerView)
        global remaining_time, current_session, timer_id
        if timer_id is not None:
            return
        total_seconds = (self.ui.timeEdit.time().hour() * 3600 +
                         self.ui.timeEdit.time().minute() * 60 +
                         self.ui.timeEdit.time().second())
        if total_seconds == 0:
            return
        self.ui.timeEdit_2.setTime(self.ui.timeEdit.time())
        remaining_time = total_seconds

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            # Update timeEdit_2 display
            h = self.remaining_time // 3600
            m = (self.remaining_time % 3600) // 60
            s = self.remaining_time % 60
            self.ui.timeEdit_2.setTime(QtCore.QTime(h, m, s))
        else:
            self.timer.stop()
            self.timer_id = None
            QtWidgets.QMessageBox.information(self, "Info", "Time's up!")

    def reset_timer(self):
        QtWidgets.QMessageBox.information(self, "Info", "Reset Timer clicked!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
