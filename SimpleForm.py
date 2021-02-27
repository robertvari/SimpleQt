from PySide2.QtWidgets import QWidget, QApplication, QPushButton
import sys


class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Form")
        self.resize(200, 600)


app = QApplication(sys.argv)
win = MyForm()
win.show()
app.exec_()