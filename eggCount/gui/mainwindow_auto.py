# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Apr  1 18:58:32 2014
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
        self.pb_acquire.setObjectName("pb_acquire")
        self.horizontalLayout.addWidget(self.pb_acquire)
        self.cb_yeast = QtGui.QCheckBox(self.centralwidget)
        self.cb_yeast.setObjectName("cb_yeast")
        self.horizontalLayout.addWidget(self.cb_yeast)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_prefix = QtGui.QLineEdit(self.centralwidget)
        self.le_prefix.setObjectName("le_prefix")
        self.horizontalLayout_2.addWidget(self.le_prefix)
        self.pb_setPrefix = QtGui.QPushButton(self.centralwidget)
        self.pb_setPrefix.setObjectName("pb_setPrefix")
        self.horizontalLayout_2.addWidget(self.pb_setPrefix)
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
        self.cb_yeast.setText(QtGui.QApplication.translate("MainWindow", "Yeast", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_setPrefix.setText(QtGui.QApplication.translate("MainWindow", "setPrefix", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_setFolder.setText(QtGui.QApplication.translate("MainWindow", "set folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_selectFolder.setText(QtGui.QApplication.translate("MainWindow", "select folder", None, QtGui.QApplication.UnicodeUTF8))

