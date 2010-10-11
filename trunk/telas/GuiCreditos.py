# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditos.ui'
#
# Created: Sun Oct 10 22:48:08 2010
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
        self.verticalLayout = QtGui.QVBoxLayout(creditos)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(creditos)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtGui.QDialogButtonBox(creditos)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(creditos)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), creditos.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), creditos.reject)
        QtCore.QMetaObject.connectSlotsByName(creditos)

    def retranslateUi(self, creditos):
        creditos.setWindowTitle(QtGui.QApplication.translate("creditos", "Créditos", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("creditos", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alisson Barbosa Ferreira, &lt;alissonbf@gmail.com&gt;                   </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alisson Oliveira Ferreira, &lt;linukiss@gmail.com&gt;    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Erick Oliveira, &lt;re.erick86@gmail.com&gt;              </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Victor Hugo Neiva, &lt;victorhugoneiva@gmail.com&gt;                          </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wesley Junior, &lt;www.wesley@gmail.com&gt;  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Willian Soares Damasceno, &lt;wilhiaods@gmail.com&gt;</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import img_rc
