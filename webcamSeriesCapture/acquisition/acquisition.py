# import webcamSeriesCapture.gui.mainwindow_auto as MW
# import webcamSeriesCapture.gui.mainwindow_auto as MW

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

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 614)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gv_preview = QtGui.QGraphicsView(self.centralwidget)
        self.gv_preview.setObjectName("lbl_preview")
        self.verticalLayout.addWidget(self.gv_preview)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_acquire = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_acquire.sizePolicy().hasHeightForWidth())
        self.pb_acquire.setSizePolicy(sizePolicy)
        self.pb_acquire.setObjectName("pb_acquire")
        self.horizontalLayout.addWidget(self.pb_acquire)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.rb_yeast = QtGui.QRadioButton(self.groupBox_3)
        self.rb_yeast.setObjectName("rb_yeast")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.rb_yeast)
        self.rb_allLight = QtGui.QRadioButton(self.groupBox_3)
        self.rb_allLight.setObjectName("rb_allLight")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.rb_allLight)
        self.rb_definedMedia = QtGui.QRadioButton(self.groupBox_3)
        self.rb_definedMedia.setChecked(True)
        self.rb_definedMedia.setObjectName("rb_definedMedia")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.rb_definedMedia)
        self.rb_noLight = QtGui.QRadioButton(self.groupBox_3)
        self.rb_noLight.setObjectName("rb_noLight")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.rb_noLight)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_prefix = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_prefix.sizePolicy().hasHeightForWidth())
        self.le_prefix.setSizePolicy(sizePolicy)
        self.le_prefix.setObjectName("le_prefix")
        self.horizontalLayout_4.addWidget(self.le_prefix)
        self.pb_setPrefix = QtGui.QPushButton(self.groupBox_2)
        self.pb_setPrefix.setObjectName("pb_setPrefix")
        self.horizontalLayout_4.addWidget(self.pb_setPrefix)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setBaseSize(QtCore.QSize(80, 0))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_idxDec = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_idxDec.sizePolicy().hasHeightForWidth())
        self.pb_idxDec.setSizePolicy(sizePolicy)
        self.pb_idxDec.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pb_idxDec.setObjectName("pb_idxDec")
        self.horizontalLayout_5.addWidget(self.pb_idxDec)
        self.le_idx = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_idx.sizePolicy().hasHeightForWidth())
        self.le_idx.setSizePolicy(sizePolicy)
        self.le_idx.setMaximumSize(QtCore.QSize(40, 16777215))
        self.le_idx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_idx.setObjectName("le_idx")
        self.horizontalLayout_5.addWidget(self.le_idx)
        self.pb_idxInc = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_idxInc.sizePolicy().hasHeightForWidth())
        self.pb_idxInc.setSizePolicy(sizePolicy)
        self.pb_idxInc.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pb_idxInc.setObjectName("pb_idxInc")
        self.horizontalLayout_5.addWidget(self.pb_idxInc)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.le_folder = QtGui.QLineEdit(self.centralwidget)
        self.le_folder.setObjectName("le_folder")
        self.horizontalLayout_3.addWidget(self.le_folder)
        self.pb_setFolder = QtGui.QPushButton(self.centralwidget)
        self.pb_setFolder.setObjectName("pb_setFolder")
        self.horizontalLayout_3.addWidget(self.pb_setFolder)
        self.pb_selectFolder = QtGui.QPushButton(self.centralwidget)
        self.pb_selectFolder.setObjectName("pb_selectFolder")
        self.horizontalLayout_3.addWidget(self.pb_selectFolder)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_acquire.setText(QtGui.QApplication.translate("MainWindow", "acquire", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "light", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_yeast.setText(QtGui.QApplication.translate("MainWindow", "yeast", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_allLight.setText(QtGui.QApplication.translate("MainWindow", "all light", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_definedMedia.setText(QtGui.QApplication.translate("MainWindow", "defined media", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_noLight.setText(QtGui.QApplication.translate("MainWindow", "no light", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_setPrefix.setText(QtGui.QApplication.translate("MainWindow", "setPrefix", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "number", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_idxDec.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.le_idx.setText(QtGui.QApplication.translate("MainWindow", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_idxInc.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_setFolder.setText(QtGui.QApplication.translate("MainWindow", "set folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_selectFolder.setText(QtGui.QApplication.translate("MainWindow", "select folder", None, QtGui.QApplication.UnicodeUTF8))


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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mouseEventFilter = None

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
        self.circle = None
        self.bgImg = None

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
        self.configureGraphicsView()

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


    def configureGraphicsView(self):
        self.overviewScene = QtGui.QGraphicsScene(self)

        self.overviewScene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)

        self.mouseEventFilter = MouseFilterObj(self)
        self.overviewScene.installEventFilter(self.mouseEventFilter)

        self.ui.gv_preview.setScene(self.overviewScene)
        self.ui.gv_preview.setMouseTracking(True)

    def init_circle(self):
        return {"r": 80, "x": 100, "y": 100}

    def registerEvents(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.grabImage)
        self.timer.start(33)


    def update_counter_number(self, old, new):
        if old == self.ui.le_idx:
            self.setImgCounter(int(self.ui.le_idx.text()))


    def draw_circle(self, img):
        if self.circle is None:
            return img

        r = self.circle['r']
        x = self.circle['x']
        y = self.circle['y']

        rr, cc = skid.circle(y, x, r)

        ret = np.zeros_like(img)
        ret[rr, cc] = img[rr, cc]

        return ret


    def grabImage(self):
        xSlice = slice(660, 1250)
        ySlice = slice(225, 825)

        ret, img_org = self.cam.read()
        img = np.rot90(img_org[ySlice, xSlice], 2)

        if self.circle:
            try:
                qi = qim2np.array2qimage(self.draw_circle(img))
            except IndexError:
                qi = qim2np.array2qimage(img)
        else:
            qi = qim2np.array2qimage(img)


        pixmap = QtGui.QPixmap()
        px = QtGui.QPixmap.fromImage(qi)

        if self.bgImg:
            self.ui.gv_preview.scene().removeItem(self.bgImg)

        self.bgImg = QtGui.QGraphicsPixmapItem(px)
        self.ui.gv_preview.scene().addItem(self.bgImg)
        self.bgImg.setZValue(-100)
        self.bgImg.setPos(0, 0)

        self.ui.gv_preview.ensureVisible(self.bgImg)
        self.ui.gv_preview.fitInView(self.ui.gv_preview.scene().itemsBoundingRect())

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
        try:
            img = self.draw_circle(img)
        except IndexError:
            pass

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

        if self.ser is not None:
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
        if self.ser is None:
            return

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
            if self.ser is not None:
                self.ser.write("Led 0 0 0\n")
                self.ser.close()
        except:
            print("Port already closed")

        try:
            del self.cam
        except AttributeError:
            print("Cam already closed")


    def clickInScene(self, x, y):
        self.moveInScene(x, y)
        self.saveImage()


    def moveInScene(self, x, y):
        if self.circle is None:
            self.circle = self.init_circle()

        self.circle["x"] = x
        self.circle["y"] = y

    def wheelInScene(self, delta):
        if self.circle is None:
            self.circle = self.init_circle()

        self.circle['r'] += np.sign(delta)

class MouseFilterObj(QtCore.QObject):#And this one
    def __init__(self, parent):
        QtCore.QObject.__init__(self)
        self.parent = parent

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.GraphicsSceneMouseRelease:
            self.parent.clickInScene(int(event.scenePos().x()),
                                      int( event.scenePos().y()))

        if event.type() == QtCore.QEvent.GraphicsSceneMouseMove:
            self.parent.moveInScene(int(event.scenePos().x()),
                                            int( event.scenePos().y()))

        if event.type() == QtCore.QEvent.Type.GraphicsSceneWheel:
            self.parent.wheelInScene(event.delta())

        return False




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    w = EggCountAcquisition()
    
    app.connect(app, QtCore.SIGNAL("aboutToQuit()"), w.cleanUp)
    w.quit.connect(app.quit)
    
    sys.exit(app.exec_())
