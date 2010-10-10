# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditos.ui'
#
# Created: Sun Oct 10 00:20:24 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_creditos(object):
    def setupUi(self, creditos):
        creditos.setObjectName("creditos")
        creditos.resize(428, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        creditos.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(creditos)
        self.buttonBox.setGeometry(QtCore.QRect(10, 270, 85, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(creditos)
        self.label.setGeometry(QtCore.QRect(0, 10, 381, 17))
        self.label.setObjectName("label")

        self.retranslateUi(creditos)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), creditos.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), creditos.reject)
        QtCore.QMetaObject.connectSlotsByName(creditos)

    def retranslateUi(self, creditos):
        creditos.setWindowTitle(QtGui.QApplication.translate("creditos", "Creditos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("creditos", "Estas pessoas fizeram o software que você esta usando", None, QtGui.QApplication.UnicodeUTF8))

import img_rc
