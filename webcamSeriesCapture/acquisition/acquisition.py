
import  webcamSeriesCapture.gui.mainwindow_auto as MW

import sys
from PySide import QtGui
from PySide import QtCore
import SimpleCV
import qimage2ndarray as qim2np
import numpy as np
from scipy import misc as spMisc
import os
import serial
import datetime as dt
import time



class EggCountAcquisition(QtGui.QMainWindow):
    quit = QtCore.Signal()
    startLoop = QtCore.Signal()

    def __init__(self):
        """
        
        args:
            path (string):
                                root path to patches
            videoFormat (string):
                                postfix for video format *(without dot)*
        """
        QtGui.QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = MW.Ui_MainWindow()
        self.ui.setupUi(self)


        self.cam = SimpleCV.Camera(1, prop_set={"width":500,"height":600}, )
        self.timer = None

        now = dt.datetime.now()
        dateToday = "{y}{m:02d}{d:02d}".format(y=now.year, m=now.month, d=now.day)
        self.folder = "/home/peter/phd/projects/egg-count/images/" + dateToday
        self.prefix = "M"
        self.path = ""
        self.imgCounter = 0
        self.setPath()

        self.ser = None
        self.isYeast = False
        self.lightLeft = True

        self.initGUI()
        self.connectSignals()
        self.registerEvents()

        self.connectToArduino()

        self.show()


    def initGUI(self):
        self.ui.le_prefix.setText(self.prefix)
        self.ui.le_folder.setText(self.folder)

    def connectSignals(self):
        self.ui.pb_acquire.clicked.connect(self.saveImage)
        self.ui.pb_setPrefix.clicked.connect(self.setPrefix)
        self.ui.pb_setFolder.clicked.connect(self.setFolder)
        self.ui.pb_selectFolder.clicked.connect(self.selectFolder)
        self.ui.cb_yeast.stateChanged.connect(self.selectYeast)
        self.ui.le_folder.returnPressed.connect(self.ui.pb_setFolder.clicked)
        self.ui.le_prefix.returnPressed.connect(self.ui.pb_setPrefix.clicked)



    def registerEvents(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.grabImage)
        self.timer.start(33)

    def grabImage(self):
        xSlice = slice(900, 1400)
        ySlice = slice(550, 1050)

        img = np.rot90(self.cam.getImage().getNumpy(), 3)

        qi = qim2np.array2qimage(img)#[ySlice, xSlice])
        pixmap = QtGui.QPixmap()
        px = QtGui.QPixmap.fromImage(qi)

        self.ui.lbl_preview.setPixmap(px)
        self.ui.lbl_preview.setScaledContents(True)
        self.ui.lbl_preview.repaint()

        return img

    def saveImage(self):
        if self.isYeast:
            self.saveYeastImage()
        else:
            self.saveDefinedMediaImage()

    def saveDefinedMediaImage(self):
        self.setLight()
        img = self.grabImage()#np.rot90(self.cam.getImage().getNumpy(), 3)
        filename = self.path.format(cnt=self.imgCounter, suf="")
        self.imgCounter += 1
        spMisc.imsave(filename, img)
        self.statusBar().showMessage("saving to {0}".format(filename))


    def saveYeastImage(self):
        img = self.grabImage()#np.rot90(self.cam.getImage().getNumpy(), 3)
        filename = self.path.format(cnt=self.imgCounter, suf="_a")
        # self.imgCounter += 1
        spMisc.imsave(filename, img)
        self.statusBar().showMessage("saving to {0}".format(filename))

        self.setLight()
        img = self.grabImage()#np.rot90(self.cam.getImage().getNumpy(), 3)
        filename = self.path.format(cnt=self.imgCounter, suf="_b")
        self.imgCounter += 1
        spMisc.imsave(filename, img)
        self.statusBar().showMessage("saving to {0}".format(filename))

        self.setLight()

    def selectFolder(self):
        folder = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.le_folder.setText(folder)
        self.setFolder()
        self.ui.pb_acquire.setFocus()

    def setFolder(self):
        self.folder = self.ui.le_folder.text()
        self.setPath()

    def setPrefix(self):
        self.prefix = self.ui.le_prefix.text()
        self.setPath()

    def setPath(self):
        self.path = os.path.join(self.folder, self.prefix)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.retrieveCounterFromFolder()

        self.statusBar().showMessage("Set folder path to {0}. Start counter with {1}".format(self.path, self.imgCounter))

        self.path = os.path.join(self.path, self.prefix + "-{cnt:02d}{suf}.png")
        self.ui.pb_acquire.setFocus()


    def selectYeast(self, isYeast):
        self.isYeast = isYeast
        if self.isYeast:
            self.lightLeft = True
            self.statusBar().showMessage("Yeast Mode: ON")
        else:
            self.statusBar().showMessage("Yeast Mode: OFF")

        self.setLight()

    def retrieveCounterFromFolder(self):
        self.imgCounter = 0
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if not file.endswith(".png"):
                    continue

                idx = file.split(".")[0].split("-")[-1]
                if idx.endswith("a") or idx.endswith("b"):
                    idx = idx.split("_")[0]

                cnt = int(idx)
                if cnt > self.imgCounter:
                    self.imgCounter = cnt + 1


    def connectToArduino(self):
        for i in range(0, 10):
            try:
                self.ser = serial.Serial('/dev/ttyACM{0}'.format(i), timeout=1)
            except OSError:
                continue

            if self.ser.readlines() != ['\r\n', '*EMRDY: 1\r\n']:
                print("Connected to Arduino at port /dev/ttyACM{0}".format(i))
                self.statusBar().showMessage("Connected to Arduino at port /dev/ttyACM{0}".format(i))
                self.setLight()
                self.setLight()
                break

    def setLight(self):
        if not self.isYeast:
            self.ser.write("Led 1 0 0\n")
            print self.ser.readlines()

        else:
            if self.lightLeft:
                self.ser.write("Led 0 1 0\n")
                print self.ser.readlines()
            else:
                self.ser.write("Led 0 0 1\n")
                print self.ser.readlines()

            self.lightLeft = not self.lightLeft

    @QtCore.Slot()
    def cleanUp(self):
        self.ser.write("Led 0 0 0\n")
        self.ser.close()
        del self.cam





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    w = EggCountAcquisition()
    
    app.connect(app, QtCore.SIGNAL("aboutToQuit()"), w.cleanUp)
    w.quit.connect(app.quit)
    
    sys.exit(app.exec_())
