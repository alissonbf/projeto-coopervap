#!/bin/env python                         
# -*- coding: utf-8 -*-             

## [Ficha]##################################################
#	                                                       #					           
#  Nome: Modulo View				                       #
#                                                          #
#  Escrito por: Alisson Barbosa Ferreira                   #
#               Alisson Oliveira Ferreira                  #
#               Victor Hugo Neiva                          #
#               Wesley Junior                              #
#                                                          #
#  Criado em: 30/08/2010			                       #
#						                                   #
#  Ultima atualizacao: 06/10/2010		                   #
#						                                   #
#  [Descricao]##############################################
#					                                       #
#  Este script contem as classes que se comunicam com      #
#  as interfaces graficas.                                 #
#					                                       #
############################################################

import sys
import re

from PyQt4.QtCore import *                 
from PyQt4.QtGui import *                  


from telas.GuiCadastroUsuario import *

from Controller import *
from Model import *

class principal(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(principal, self).__init__(parent)
        self.setupUi(self)

        self.setIncluindo(False)
        self.setEditando(False)
        self.incluindoUsuario = False        
        self.editandoUsuario = False

        self.bancoDeDados = abrirBancoDeDados(self) 
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
        

        self.connect(self.tabela.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self, SLOT(self.preenche()))
       
        self.EditNome.setEnabled(False)
        self.EditEmail.setEnabled(False)
        self.EditFuncao.setEnabled(False)
        self.EditLogin.setEnabled(False)
        self.EditSenha.setEnabled(False)
        self.EditConfirme.setEnabled(False)  

    # Preence a tabela com os dados que estão no banco de dados
    def abrirTabelaUsuario(self):        
        consulta = "SELECT id_usuario,nome,email,funcao,status,login FROM usuario"     
        self.usuarioModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.usuarioModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.usuarioModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.usuarioModel.setHeaderData(2, Qt.Horizontal, "Email")
        self.usuarioModel.setHeaderData(3, Qt.Horizontal, QString.fromUtf8("Função"))
        self.usuarioModel.setHeaderData(4, Qt.Horizontal, "Status")
        self.usuarioModel.setHeaderData(5, Qt.Horizontal, "Login")
        self.usuarioModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        self.tabela.setModel(self.usuarioModel) 



        

    # Ativa o botão de salvar e muda o nome do botão de excluir para cancelar, se o status for True
    def setIncluindo(self,status):
        self.incluindoUsuario = status
        self.Salvar.setEnabled(self.incluindoUsuario)
        if (self.incluindoUsuario):
            self.Deletar.setEnabled(self.incluindoUsuario)
        else:
            self.Deletar.setEnabled(self.incluindoUsuario)


    # Ativa o botão de salvar e muda o nome do botão de excluir para cancelar, se o status for True
    def setEditando(self,status):
        self.editandoUsuario = status
        self.Salvar.setEnabled(self.editandoUsuario)
        if (self.editandoUsuario):
            self.Deletar.setEnabled(self.editandoUsuario)
        else:
           self.Deletar.setEnabled(self.editandoUsuario)

    # Valida os dados, digitados pelo usuario
    def valido(self):
        if(not(self.EditID.text()=="")):
            id_usu = int(self.EditID.text())
        else:
            id_usu = self.EditID.text()
        nome = self.EditNome.text()
        email = self.EditEmail.text()
        funcao = self.EditFuncao.text()
        login = self.EditLogin.text()
        senha = self.EditSenha.text()
        senha_confirme = self.EditConfirme.text()
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
                QMessageBox.information(None, "Cadastro de Usuario", "Usuario alterado com sucesso!" )
                return True
        except AttributeError:                
            pass


    # Cria uma nova linha na tabela e limpa o formulario de departamentos
    @pyqtSignature("")        
    def on_Novo_clicked(self):
        self.setIncluindo(True)
        linha = self.usuarioModel.rowCount()
        self.mapeador.submit()
        self.usuarioModel.insertRow(linha)
        self.mapeador.setCurrentIndex(linha)
        self.EditSenha.setEnabled(True)
        self.EditConfirme.setEnabled(True)
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

            if(usu.id!="" and is_valid):
                if(self.atualizacao(usu)):                                            
                    if (self.incluindoUsuario):
                        self.setIncluindo(False)
                    if (self.editandoUsuario):
                        self.setEditando(False)
                    self.abrirTabelaUsuario()
            elif(self.inclusao(usu) and is_valid):
                self.mapeador.submit()
                if (self.incluindoUsuario):
                    self.setIncluindo(False)
                if (self.editandoUsuario):
                    self.setEditando(False)
                self.usuarioModel.submitAll()        
                self.abrirTabelaUsuario() 

        except AttributeError:
            pass
    
    @pyqtSignature("")
    def on_Deletar_clicked(self):
        linha = self.usuarioModel.rowCount()
        self.usuarioModel.removeRow(linha - 1)        
        self.EditID.clear()
        self.EditNome.clear()
        self.EditEmail.clear()
        self.EditFuncao.clear()
        self.EditLogin.clear()
        self.EditSenha.clear()
        self.EditConfirme.clear()
        self.EditNome.setFocus()
        self.abrirTabelaUsuario()     

    def preenche(self):
        self.EditNome.setEnabled(True)
        self.EditEmail.setEnabled(True)
        self.EditFuncao.setEnabled(True)
        self.EditLogin.setEnabled(True)
        self.EditSenha.setEnabled(True)
        self.EditConfirme.setEnabled(True)        

    @pyqtSignature("QString")      
    def on_EditNome_textEdited(self, text):
        print "Sinal enviado"
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


    @pyqtSignature("") 
    def on_Fechar_clicked(self):
        self.close()
            
        

        
















        
        
        
