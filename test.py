# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
import sys
import os
from PySide import QtCore, QtGui
# Create a Qt application

class CameraDisplay(QtGui.QLabel):
  def __init__(self):
    super(CameraDisplay, self).__init__()

  def updateFrame(self, image):
    self.setPixmap(QtGui.QPixmap.fromImage(image))

class ControlCenter(QtGui.QWidget):
  up_camera_signal = QtCore.Signal(QtGui.QImage)
  up_camera = None

  def __init__(self):
    super(ControlCenter, self).__init__()
    self.up_camera = CameraDisplay()
    self.up_camera_signal.connect(self.up_camera.updateFrame)

    grid = QtGui.QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(self.up_camera, 0, 0)

    self.setLayout(grid)

    self.setGeometry(300, 300, 350, 300)
    self.setWindowTitle('Control Center')
    self.show()

  def up_camera_callback(self, data):
    '''This function gets called by an external thread'''
    try:
      image = QtGui.QImage(data.data, data.width, data.height, QtGui.QImage.Format_RGB888)
      self.up_camera_signal.emit(image)

    except Exception, e:
      print(e)

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  ex = ControlCenter()
  sys.exit(app.exec_())