import webcamSeriesCapture.gui.mainwindow_auto as MW
import webcamSeriesCapture.gui.mainwindow_auto as MW

import sys
from PySide import QtGui
from PySide import QtCore
import cv2
import qimage2ndarray as qim2np
import numpy as np
from scipy import misc as spMisc
import os
import serial
import datetime as dt
import time
import sys
import skimage.io as skio
import skimage.color as skic


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


        self.cam = cv2.VideoCapture(0)
        self.timer = None
        self.ledCode = "1 0 0"

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
        self.ui.rb_yeast.toggled.connect(self.selectYeast)
        self.ui.rb_definedMedia.toggled.connect(self.selectDefinedMedia)
        self.ui.rb_noLight.toggled.connect(self.selectNoLight)
        self.ui.rb_allLight.toggled.connect(self.selectAllLight)
        self.ui.le_folder.returnPressed.connect(self.ui.pb_setFolder.clicked)
        self.ui.le_prefix.returnPressed.connect(self.ui.pb_setPrefix.clicked)
        incImgCounter = lambda: self.setImgCounter(self.imgCounter + 1)
        self.ui.pb_idxInc.clicked.connect(incImgCounter)
        decImgCounter = lambda: self.setImgCounter(self.imgCounter - 1)
        self.ui.pb_idxDec.clicked.connect(decImgCounter)



    def registerEvents(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.grabImage)
        self.timer.start(33)

    def grabImage(self):
        xSlice = slice(660, 1250)
        ySlice = slice(225, 825)
        
        ret, img = self.cam.read()
        img = np.rot90(img[ySlice, xSlice], 3)

        qi = qim2np.array2qimage(img)#[ySlice, xSlice])
        pixmap = QtGui.QPixmap()
        px = QtGui.QPixmap.fromImage(qi)

        self.ui.lbl_preview.setPixmap(px)
        self.ui.lbl_preview.setScaledContents(True)
        self.ui.lbl_preview.repaint()

        return img

    def saveImage(self):
        if not os.path.exists(os.path.split(self.path)[0]):
            os.makedirs(os.path.split(self.path)[0])

        if self.isYeast:            
            if not os.path.exists(os.path.split(self.path_raw)[0]):
                os.makedirs(os.path.split(self.path_raw)[0])
            self.saveYeastImage()
        else:
            self.saveDefinedMediaImage()

    def setImgCounter(self, cnt):
        self.imgCounter = cnt
        self.ui.le_idx.setText("{0}".format(cnt))
        filename = self.path.format(cnt=self.imgCounter, suf="_b")
        self.statusBar().showMessage("saving next image to {0}".format(filename))

    def saveDefinedMediaImage(self):
        self.setLight()
        img = self.grabImage()#np.rot90(self.cam.getImage().getNumpy(), 3)
        filename = self.path.format(cnt=self.imgCounter, suf="")
        self.setImgCounter(self.imgCounter + 1)
        spMisc.imsave(filename, img)

    def merge_images(self, img_a, img_b):
        i_a = skic.rgb2lab(img_a)
        i_b = skic.rgb2lab(img_b)
        
        norm_lum = np.min(np.asarray([i_a[..., 0], i_b[..., 0]]), axis=0)
        
        res_img = i_a.copy()
        res_img[..., 0] = norm_lum
        
        return skic.lab2rgb(res_img)


    def saveYeastImage(self):
        img_a = self.grabImage()
        filename = self.path_raw.format(cnt=self.imgCounter, suf="_a")
        skio.imsave(filename, img_a)

        self.setLight()
        img_b = self.grabImage()
        # grab a second time to make sure openCV flushed the camera buffer
        img_b = self.grabImage()
        filename = self.path_raw.format(cnt=self.imgCounter, suf="_b")
        skio.imsave(filename, img_b)

        merged_img = self.merge_images(img_a, img_b)
        filename = self.path.format(cnt=self.imgCounter, suf="")
        skio.imsave(filename, merged_img)

        self.setLight()
        self.setImgCounter(self.imgCounter + 1)

    def selectFolder(self):
        folder = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.le_folder.setText(folder)
        self.setFolder()
        self.ui.pb_acquire.setFocus()

    def setFolder(self):
        self.prefix = self.ui.le_prefix.text()
        self.folder = self.ui.le_folder.text()
        self.setPath()

    def setPrefix(self):
        self.prefix = self.ui.le_prefix.text()
        self.folder = self.ui.le_folder.text()
        self.setPath()

    def setPath(self):
        self.path = os.path.join(self.folder, self.prefix)
        self.path_raw = os.path.join(self.folder, 'raw', self.prefix)

        if not os.path.exists(self.path):
            self.setImgCounter(1)
        else:
            self.retrieveCounterFromFolder()

        self.statusBar().showMessage("Set folder path to {0}. Start counter with {1}".format(self.path, self.imgCounter))

        self.path = os.path.join(self.path, self.prefix + "-{cnt:02d}{suf}.png")
        self.path_raw = os.path.join(self.path_raw, self.prefix + "-{cnt:02d}{suf}.png")
        self.ui.pb_acquire.setFocus()


    def selectYeast(self, isYeast):
        if not isYeast:
            return

        self.isYeast = True
        self.lightLeft = True
        self.statusBar().showMessage("Yeast Mode: ON")

        self.setLight()

    def selectDefinedMedia(self, isDefinedMedia):
        if not isDefinedMedia:
            return

        self.isYeast = False
        self.ledCode = "1 0 0"
        self.statusBar().showMessage("Defined Media Mode: OFF")

        self.setLight()

    def selectNoLight(self, isNoLight):
        if not isNoLight:
            return

        self.isYeast = False
        self.ledCode = "0 0 0"
        self.statusBar().showMessage("Defined Media Mode: OFF")

        self.setLight()


    def selectAllLight(self, isAllLight):
        if not isAllLight:
            return

        self.isYeast = False
        self.ledCode = "1 1 1"
        self.statusBar().showMessage("Defined Media Mode: OFF")

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
                    self.setImgCounter(cnt + 1)


    def connectToArduino(self):
        if sys.platform == 'linux' or sys.platform == 'linux2':
            for i in range(0, 10):
                try:
                    self.ser = serial.Serial('/dev/ttyACM{0}'.format(i), timeout=1)
                except OSError:
                    continue
        elif sys.platform == 'darwin':
            for port in [x for x in os.listdir('/dev/') if 'usbmodem' in x]:
                try:
                    import serial
                    self.ser = serial.Serial('/dev/' + port, timeout=1)
                except OSError:
                    continue
        else:
            import serial.tools.list_ports
            ports = list(serial.tools.list_ports.comports())
            for port_name, device, bus in ports:
                try:
                    self.ser = serial.Serial(port_name, timeout=1)
                except serial.serialutil.SerialException:
                    continue

        if self.ser.readlines() != ['\r\n', '*EMRDY: 1\r\n']:
            # print("Connected to Arduino at port /dev/ttyACM{0}".format(i))
            self.statusBar().showMessage("Connected to Arduino") 
            self.setLight()
            self.setLight()

    def setLight(self):
        if not self.isYeast:
            self.ser.write("Led {0}\n".format(self.ledCode))
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
