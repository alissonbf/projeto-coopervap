# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobre.ui'
#
# Created: Sun Oct 10 23:42:10 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SobreDialog(object):
    def setupUi(self, SobreDialog):
        SobreDialog.setObjectName("SobreDialog")
        SobreDialog.resize(482, 359)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SobreDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SobreDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(SobreDialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/images/logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(SobreDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_3 = QtGui.QLabel(SobreDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(SobreDialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(SobreDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.creditos = QtGui.QPushButton(SobreDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/licenca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.creditos.setIcon(icon1)
        self.creditos.setObjectName("creditos")
        self.horizontalLayout.addWidget(self.creditos)
        self.Licenca = QtGui.QPushButton(SobreDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/gnu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Licenca.setIcon(icon2)
        self.Licenca.setObjectName("Licenca")
        self.horizontalLayout.addWidget(self.Licenca)
        self.tilivre = QtGui.QPushButton(SobreDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/images/mascote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tilivre.setIcon(icon3)
        self.tilivre.setIconSize(QtCore.QSize(16, 16))
        self.tilivre.setObjectName("tilivre")
        self.horizontalLayout.addWidget(self.tilivre)
        self.fechar = QtGui.QPushButton(SobreDialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/images/fechar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fechar.setIcon(icon4)
        self.fechar.setObjectName("fechar")
        self.horizontalLayout.addWidget(self.fechar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(SobreDialog)
        QtCore.QObject.connect(self.fechar, QtCore.SIGNAL("clicked()"), SobreDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SobreDialog)

    def retranslateUi(self, SobreDialog):
        SobreDialog.setWindowTitle(QtGui.QApplication.translate("SobreDialog", "Sobre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SobreDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Easy Estoque</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SobreDialog", "Este software foi feito para realizar o controle de peças de informatica.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SobreDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E esta sobre a licença:</p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">GNU/GPL</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SobreDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mantenedora:</p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><h2>Ti Livre</h2> </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.creditos.setText(QtGui.QApplication.translate("SobreDialog", "Créditos", None, QtGui.QApplication.UnicodeUTF8))
        self.Licenca.setText(QtGui.QApplication.translate("SobreDialog", "Licença", None, QtGui.QApplication.UnicodeUTF8))
        self.tilivre.setText(QtGui.QApplication.translate("SobreDialog", "Ti Livre", None, QtGui.QApplication.UnicodeUTF8))
        self.fechar.setText(QtGui.QApplication.translate("SobreDialog", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

import img_rc
