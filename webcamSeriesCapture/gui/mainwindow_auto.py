# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jun 13 15:17:53 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 614)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_preview = QtGui.QLabel(self.centralwidget)
        self.lbl_preview.setObjectName("lbl_preview")
        self.verticalLayout.addWidget(self.lbl_preview)
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
        self.lbl_preview.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
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

