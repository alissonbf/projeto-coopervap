# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'licenca.ui'
#
# Created: Fri Jan  7 15:49:54 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_licenca(object):
    def setupUi(self, licenca):
        licenca.setObjectName("licenca")
        licenca.resize(619, 417)
        self.verticalLayout = QtGui.QVBoxLayout(licenca)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtGui.QTextEdit(licenca)
        self.textEdit.setEnabled(True)
        self.textEdit.setFrameShape(QtGui.QFrame.Box)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtGui.QDialogButtonBox(licenca)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(licenca)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), licenca.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), licenca.reject)
        QtCore.QMetaObject.connectSlotsByName(licenca)

    def retranslateUi(self, licenca):
        licenca.setWindowTitle(QtGui.QApplication.translate("licenca", "Licença", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("licenca", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Em termos gerais, a GPL baseia-se em 4 liberdades:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Sans\'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A liberdade de executar o programa, para qualquer propósito (liberdade nº 0)</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A liberdade de estudar como o programa funciona e adaptá-lo para as suas necessidades (liberdade nº 1). O acesso ao código-fonte é um pré-requisito para esta liberdade.</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A liberdade de redistribuir cópias de modo que você possa ajudar ao seu próximo (liberdade nº 2).</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A liberdade de aperfeiçoar o programa, e liberar os seus aperfeiçoamentos, de modo que toda a comunidade se beneficie deles (liberdade nº 3). O acesso ao código-fonte é um pré-requisito para esta liberdade.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Com a garantia destas liberdades, a GPL permite que os programas sejam distribuídos e reaproveitados, mantendo, porém, os direitos do autor por forma a não permitir que essa informação seja usada de uma maneira que limite as liberdades originais. A licença não permite, por exemplo, que o código seja apoderado por outra pessoa, ou que sejam impostos sobre ele restrições que impeçam que seja distribuído da mesma maneira que foi adquirido.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Fonte: </span><a href=\"http://pt.wikipedia.org/wiki/GNU_General_Public_License\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">Wikipedia</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\"> Visite: </span><a href=\"http://www.gnu.org/licenses/gpl.html\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">Gnu.org</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

