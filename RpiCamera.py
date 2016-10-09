import sys
import os
import time
from PySide import QtGui, QtCore


class CamSettings:
    shutter = 1000
    ISO = 100
    delay = 0
    total = 10
    timeout = 100
    quality = 100

    def __init__(self, shutter, iso, delay, total, timeout, quality):
        self.shutter = shutter
        self.iso = iso
        self.delay = delay
        self.total = total
        self.timeout = timeout
        self.quality = quality


class Timelapse:
    fn = ""
    pics = 0

    def __init__(self, fn, pics):
        self.fn = fn
        self.pics = pics


def uniqueFn(fn):
    if not os.path.exists(fn):
        return fn

    path, name = os.path.split(fn)
    name, ext = os.path.splitext(name)

    make_fn = lambda i: os.path.join(path, '%s-%d%s' % (name, i, ext))

    for i in xrange(2, sys.maxint):
        uni_fn = make_fn(i)
        if not os.path.exists(uni_fn):
            return uni_fn

    return None


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        pixmap = QtGui.QPixmap(210, 180)
        self.img = QtGui.QLabel(self)
        self.img.setPixmap(pixmap)
        self.img.move(100, 0)

        self.ST = QtGui.QLabel(self)
        self.ST.move(60, 0)
        self.ST.setText(unicode(CamSettings.shutter))
        self.ST.adjustSize()

        self.ISO = QtGui.QLabel(self)
        self.ISO.move(60, 30)
        self.ISO.setText(unicode(CamSettings.ISO))
        self.ISO.adjustSize()

        self.Dl = QtGui.QLabel(self)
        self.Dl.move(60, 60)
        self.Dl.setText(unicode(CamSettings.delay))
        self.Dl.adjustSize()

        self.TO = QtGui.QLabel(self)
        self.TO.move(60, 90)
        self.TO.setText(unicode(CamSettings.timeout))
        self.TO.adjustSize()

        self.Tl = QtGui.QLabel(self)
        self.Tl.move(60, 120)
        self.Tl.setText(unicode(CamSettings.total))
        self.Tl.adjustSize()

        self.Q = QtGui.QLabel(self)
        self.Q.move(60, 150)
        self.Q.setText(unicode(CamSettings.quality))
        self.Q.adjustSize()

        btnSTu = QtGui.QPushButton("+", self)
        btnSTu.resize(30, 30)
        btnSTu.move(0, 0)
        btnSTu.clicked.connect(self.ShutterLonger)
        btnSTu.setToolTip('Shutter Time (ns)')

        btnSTd = QtGui.QPushButton("-", self)
        btnSTd.resize(30, 30)
        btnSTd.move(30, 0)
        btnSTd.clicked.connect(self.ShutterShorter)
        btnSTd.setToolTip('Shutter Time (ns)')

        btnISOu = QtGui.QPushButton("+", self)
        btnISOu.resize(30, 30)
        btnISOu.move(0, 30)
        btnISOu.clicked.connect(self.ISOup)
        btnISOu.setToolTip('ISO')

        btnISOd = QtGui.QPushButton("-", self)
        btnISOd.resize(30, 30)
        btnISOd.move(30, 30)
        btnISOd.clicked.connect(self.ISOdown)
        btnISOd.setToolTip('ISO')

        btnDlu = QtGui.QPushButton("+", self)
        btnDlu.resize(30, 30)
        btnDlu.move(0, 60)
        btnDlu.clicked.connect(self.Dlup)
        btnDlu.setToolTip('delay after pic (ms)')

        btnDld = QtGui.QPushButton("-", self)
        btnDld.resize(30, 30)
        btnDld.move(30, 60)
        btnDld.clicked.connect(self.Dldown)
        btnDld.setToolTip('delay after pic (s)')

        btnTOu = QtGui.QPushButton("+", self)
        btnTOu.resize(30, 30)
        btnTOu.move(0, 90)
        btnTOu.clicked.connect(self.TOup)
        btnTOu.setToolTip('timeout (time delay before pic, ms)')

        btnTOd = QtGui.QPushButton("-", self)
        btnTOd.resize(30, 30)
        btnTOd.move(30, 90)
        btnTOd.clicked.connect(self.TOdown)
        btnTOd.setToolTip('timeout (time delay before pic, ms)')

        btnTlu = QtGui.QPushButton("+", self)
        btnTlu.resize(30, 30)
        btnTlu.move(0, 120)
        btnTlu.clicked.connect(self.Tlup)
        btnTlu.setToolTip('total # of pics')

        btnTlu = QtGui.QPushButton("-", self)
        btnTlu.resize(30, 30)
        btnTlu.move(30, 120)
        btnTlu.clicked.connect(self.Tldown)
        btnTlu.setToolTip('total # of pics')

        btnQu = QtGui.QPushButton("+", self)
        btnQu.resize(30, 30)
        btnQu.move(0, 150)
        btnQu.clicked.connect(self.Qup)
        btnQu.setToolTip('quality')

        btnQu = QtGui.QPushButton("-", self)
        btnQu.resize(30, 30)
        btnQu.move(30, 150)
        btnQu.clicked.connect(self.Qdown)
        btnQu.setToolTip('quality')

        btnStart = QtGui.QPushButton('>', self)
        btnStart.setToolTip('Start')
        btnStart.resize(30, 30)
        btnStart.move(0, 180)
        btnStart.clicked.connect(self.StartCamera)

        self.mult = 1

        self.btnMult = QtGui.QPushButton(str(self.mult), self)
        self.btnMult.setToolTip('Multiplier')
        self.btnMult.resize(30, 30)
        self.btnMult.move(30, 180)
        self.btnMult.clicked.connect(self.toggleMult)

        self.setGeometry(0, 0, 320, 210)
        self.setWindowTitle('PiCameraControl')
        self.show()

    def toggleMult(self):
        self.mult = self.mult * 10
        if self.mult > 1000000:
            self.mult = 1
        self.btnMult.setText(str(self.mult))
        if self.mult > 1000:
            self.btnMult.resize(60, 30)
        else:
            self.btnMult.resize(30, 30)

    def ShutterLonger(self):
        CamSettings.shutter = CamSettings.shutter + self.mult

        self.ST.setText(unicode(CamSettings.shutter))
        self.ST.adjustSize()

    def ShutterShorter(self):
        CamSettings.shutter = CamSettings.shutter - self.mult
        if (CamSettings.shutter < 1000):
            CamSettings.shutter = 1000

        self.ST.setText(unicode(CamSettings.shutter))
        self.ST.adjustSize()

    def ISOup(self):
        CamSettings.ISO = CamSettings.ISO + self.mult

        self.ISO.setText(unicode(CamSettings.ISO))
        self.ISO.adjustSize()

    def ISOdown(self):
        CamSettings.ISO = CamSettings.ISO - self.mult
        if (CamSettings.ISO < 100):
            CamSettings.ISO = 100

        self.ISO.setText(unicode(CamSettings.ISO))
        self.ISO.adjustSize()

    def Dlup(self):
        CamSettings.delay = CamSettings.delay + self.mult

        self.Dl.setText(unicode(CamSettings.delay))
        self.Dl.adjustSize()

    def Dldown(self):
        CamSettings.delay = CamSettings.delay - self.mult
        if (CamSettings.delay < 0):
            CamSettings.delay = 0

        self.Dl.setText(unicode(CamSettings.delay))
        self.Dl.adjustSize()

    def TOup(self):
        CamSettings.timeout = CamSettings.timeout + self.mult

        self.TO.setText(unicode(CamSettings.timeout))
        self.TO.adjustSize()

    def TOdown(self):
        CamSettings.timeout = CamSettings.timeout - self.mult
        if (CamSettings.timeout < 100):
            CamSettings.timeout = 100

        self.TO.setText(unicode(CamSettings.timeout))
        self.TO.adjustSize()

    def Tlup(self):
        CamSettings.total = CamSettings.total + self.mult

        self.Tl.setText(unicode(CamSettings.total))
        self.Tl.adjustSize()

    def Tldown(self):
        CamSettings.total = CamSettings.total - self.mult
        if (CamSettings.total < 1):
            CamSettings.total = 1

        self.Tl.setText(unicode(CamSettings.total))
        self.Tl.adjustSize()

    def Qup(self):
        CamSettings.quality = CamSettings.quality + self.mult
        if (CamSettings.quality > 100):
            CamSettings.quality = 100
        self.Q.setText(unicode(CamSettings.quality))
        self.Q.adjustSize()

    def Qdown(self):
        CamSettings.quality = CamSettings.quality - self.mult
        if (CamSettings.quality < 10):
            CamSettings.quality = 10

        self.Q.setText(unicode(CamSettings.quality))
        self.Q.adjustSize()

    def StartCamera(self):
        fn = "Timelapse"
        fn = uniqueFn(fn)
        command = str("mkdir ") + str(fn)
        f = os.popen(command)
        now = f.read()
        print now
        currentTL = Timelapse(fn, 0)

        count = 1
        while (count < CamSettings.total + 1):
            pfn = currentTL.fn + '/ss-' + str(CamSettings.shutter) + 'ISO-' + str(CamSettings.ISO) + 'TO-' + str(
                CamSettings.timeout) + 'Q-' + str(CamSettings.quality) + '.jpg'
            pfn = uniqueFn(pfn)
            command = 'raspistill -o {} -ss {} -ISO {} -t {} -q {} -n -th none -hf -vf -awb auto'.format(pfn,
                                                                                                         CamSettings.shutter,
                                                                                                         CamSettings.ISO,
                                                                                                         CamSettings.timeout,
                                                                                                         CamSettings.quality)
            f = os.popen(command)
            now = f.read()
            print now
            print command

            pm = QtGui.QPixmap(pfn)
            pm = pm.scaled(210, 180, aspectRatioMode=QtCore.Qt.KeepAspectRatio)
            self.img.setPixmap(pm)
            self.img.adjustSize

            count = count + 1
            currentTL.pics = currentTL.pics + 1
            time.sleep(CamSettings.delay)


def main():
    st = CamSettings(1000, 100, 0, 3, 500, 100)
    app = QtGui.QApplication(sys.argv)

    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()