# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrotecnico.ui'
#
# Created: Tue Dec 21 16:40:04 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_tecnico(object):
    def setupUi(self, tecnico):
        tecnico.setObjectName("tecnico")
        tecnico.resize(669, 418)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/technical.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tecnico.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(tecnico)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtGui.QFrame(tecnico)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btSalvar = QtGui.QPushButton(self.frame_4)
        self.btSalvar.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/button_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSalvar.setIcon(icon1)
        self.btSalvar.setFlat(True)
        self.btSalvar.setObjectName("btSalvar")
        self.horizontalLayout_4.addWidget(self.btSalvar)
        self.btCancelar = QtGui.QPushButton(self.frame_4)
        self.btCancelar.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btCancelar.setIcon(icon2)
        self.btCancelar.setFlat(True)
        self.btCancelar.setObjectName("btCancelar")
        self.horizontalLayout_4.addWidget(self.btCancelar)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame = QtGui.QFrame(tecnico)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.EditNome = QtGui.QLineEdit(self.frame)
        self.EditNome.setEnabled(True)
        self.EditNome.setObjectName("EditNome")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.EditNome)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.EditFuncao = QtGui.QLineEdit(self.frame)
        self.EditFuncao.setEnabled(True)
        self.EditFuncao.setObjectName("EditFuncao")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.EditFuncao)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.comboStatus = QtGui.QComboBox(self.frame)
        self.comboStatus.setEnabled(True)
        self.comboStatus.setObjectName("comboStatus")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboStatus)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(tecnico)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(tecnico)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabela = QtGui.QTableView(self.frame_3)
        self.tabela.setObjectName("tabela")
        self.horizontalLayout_3.addWidget(self.tabela)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(tecnico)
        QtCore.QMetaObject.connectSlotsByName(tecnico)

    def retranslateUi(self, tecnico):
        tecnico.setWindowTitle(QtGui.QApplication.translate("tecnico", "Cadastro de tecnicos", None, QtGui.QApplication.UnicodeUTF8))
        self.btSalvar.setText(QtGui.QApplication.translate("tecnico", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancelar.setText(QtGui.QApplication.translate("tecnico", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("tecnico", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("tecnico", "Função", None, QtGui.QApplication.UnicodeUTF8))
        self.comboStatus.setItemText(0, QtGui.QApplication.translate("tecnico", "Ativo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboStatus.setItemText(1, QtGui.QApplication.translate("tecnico", "Inativo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("tecnico", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("tecnico", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("tecnico", "Tecnicos Cadastrados", None, QtGui.QApplication.UnicodeUTF8))

import img_rc
