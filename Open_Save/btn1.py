from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
import sys
import os


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("btn_sv.ui", self)
        self.btn_open.clicked.connect(self.add_file)
        self.btn_save.clicked.connect(self.save_file)

    def add_file(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Путь к файлу")
        if self.filename:
            self.textEdit.setText(self.filename)

    def save_file(self):
        self.filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", ".", "Text Files (*.txt);;All Files(*)")

        if self.filename:
            with open(self.filename, 'w') as file:
                file.write("Welcome Home, Son ")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
