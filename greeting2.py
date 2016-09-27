# -*- coding: gbk -*-
# -*- coding: utf-8 -*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *

qt_app = QApplication(sys.argv)

class LayoutExample(QWidget):
    ''' An example of PySide/PyQt absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''

    def __init__(self):
        # Initialize the object as a QWidget and
        # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('Dynamic Greeter')
        self.setMinimumWidth(400)

        # Create the QVBoxLayout that lays out the whole form
        # 创建垂直排列盒子层
        self.layout = QVBoxLayout()

        # Create the form layout that manages the labeled controls
        # 特殊的两栏布局，
        self.form_layout = QFormLayout()

        # The salutations that we want to make available
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']

        # Create and fill the combo box to choose the salutation
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)

        # Add it to the form layout with a label
        self.form_layout.addRow('Salutation:', self.salutation)

        # Create the entry control to specify a recipient
        # and set its placeholder text
        self.recipient = QLineEdit(self)
        self.recipient.setPlaceholderText('world' or 'Matey')

        # Add it to the form layout with a label
        self.form_layout.addRow('Recipient:', self.recipient)

        # Create and add the label to show the greeting text
        self.greeting = QLabel('', self)
        self.form_layout.addRow('Greeting:', self.greeting)

        # Add the form layout to the main VBox layout
        self.layout.addLayout(self.form_layout)

        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)

        # Create a horizontal box layout to hold the button
        self.button_box = QHBoxLayout()

        # Add stretch to push the button to the far right
        self.button_box.addStretch(1)

        # Create the build button with its caption
        self.build_button = QPushButton('Build Greeting', self)

        self.build_button.clicked.connect(self.show_greeting)
        # 设置Button的大小
        # self.build_button.setMinimumSize(QSize(200,100))

        # Add it to the button box
        self.button_box.addWidget(self.build_button)

        # Add the button box to the bottom of the main VBox layout
        self.layout.addLayout(self.button_box)

        # Set the VBox layout as the window's main layout
        self.setLayout(self.layout)

        #  全屏显示，首先得到屏幕的尺寸
        self.screen = QDesktopWidget().screenGeometry()
        # 把对话框设置为与屏幕大小一致 全屏显示
        self.setGeometry(0,0,self.screen.width(),self.screen.height())
    @Slot()
    def show_greeting(self):
        print("button pressed")
        self.greeting.setText('%s,%s!' % (self.salutations[self.salutation.currentIndex()],self.recipient.text()))
    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()

# Create an instance of the application window and run it
if __name__ == "__main__":
    app = LayoutExample()
    app.run()