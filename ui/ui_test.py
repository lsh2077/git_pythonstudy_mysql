from  PyQt5 import uic

from PyQt5.QtWidgets import QWidget, QApplication


class MyApp(QWidget):
    def __init__(self):
        self.ui = uic.loadUi("test.ui")
        self.ui.btn01.clicked.connect(self.show_msg)
        self.ui.show()

    def show_msg(self):
        print("test")


if __name__=="__main__":
    app = QApplication([])
    w = MyApp()
    app.exec_()