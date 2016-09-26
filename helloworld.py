# Allow access to command-line arguments
import sys

# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *

# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)

# Create a label widget with our text
#label = QLabel('Hello, world!')

# Show it as a standalone widget
#label.show()

# widget = QWidget()
# widget.setMinimumSize(QSize(800,600))
# widget.setWindowTitle('I am a Window')
# widget.show()





# Run the application's event loop
# qt_app.exec_()

class HelloWorldApp(QLabel):
    ''' A QT application that display the text, hello world '''
    def __init__(self):
        QLabel.__init__(self,"Hello World")

        self.setMinimumSize(QSize(600,300))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('test')

    def run(self):
        self.show()
        qt_app.exec_()

if __name__ == "__main__":
    HelloWorldApp().run()