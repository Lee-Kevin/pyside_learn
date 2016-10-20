#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

"""

import sys
from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.vbox = QtGui.QHBoxLayout(self)
        # self.vbox.addStretch(150)
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.le)

        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
                                              'Enter your name:')

        if ok:
            self.le.setText(str(text))

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()