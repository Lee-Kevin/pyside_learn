#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this example, we select a file with a
QtGui.QFileDialog and display its contents
in a QtGui.QTextEdit.

"""

import sys
from PySide import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                  '/home')
        self.textEdit.setText("Hello World")
        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(str(data))
            self.textEdit.setText("Hello World")

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()