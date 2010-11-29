#!/bin/env python                         
# -*- coding: utf-8 -*-             

## [Ficha]##################################################
#	                                                   #					           
#  Nome: Modulo View				           #
#                                                          #
#  Escrito por: Alisson Barbosa Ferreira                   #
#               Alisson Oliveira Ferreira                  #
#               Victor Hugo Neiva                          #
#               Wesley Junior                              #
#                                                          #
#  Criado em: 30/08/2010			           #
#						           #
#  Ultima atualizacao: 24/11/2010		           #
#						           #
#  [Descricao]##############################################
#					                   #
#  Este script contem as classes que se comunicam com      #
#  as interfaces graficas e da vida aos seus botões        #
#					                   #
############################################################

import sys
import re
import webbrowser

from PyQt4.QtCore import *                 
from PyQt4.QtGui import *         

from telas.GuiPrincipal import *

from telas.GuiCadastroUsuario import *
from telas.GuiCadastroEquipamento import *

from telas.GuiSobre import *
from telas.GuiLicenca import *
from telas.GuiCreditos import *


from Controller import *
from Model import *


#-& CLASSE &-#
class Principal(QMainWindow, Ui_principal):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        
        abrirBancoDeDados(self)
        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")

        # Cria a area onde as sub-janelas serão abertas
        self.MdiArea = QMdiArea(self)
        


    def __done__(self):
        fecharBancoDeDados(self.bancoDeDados)

    # Mostra janela para manutenção de usuarios, paramentro obj é a janela a ser aberta
    def mostrarSubwindow(self, obj):
        window = obj               
        SubWindow = QMdiSubWindow()
        SubWindow.setWidget(window)        
        SubWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.MdiArea.addSubWindow(SubWindow)
        SubWindow.show()

    # Verifica se o usuario existe no banco
    def is_exist(self):
        user=self.EditUser.text()
        senha=self.EditSenha.text()
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT COUNT(*) FROM usuario WHERE login=? and senha=? and status=?")
        query.addBindValue(user)
        query.addBindValue(senha)
        query.addBindValue("Ativo")
        query.exec_()
        while (query.next()):
            var = query.value(0).toInt()
            if var[0] == 1:
                return True
            else:
                return False 


    @pyqtSignature("")
    def on_btEntrar_clicked(self):
        if self.is_exist():
            self.setCentralWidget(self.MdiArea)
            self.menubar.setEnabled(True)
            self.toolBar.setEnabled(True)
            self.showMaximized()
        else:
            msg = QMessageBox.warning(self, QString.fromUtf8("Falha na autenticação"),QString.fromUtf8("Este usuário não existe ou foi desativado!"), QMessageBox.Close)
 
    
    @pyqtSignature("")
    def on_actionCadastrar_Usuarios_triggered(self):          
        cadusu = CadastroUsuario()
        self.mostrarSubwindow(cadusu)

    @pyqtSignature("")
    def on_actionCadastrar_Equipamentos_triggered(self):          
        cadequp = CadastroEquipamento()
        self.mostrarSubwindow(cadequp)

    @pyqtSignature("")
    def on_actionDocumenta_o_triggered(self):          
        webbrowser.open('docs/Manual desenvolvedor/_build/html/index.html')

    @pyqtSignature("")
    def on_actionAjuda_Programa_triggered(self):          
        webbrowser.open('docs/manual do usuario/_build/html/index.html')

    @pyqtSignature("")
    def on_actionSobre_triggered(self):          
        sobre = Sobre()
        sobre.exec_()

    @pyqtSignature("")
    def on_actionSair_triggered(self):          
        quit()





#-& CLASSE &-#
class Sobre(QDialog, Ui_SobreDialog):
    def __init__(self, parent=None):
        super(Sobre, self).__init__(parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_creditos_clicked(self):          
        creditos = Creditos()
        creditos.exec_()

    @pyqtSignature("")
    def on_Licenca_clicked(self):
        licenca = Licenca()
        licenca.exec_()

    @pyqtSignature("")
    def on_tilivre_clicked(self):
        webbrowser.open('http://www.tilivre.net.br')


#-& CLASSE &-#
class Creditos(QDialog, Ui_creditos):
    def __init__(self, parent=None):
        super(Creditos, self).__init__(parent)
        self.setupUi(self)


#-& CLASSE &-#
class Licenca(QDialog, Ui_licenca):
    def __init__(self, parent=None):
        super(Licenca, self).__init__(parent)
        self.setupUi(self)


#-& CLASSE &-#
class CadastroUsuario(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(CadastroUsuario, self).__init__(parent)
        self.setupUi(self)

        self.setIncluindo(False)
        self.setEditando(False)
        self.incluindoUsuario = False        
        self.editandoUsuario = False

        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")  
        self.usuarioModel = QSqlTableModel(self, self.bancoDeDados)
        self.abrirTabelaUsuario()

        self.mapeador = QDataWidgetMapper()
        self.mapeador.setModel(self.usuarioModel)
        self.mapeador.addMapping(self.EditID, 0)
        self.mapeador.addMapping(self.EditNome, 1)
        self.mapeador.addMapping(self.EditEmail, 2)
        self.mapeador.addMapping(self.EditFuncao, 3)
        self.mapeador.addMapping(self.ComboStatus, 4)
        self.mapeador.addMapping(self.EditLogin, 5)
        self.mapeador.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)       
        

        self.connect(self.tabela.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeador, SLOT("setCurrentModelIndex(QModelIndex)"))      
         

    def __done__(self):
        QSqlDatabase.removeDatabase("coopervap-bd")
        


    # Preence a tabela com os dados que estão no banco de dados
    def abrirTabelaUsuario(self):        
        consulta = "SELECT id_usuario,nome,email,funcao,status,login FROM usuario ORDER BY id_usuario"     
        self.usuarioModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.usuarioModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.usuarioModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.usuarioModel.setHeaderData(2, Qt.Horizontal, "Email")
        self.usuarioModel.setHeaderData(3, Qt.Horizontal, QString.fromUtf8("Função"))
        self.usuarioModel.setHeaderData(4, Qt.Horizontal, "Status")
        self.usuarioModel.setHeaderData(5, Qt.Horizontal, "Login")
        self.usuarioModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        self.tabela.setModel(self.usuarioModel)         
    
    # Ativa o botão de salvar e  cancelar, se o status for True
    def setIncluindo(self,status):
        self.incluindoUsuario = status
        self.Salvar.setEnabled(self.incluindoUsuario)
        if (self.incluindoUsuario):
            self.Deletar.setEnabled(self.incluindoUsuario)
        else:
            self.Deletar.setEnabled(self.incluindoUsuario)
    

    # Ativa o botão de salvar e cancelar, se o status for True
    def setEditando(self,status):
        self.editandoUsuario = status
        self.Salvar.setEnabled(self.editandoUsuario)
        if (self.editandoUsuario):
            self.Deletar.setEnabled(self.editandoUsuario)
        else:
           self.Deletar.setEnabled(self.editandoUsuario)

    # Valida os dados, digitados pelo usuario
    def valido(self):
        if(self.EditID.text()!=""):
            id_usu = int(self.EditID.text())
            senha = "##########"
            senha_confirme = "##########"
        else:
            id_usu = self.EditID.text()
            senha = self.EditSenha.text()
            senha_confirme = self.EditConfirme.text()

        nome = self.EditNome.text()
        email = self.EditEmail.text()
        funcao = self.EditFuncao.text()
        login = self.EditLogin.text()
        status = self.ComboStatus.currentText()

        valor = False
        usu = None

        
        if(nome=="" or email=="" or funcao=="" or login=="" or senha=="" or senha_confirme==""):
            msg = QMessageBox.critical(self, "Erro",QString.fromUtf8("Todos os campos são obrigatorios!"), QMessageBox.Close)
        elif(not(re.match('(.+)@(.+)\.(.+)',email,re.IGNORECASE))):        
            msg = QMessageBox.critical(self, "Erro","Email invalido!", QMessageBox.Close)             
        elif(senha!=senha_confirme):
            msg = QMessageBox.critical(self, "Erro",QString.fromUtf8("O campo confirme senha e o campo senha, não são iguais"), QMessageBox.Close)
        else:
            usu = usuario(nome,email,funcao,status,login,senha,id_usu)
            valor = True
        
        return valor,usu

    # Insere os dados do usuario no banco
    def inclusao(self,usu):   
        try:           
            obj = usu
            query = QSqlQuery(self.bancoDeDados)
            query.prepare("INSERT INTO usuario (nome,email,funcao,status,login,senha)" "VALUES (?,?,?,?,?,?)")
            query.addBindValue(obj.nome)
            query.addBindValue(obj.email)
            query.addBindValue(obj.funcao)
            query.addBindValue(obj.status)
            query.addBindValue(obj.login)
            query.addBindValue(obj.senha)
            query.exec_()                   
                 

            if (query.lastError().type() != QSqlError.NoError):
                err = query.lastError()            
                QMessageBox.critical(None, "Erro no cadastro do usuario", err.text())    
                return False    
            else:
                QMessageBox.information(None, "Cadastro de Usuario", "Usuario cadastrado com sucesso!" )
                return True
        except AttributeError:                
            pass

    # Atualiza os dados do usuario que estão no banco
    def atualizacao(self,usu):
        try:           
            obj = usu
            query = QSqlQuery(self.bancoDeDados)
            query.prepare("UPDATE usuario SET nome=?,email=?,funcao=?,status=?,login=? WHERE id_usuario=?")
            query.addBindValue(obj.nome)
            query.addBindValue(obj.email)
            query.addBindValue(obj.funcao)
            query.addBindValue(obj.status)
            query.addBindValue(obj.login)
            query.addBindValue(obj.id)
            query.exec_()                   
                 

            if (query.lastError().type() != QSqlError.NoError):
                err = query.lastError()            
                QMessageBox.critical(None, "Erro no cadastro do usuario", err.text())    
                return False    
            else:
                QMessageBox.information(None, "Cadastro de Usuario", QString.fromUtf8("Usuario alterado com sucesso!\n(Exceto a senha, para mais informações consulte a ajuda)") )
                return True
        except AttributeError:                
            pass

    # Ativa todos os campos de inserção de dados
    def destrava(self):
        self.EditNome.setEnabled(True)
        self.EditEmail.setEnabled(True)
        self.EditFuncao.setEnabled(True)
        self.EditLogin.setEnabled(True)
        self.ComboStatus.setEnabled(True)
        self.EditSenha.setEnabled(True)
        self.EditConfirme.setEnabled(True) 

    # Desativa todos os campos de inserção de dados
    def trava(self):
        self.EditNome.setEnabled(False)
        self.EditEmail.setEnabled(False)
        self.EditFuncao.setEnabled(False)
        self.EditLogin.setEnabled(False)
        self.ComboStatus.setEnabled(False)
        self.EditSenha.setEnabled(False)
        self.EditConfirme.setEnabled(False)   
        

    # Cria uma nova linha na tabela e limpa o formulario de departamentos
    @pyqtSignature("")        
    def on_Novo_clicked(self):
        self.destrava()
        self.setIncluindo(True)
        linha = self.usuarioModel.rowCount()
        self.mapeador.submit()
        self.usuarioModel.insertRow(linha)
        self.mapeador.setCurrentIndex(linha)
        self.EditSenha.setEnabled(True)
        self.EditConfirme.setEnabled(True)
        self.destrava()
        self.EditID.clear()
        self.EditNome.clear()
        self.EditEmail.clear()
        self.EditFuncao.clear()
        self.EditSenha.clear()
        self.EditConfirme.clear()
        self.EditNome.setFocus()

    # Salva os dados no banco de dados depois de validados
    @pyqtSignature("")        
    def on_Salvar_clicked(self):
        try:
            is_valid, usu = self.valido()

            if(usu.id!="" and is_valid and usu.senha=="##########"):
                if(self.atualizacao(usu)):                                            
                    if (self.incluindoUsuario):
                        self.setIncluindo(False)
                    if (self.editandoUsuario):
                        self.setEditando(False)
                    self.abrirTabelaUsuario()
            elif(self.inclusao(usu) and is_valid):
                if (self.incluindoUsuario):
                    self.setIncluindo(False)
                if (self.editandoUsuario):
                    self.setEditando(False)   
                self.abrirTabelaUsuario() 

        except AttributeError:
            pass
    

    # Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma.
    @pyqtSignature("")
    def on_Deletar_clicked(self):
        self.trava()
        linha = self.usuarioModel.rowCount()
        self.usuarioModel.removeRow(linha - 1)    
        self.setIncluindo(False)
        self.setEditando(False)
        self.EditID.clear()
        self.EditNome.clear()
        self.EditEmail.clear()
        self.EditFuncao.clear()
        self.EditLogin.clear()
        self.EditSenha.clear()
        self.EditConfirme.clear()        
        self.abrirTabelaUsuario()         

    # Desativa os campos de texto de senha e confirmar senha, recebe como parametro o texto que esta no campo de texto
    @pyqtSignature("QString")      
    def on_EditNome_textEdited(self, text):
        if (not(self.incluindoUsuario or self.editandoUsuario)):
            self.EditSenha.setEnabled(False)
            self.EditConfirme.setEnabled(False)
            self.setEditando(True)

    @pyqtSignature("QString")      
    def on_EditEmail_textEdited(self, text):
        if (not(self.incluindoUsuario or self.editandoUsuario)):
            self.EditSenha.setEnabled(False)
            self.EditConfirme.setEnabled(False)
            self.setEditando(True)

    @pyqtSignature("QString")      
    def on_EditFuncao_textEdited(self, text):
        if (not(self.incluindoUsuario or self.editandoUsuario)):
            self.EditSenha.setEnabled(False)
            self.EditConfirme.setEnabled(False)
            self.setEditando(True)

    @pyqtSignature("QString")      
    def on_EditLogin_textEdited(self, text):
        if (not(self.incluindoUsuario or self.editandoUsuario)):
            self.EditSenha.setEnabled(False)
            self.EditConfirme.setEnabled(False)
            self.setEditando(True)

    @pyqtSignature("QString")      
    def on_ComboStatus_activated(self, text):
        if (not(self.incluindoUsuario or self.editandoUsuario)):
            self.EditSenha.setEnabled(False)
            self.EditConfirme.setEnabled(False)
            self.setEditando(True)

    # Fecha janela
    @pyqtSignature("") 
    def on_Fechar_clicked(self):
        self.close()
            
        

#-& CLASSE &-#
class CadastroEquipamento(QWidget, Ui_equipamento):
    def __init__(self, parent=None):
        super(CadastroEquipamento, self).__init__(parent)
        self.setupUi(self)

        self.setIncluindo(False)
        self.setEditando(False)
        self.incluindoEquipamento = False        
        self.editandoEquipamento = False

        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")
        self.equipamentoModel = QSqlTableModel(self, self.bancoDeDados)
        #self.abrirTabelaEquipamento()

        self.mapeador = QDataWidgetMapper()
        self.mapeador.setModel(self.equipamentoModel)
        self.mapeador.addMapping(self.EditID, 0)
        self.mapeador.addMapping(self.EditNome, 1)
        self.mapeador.addMapping(self.EditMarca, 2)
        self.mapeador.addMapping(self.EditUnidade, 3)
        self.mapeador.addMapping(self.spinQtd, 4)
        self.mapeador.addMapping(self.spinEstMin, 5)
        self.mapeador.addMapping(self.EditPatrimonio, 6)
        self.mapeador.addMapping(self.comboReponsavel, 7)
        self.mapeador.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)   
        
    def __done__(self):
        QSqlDatabase.removeDatabase("coopervap-bd")

    # Preence a tabela com os dados que estão no banco de dados
    def abrirTabelaEquipamento(self):        
        consulta = "SELECT id_usuario,nome,email,funcao,status,login FROM usuario ORDER BY id_usuario"     
        self.equipamentoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.equipamentoModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.equipamentoModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.equipamentoModel.setHeaderData(2, Qt.Horizontal, "Marca")
        self.equipamentoModel.setHeaderData(3, Qt.Horizontal, "Unidade")
        self.equipamentoModel.setHeaderData(4, Qt.Horizontal, "Qtd")
        self.equipamentoModel.setHeaderData(5, Qt.Horizontal, "Estoque Min")
        self.equipamentoModel.setHeaderData(6, Qt.Horizontal, QString.fromUtf8("Patrimônio"))
        self.equipamentoModel.setHeaderData(7, Qt.Horizontal, QString.fromUtf8("Responsável"))
        self.equipamentoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        self.tabela.setModel(self.equipamentoModel)  


    # Ativa o botão de salvar e  cancelar, se o status for True
    def setIncluindo(self,status):
        self.incluindoEquipamento = status
        self.btSalvar.setEnabled(self.incluindoEquipamento)
        if (self.incluindoEquipamento):
            self.btCancelar.setEnabled(self.incluindoEquipamento)
        else:
            self.btCancelar.setEnabled(self.incluindoEquipamento)
    

    # Ativa o botão de salvar e cancelar, se o status for True
    def setEditando(self,status):
        self.editandoEquipamento = status
        self.btSalvar.setEnabled(self.editandoEquipamento)
        if (self.editandoEquipamento):
            self.btCancelar.setEnabled(self.editandoEquipamento)
        else:
           self.btCancelar.setEnabled(self.editandoEquipamento)















        
        
        
