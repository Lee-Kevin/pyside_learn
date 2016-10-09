#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 设置字体和字号
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 5))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个button器件
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # sizeHint是推荐的button大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()