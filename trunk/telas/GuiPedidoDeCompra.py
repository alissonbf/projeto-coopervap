# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pedidodecompra.ui'
#
# Created: Thu Dec 30 22:28:43 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_pedidodecompra(object):
    def setupUi(self, pedidodecompra):
        pedidodecompra.setObjectName("pedidodecompra")
        pedidodecompra.resize(769, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/pedidodecompra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pedidodecompra.setWindowIcon(icon)
        self.verticalLayout_4 = QtGui.QVBoxLayout(pedidodecompra)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtGui.QTabWidget(pedidodecompra)
        self.tabWidget.setMinimumSize(QtCore.QSize(751, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolBox = QtGui.QToolBox(self.tab)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 729, 418))
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtGui.QFrame(self.page)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btSalvarPedido = QtGui.QPushButton(self.frame_4)
        self.btSalvarPedido.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/button_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSalvarPedido.setIcon(icon1)
        self.btSalvarPedido.setFlat(True)
        self.btSalvarPedido.setObjectName("btSalvarPedido")
        self.horizontalLayout_4.addWidget(self.btSalvarPedido)
        self.btCancelarPedido = QtGui.QPushButton(self.frame_4)
        self.btCancelarPedido.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btCancelarPedido.setIcon(icon2)
        self.btCancelarPedido.setFlat(True)
        self.btCancelarPedido.setObjectName("btCancelarPedido")
        self.horizontalLayout_4.addWidget(self.btCancelarPedido)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame = QtGui.QFrame(self.page)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.EditPedido = QtGui.QLineEdit(self.frame)
        self.EditPedido.setObjectName("EditPedido")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.EditPedido)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.EditData = QtGui.QLineEdit(self.frame)
        self.EditData.setObjectName("EditData")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.EditData)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboResponsavel = QtGui.QComboBox(self.frame)
        self.comboResponsavel.setObjectName("comboResponsavel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboResponsavel)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboStatus = QtGui.QComboBox(self.frame)
        self.comboStatus.setObjectName("comboStatus")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboStatus)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_6 = QtGui.QFrame(self.page)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtGui.QLabel(self.frame_6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_3 = QtGui.QFrame(self.page)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabela = QtGui.QTableView(self.frame_3)
        self.tabela.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela.setTabKeyNavigation(False)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabela.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabela.setSortingEnabled(True)
        self.tabela.setObjectName("tabela")
        self.tabela.horizontalHeader().setSortIndicatorShown(True)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.tabela)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.toolBox.addItem(self.page, "")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtGui.QFrame(self.page_3)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btSalvarEquipamento = QtGui.QPushButton(self.frame_5)
        self.btSalvarEquipamento.setEnabled(True)
        self.btSalvarEquipamento.setIcon(icon1)
        self.btSalvarEquipamento.setFlat(True)
        self.btSalvarEquipamento.setObjectName("btSalvarEquipamento")
        self.horizontalLayout_5.addWidget(self.btSalvarEquipamento)
        self.btCancelarEquipamento = QtGui.QPushButton(self.frame_5)
        self.btCancelarEquipamento.setEnabled(True)
        self.btCancelarEquipamento.setIcon(icon2)
        self.btCancelarEquipamento.setFlat(True)
        self.btCancelarEquipamento.setObjectName("btCancelarEquipamento")
        self.horizontalLayout_5.addWidget(self.btCancelarEquipamento)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_2 = QtGui.QFrame(self.page_3)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBox_3 = QtGui.QComboBox(self.frame_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_3)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout_3)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.formLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.frame_8 = QtGui.QFrame(self.page_3)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtGui.QLabel(self.frame_8)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_7 = QtGui.QFrame(self.page_3)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabela_2 = QtGui.QTableView(self.frame_7)
        self.tabela_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_2.setTabKeyNavigation(False)
        self.tabela_2.setAlternatingRowColors(True)
        self.tabela_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabela_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabela_2.setSortingEnabled(True)
        self.tabela_2.setObjectName("tabela_2")
        self.tabela_2.horizontalHeader().setSortIndicatorShown(True)
        self.tabela_2.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_7.addWidget(self.tabela_2)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout_2.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_11 = QtGui.QFrame(self.tab_3)
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_15 = QtGui.QLabel(self.frame_11)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_12 = QtGui.QLabel(self.frame_11)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_12)
        self.EditData_2 = QtGui.QLineEdit(self.frame_11)
        self.EditData_2.setObjectName("EditData_2")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.EditData_2)
        self.horizontalLayout_11.addLayout(self.formLayout_4)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_13 = QtGui.QLabel(self.frame_11)
        self.label_13.setObjectName("label_13")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.comboResponsavel_2 = QtGui.QComboBox(self.frame_11)
        self.comboResponsavel_2.setObjectName("comboResponsavel_2")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboResponsavel_2)
        self.label_14 = QtGui.QLabel(self.frame_11)
        self.label_14.setObjectName("label_14")
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.comboStatus_2 = QtGui.QComboBox(self.frame_11)
        self.comboStatus_2.setObjectName("comboStatus_2")
        self.comboStatus_2.addItem("")
        self.comboStatus_2.addItem("")
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboStatus_2)
        self.horizontalLayout_11.addLayout(self.formLayout_6)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_10 = QtGui.QFrame(self.tab_3)
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtGui.QLabel(self.frame_10)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_9 = QtGui.QFrame(self.tab_3)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabela_3 = QtGui.QTableView(self.frame_9)
        self.tabela_3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_3.setTabKeyNavigation(False)
        self.tabela_3.setAlternatingRowColors(True)
        self.tabela_3.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabela_3.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabela_3.setSortingEnabled(True)
        self.tabela_3.setObjectName("tabela_3")
        self.tabela_3.horizontalHeader().setSortIndicatorShown(True)
        self.tabela_3.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_9.addWidget(self.tabela_3)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(pedidodecompra)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pedidodecompra)

    def retranslateUi(self, pedidodecompra):
        pedidodecompra.setWindowTitle(QtGui.QApplication.translate("pedidodecompra", "Pedidos de Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.btSalvarPedido.setText(QtGui.QApplication.translate("pedidodecompra", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancelarPedido.setText(QtGui.QApplication.translate("pedidodecompra", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("pedidodecompra", "Nº Pedido de compra", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("pedidodecompra", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("pedidodecompra", "Responsavel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("pedidodecompra", "Status do pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.comboStatus.setItemText(0, QtGui.QApplication.translate("pedidodecompra", "Em andamento", None, QtGui.QApplication.UnicodeUTF8))
        self.comboStatus.setItemText(1, QtGui.QApplication.translate("pedidodecompra", "Finalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("pedidodecompra", "Pedidos Cadastrados", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("pedidodecompra", "Dados do pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.btSalvarEquipamento.setText(QtGui.QApplication.translate("pedidodecompra", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancelarEquipamento.setText(QtGui.QApplication.translate("pedidodecompra", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("pedidodecompra", "Pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("pedidodecompra", "Nome do equipamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("pedidodecompra", "Unidade", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("pedidodecompra", "entregar até", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("pedidodecompra", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("pedidodecompra", "Equipamentos dos pedidos cadastrados", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("pedidodecompra", "Equipamentos do pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("pedidodecompra", "Cadastrar pedido de compra", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("pedidodecompra", "Nome do equipamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("pedidodecompra", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("pedidodecompra", "Responsavel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("pedidodecompra", "Status do pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.comboStatus_2.setItemText(0, QtGui.QApplication.translate("pedidodecompra", "Em andamento", None, QtGui.QApplication.UnicodeUTF8))
        self.comboStatus_2.setItemText(1, QtGui.QApplication.translate("pedidodecompra", "Finalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("pedidodecompra", "Resultado", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("pedidodecompra", "Buscar pedidos de compra", None, QtGui.QApplication.UnicodeUTF8))

import img_rc