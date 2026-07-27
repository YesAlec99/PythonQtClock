from PyQt5 import QtWidgets
import sys
from generatedUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # create the ui object
        self.ui.setupUi(self)  # apply it to this window

        # Connect buttons
        self.ui.StartTimer.clicked.connect(self.start_timer)
        self.ui.ResetTimer.clicked.connect(self.reset_timer)

    def start_timer(self):
        print("Start Timer clicked!")

    def reset_timer(self):
        QtWidgets.QMessageBox.information(self, "Info", "Reset Timer clicked!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
