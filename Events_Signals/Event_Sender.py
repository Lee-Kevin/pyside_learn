#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
可以通过Sender 方法，很清楚的知道是哪一个器件出发了 event
"""

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked2)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
    def buttonClicked2(self):
        self.statusBar().showMessage("Hello world")

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()