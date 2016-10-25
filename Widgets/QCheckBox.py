#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this example, a QtGui.QCheckBox widget
is used to toggle the title of a window.

"""

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        cb2 = QtGui.QCheckBox("Hello",self)
        cb2.move(20,40)
        cb2.toggle()
        cb2.stateChanged.connect(self.hello)
        self.setGeometry(600, 300, 250, 150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')
    def hello(self,state):
        if state == QtCore.Qt.Checked:
            print("Hello Checked")
        else:
            print("Unchecked")

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()