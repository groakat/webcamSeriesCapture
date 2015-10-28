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
import skimage.transform as skit
import skimage.feature as skif
import skimage.draw as skid
import skimage.filters as skifilt


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
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.timer = None
        self.ledCode = "1 0 0"

        now = dt.datetime.now()
        dateToday = "{y}{m:02d}{d:02d}".format(y=now.year, m=now.month, d=now.day)
        self.folder = "/home/peter/phd/projects/egg-count/images/" + dateToday
        self.prefix = "M"
        self.path = ""
        self.imgCounter = 0

        self.ser = None
        self.isYeast = False
        self.lightLeft = True

        self.setPath()
        self.initGUI()
        self.connectSignals()

        self.connectToArduino()

        self.selectAllLight(True)
        self.ui.rb_allLight.setChecked(True)
       

        self.show()
        self.registerEvents()


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
        
        QtGui.QApplication.instance().focusChanged.connect(self.update_counter_number)



    def registerEvents(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.grabImage)
        self.timer.start(33)
        
    def update_counter_number(self, old, new):
        if old == self.ui.le_idx:
            self.setImgCounter(int(self.ui.le_idx.text()))

    def grabImage(self):
        xSlice = slice(660, 1250)
        ySlice = slice(225, 825)
        
        ret, img_org = self.cam.read()
        img = np.rot90(img_org[ySlice, xSlice], 2)

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

        if not os.path.exists(os.path.split(self.path_raw)[0]):
            os.makedirs(os.path.split(self.path_raw)[0])
                
        if self.isYeast:            
            self.saveYeastImage()
        else:
            self.saveDefinedMediaImage()

    def setImgCounter(self, cnt):
        self.imgCounter = cnt
        self.ui.le_idx.setText("{0}".format(cnt))
        filename = self.path.format(cnt=self.imgCounter, suf="_b")
        self.statusBar().showMessage("saving next image to {0}".format(filename))
        #self.setLight()

    def merge_images(self, img_a, img_b):
        i_a = skic.rgb2lab(img_a)
        i_b = skic.rgb2lab(img_b)
        
        norm_lum = np.max(np.asarray([i_a[..., 0], i_b[..., 0]]), axis=0)
        
        res_img = i_a.copy()
        res_img[..., 0] = norm_lum
        
        return skic.lab2rgb(res_img)
        
    def average_hough_detections(self, hough_radii, hough_res, num_best=5):   
        """
        Smooths `num_best` hough detections with Gaussian and 
        computes weighted average across the `num_best` hough
        detections to get more precise center_x, center_y and 
        radius of circle
        """
        
        centers = []
        accums = []
        radii = []
        
        for radius, h in zip(hough_radii, hough_res):
            # For each radius, extract two circles
            h_smooth = skifilt.gaussian_filter(h, sigma=4)
            num_peaks = 1
            peaks = skif.peak_local_max(h, min_distance=40, num_peaks=num_peaks)
            centers.extend(peaks)
            accums.extend(h[peaks[:, 0], peaks[:, 1]])
            radii.extend([radius] * num_peaks)        
            
        h_sum = np.sum([skifilt.gaussian_filter(x, sigma=2) 
                        for x in hough_res[np.argsort(accums)[::-1][:num_best]]], axis=0)
    
        peaks = skif.peak_local_max(h_sum, min_distance=40, num_peaks=num_peaks)
    
        center_x, center_y = peaks[0]
    
        max_sel = [np.max(x.ravel()) for x in hough_res[np.argsort(accums)[::-1][:num_best]]]
        radii_sel = [radii[i] for i in np.argsort(accums)[::-1][:num_best]]    
    
        radius = sum([m * r for m, r in zip(max_sel, radii_sel)]) / float(sum(max_sel)) 
        
        return center_x, center_y, int(radius)

    def blackout_outside(self, img, sigma=3):    
        img_g = skic.rgb2gray(img)
        edges = skif.canny(img_g, sigma=sigma)
        
        hough_radii = np.arange(180, 210, 2)
        hough_res = skit.hough_circle(edges, hough_radii)
        
        centers = []
        accums = []
        radii = []

        for radius, h in zip(hough_radii, hough_res):
            # For each radius, extract two circles
            num_peaks = 1
            peaks = skif.peak_local_max(h, min_distance=40, num_peaks=num_peaks)
            if peaks != []:
                centers.extend(peaks)
                accums.extend(h[peaks[:, 0], peaks[:, 1]])
                radii.extend([radius] * num_peaks)

#                print radius, np.max(h.ravel()), len(peaks)

        if accums == [] and sigma==3:
            return self.blackout_outside(img, sigma=3)
            
    #     Draw the most prominent 5 circles
        image = (img.copy() / 4.0).astype(np.uint8)
        cx, cy = skid.circle(*self.average_hough_detections(hough_radii, hough_res))
        image[cy, cx] = img[cy, cx]
        
        return image



    def saveDefinedMediaImage(self):
        self.setLight()
        img = self.grabImage()#np.rot90(self.cam.getImage().getNumpy(), 3)

        ledCode = self.ledCode
        self.ledCode = "0 0 0"
        self.setLight()

        filename = self.path_raw.format(cnt=self.imgCounter, suf="")
        spMisc.imsave(filename, img)

        filename = self.path.format(cnt=self.imgCounter, suf="")
        img = self.blackout_outside(img)
        spMisc.imsave(filename, img)        

        self.setImgCounter(self.imgCounter + 1)

        self.ledCode = ledCode
        self.setLight()

    def saveYeastImage(self):
        self.setLight()
        img_a = self.grabImage()
        # grab a second time to make sure openCV flushed the camera buffer
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

        self.ser.write("Led 1 1 1\n")
        print self.ser.readlines()
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

        self.path = os.path.join(self.path, self.prefix + "-{cnt:03d}{suf}.png")
        self.path_raw = os.path.join(self.path_raw, self.prefix + "-{cnt:03d}{suf}.png")
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
                if 'Arduino' in device:
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
        self.timer.stop()
        try:
            self.ser.write("Led 0 0 0\n")
            self.ser.close()
        except:
            print("Port already closed")
            
        try:
            del self.cam
        except AttributeError:
            print("Cam already closed")





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    w = EggCountAcquisition()
    
    app.connect(app, QtCore.SIGNAL("aboutToQuit()"), w.cleanUp)
    w.quit.connect(app.quit)
    
    sys.exit(app.exec_())
