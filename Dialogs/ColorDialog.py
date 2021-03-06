#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this example, we select a colour value
from the QtGui.QColorDialog and change the background
colour of a QtGui.QFrame widget.
"""

import sys
from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        col = QtGui.QColor(0, 0, 0)

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(80, 22, 200, 200)

        self.setGeometry(300, 300, 400, 280)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())
            print(col.name())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()