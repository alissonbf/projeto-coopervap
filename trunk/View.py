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
#  Ultima atualizacao: 22/12/2010		           #
#						           #
#  [Descricao]##############################################
#					                   #
#  Este script contem as classes que se comunicam com      #
#  as interfaces graficas e da vida aos seus botões        #
#					                   #
############################################################
import re
import webbrowser
import time

from PyQt4.QtCore import *                 
from PyQt4.QtGui import *         

from telas.GuiPrincipal import *

from telas.GuiCadastroUsuario import *
from telas.GuiCadastroEquipamento import *
from telas.GuiCadastroDepartamento import *
from telas.GuiCadastroTecnico import *
from telas.GuiPedidoDeCompra import *

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

        # Variavel globais
        self.id=int()        

        abrirBancoDeDados(self)
        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")

        # Abre o arquivo de login do sistema
        self.file=open('data/login','a')

        # Cria a area onde as sub-janelas serão abertas
        self.MdiArea = QMdiArea(self)
        


    def __del__(self):
        QSqlDatabase.removeDatabase("coopervap-bd")
        

    # Mostra janela para manutenção de usuarios, paramentro obj é a janela a ser aberta
    def mostrarSubwindow(self, obj):
        window = obj               
        SubWindow = QMdiSubWindow()
        SubWindow.setWidget(window)        
        SubWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.MdiArea.addSubWindow(SubWindow)
        SubWindow.show()
        
    # Grava os dados do usuario logado no arquivo de login
    def log(self,u,s):
        user  = u
        senha = s
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT id_usuario FROM usuario WHERE login=? and senha=? and status=?")
        query.addBindValue(user)
        query.addBindValue(senha)
        query.addBindValue("Ativo")
        query.exec_()
        while(query.next()):            
            self.id = query.value(0).toInt()            
            
        tempo=time.localtime()        
        salve=str(self.id[0])+' '+str(tempo[2])+'/'+str(tempo[1])+'/'+str(tempo[0])+' '+str(tempo[3])+':'+str(tempo[4])+':'+str(tempo[5])+'\n'
        self.file.write(salve)
        self.file.close()

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
        while(query.next()):            
            var = query.value(0).toInt()
            if var[0] == 1:
                self.log(user, senha)
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
    def on_actionCadastrar_Tecnicos_triggered(self):
        cadtec = CadastroTecnico()
        self.mostrarSubwindow(cadtec)

    @pyqtSignature("")
    def on_actionCadastrar_Departamentos_triggered(self):
        caddepto = CadastroDepartamento()
        self.mostrarSubwindow(caddepto)

    @pyqtSignature("")
    def on_actionCadastrar_SubDepartamentos_triggered(self):
        cadsub = CadastroSubdepartamento()
        self.mostrarSubwindow(cadsub)

    @pyqtSignature("")
    def on_actionRealizar_Pedido_de_Compra_triggered(self):
        pedido = PedidoDeCompra()
        self.mostrarSubwindow(pedido)

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
class CadastroDepartamento(QWidget, Ui_departamento):
    def __init__(self, parent=None):
        super(CadastroDepartamento, self).__init__(parent)
        self.setupUi(self)
        self.setIncluindo(False)
        self.setEditando(False)
        self.incluindoDepartamento = False
        self.editandoDepartamento = False
        self.EditID.setVisible(False)
        
        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")
        self.departamentoModel = QSqlTableModel(self, self.bancoDeDados)
        self.abrirTabelaDepartamento()

        self.mapeador = QDataWidgetMapper()
        self.mapeador.setModel(self.departamentoModel)
        self.mapeador.addMapping(self.EditID, 0)
        self.mapeador.addMapping(self.EditNome, 1)
        self.mapeador.addMapping(self.EditCentroCusto, 2)
        self.mapeador.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        
        self.connect(self.tabela.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeador, SLOT("setCurrentModelIndex(QModelIndex)"))

    # Preence a tabela com os dados que estão no banco de dados
    def abrirTabelaDepartamento(self):
        consulta = "SELECT id_departamento,nome,centro_de_custo FROM departamento ORDER BY id_departamento"
        self.departamentoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.departamentoModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.departamentoModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.departamentoModel.setHeaderData(2, Qt.Horizontal, "Centro de custo")
        self.departamentoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.tabela.setModel(self.departamentoModel)

    
    # Ativa o botão de salvar e  cancelar, se o status for True
    def setIncluindo(self,status):
        self.incluindoDepartamento = status
        self.btSalvar.setEnabled(self.incluindoDepartamento)



    # Ativa o botão de salvar e cancelar, se o status for True
    def setEditando(self,status):
        self.editandoDepartamento = status
        self.btSalvar.setEnabled(self.editandoDepartamento)


    # Valida todos os campos da tela de departamento
    def Valido(self):
        if(self.EditID.text()!=""):
            id=int(self.EditID.text())
        else:
            id=self.EditID.text()
            
        nome=self.EditNome.text()
        centro=self.EditCentroCusto.text()

        if (nome=="" or centro==".."):
            msg = QMessageBox.critical(self, "Erro",QString.fromUtf8("Todos os campos são obrigatorios!"), QMessageBox.Close)
            return False, None
        else:
            depto=departamento(nome,centro,id)
            return True, depto

    # Atualiza os dados no banco de dados
    def atualiza(self,obj):
        try:
            depto=obj

            # Captura do arquivo de login o usuario logado
            file=open("data/login","r")
            texto=file.readlines()
            last_login=texto[len(texto)-1]
            id_usu=last_login[0]

            query = QSqlQuery(self.bancoDeDados)
            query.prepare("UPDATE departamento set nome=?, centro_de_custo=?, id_usuario=? WHERE id_departamento=?")
            query.addBindValue(depto.nome)
            query.addBindValue(depto.centro)            
            query.addBindValue(id_usu)
            query.addBindValue(depto.id)
            query.exec_()

            if (query.lastError().type() != QSqlError.NoError):
                err = query.lastError()
                QMessageBox.critical(None, "Erro na atualização do departamento", err.text())
                return False
            else:
                QMessageBox.information(None, QString.fromUtf8("Atualização do Departamento"), "Departamento atualizado com sucesso!" )
                return True
        except AttributeError:
            pass
        
    # Insere os dados no banco de dados
    def insere(self,obj):
        try:
            depto=obj

            # Captura do arquivo de login o usuario logado
            file=open("data/login","r")
            texto=file.readlines()
            last_login=texto[len(texto)-1]
            id_usu=last_login[0]
            
            query = QSqlQuery(self.bancoDeDados)
            query.prepare("INSERT INTO departamento (nome,centro_de_custo,id_usuario)" "VALUES (?,?,?)")
            query.addBindValue(depto.nome)
            query.addBindValue(depto.centro)
            query.addBindValue(id_usu)
            query.exec_()

            if (query.lastError().type() != QSqlError.NoError):
                err = query.lastError()
                QMessageBox.critical(None, "Erro no cadastro do departamento", err.text())
                return False
            else:
                QMessageBox.information(None, "Cadastro de Departamento", "Departamento cadastrado com sucesso!" )
                return True
        except AttributeError:
            pass

    # Insere ou atualiza os dados no banco de dados
    @pyqtSignature("")
    def on_btSalvar_clicked(self):
        is_valid, depto=self.Valido()
        
        if (is_valid and depto.id!=""):
            if(self.atualiza(depto)):
                if (self.incluindoDepartamento):
                    self.setIncluindo(False)
                if (self.editandoDepartamento):
                    self.setEditando(False)
                self.abrirTabelaDepartamento()
        elif(is_valid):
            if(self.insere(depto)):
                if (self.incluindoDepartamento):
                    self.setIncluindo(False)
                if (self.editandoDepartamento):
                    self.setEditando(False)
                self.abrirTabelaDepartamento()

            
    # Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma.
    @pyqtSignature("")
    def on_btCancelar_clicked(self):
        self.setIncluindo(False)
        self.setEditando(False)
        self.EditID.clear()
        self.EditNome.clear()
        self.EditCentroCusto.clear()
        self.abrirTabelaDepartamento()

    # Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado
    @pyqtSignature("QString")
    def on_EditNome_textEdited(self, text):
        if (not(self.incluindoDepartamento or self.editandoDepartamento)):
            self.setEditando(True)

    # Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado
    @pyqtSignature("QString")
    def on_EditCentroCusto_textEdited(self, text):
        if (not(self.incluindoDepartamento or self.editandoDepartamento)):            
            self.setEditando(True)

#-& CLASSE &-#
class CadastroTecnico(QWidget, Ui_tecnico):
    def __init__(self, parent=None):
        super(CadastroTecnico, self).__init__(parent)
        self.setupUi(self)
        
        self.setIncluindo(False)
        self.setEditando(False)
        self.incluindoTecnico = False
        self.editandoTecnico = False
        
        self.EditID.setVisible(False)
        self.EditUsuario.setVisible(False)        

        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")
        self.tecnicoModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        self.abrirTabelaTecnico()
        self.abrirComboDepto()

        self.mapeador = QDataWidgetMapper()
        self.mapeador.setModel(self.tecnicoModel)

        self.relacionalDelegate = QSqlRelationalDelegate(self.mapeador)

        self.mapeador.setItemDelegate(self.relacionalDelegate)
        self.comboDepto.model().sort(1, Qt.AscendingOrder)

        self.mapeador.addMapping(self.EditID, 0)
        self.mapeador.addMapping(self.EditNome, 1)
        self.mapeador.addMapping(self.EditFuncao, 2)
        self.mapeador.addMapping(self.comboStatus, 3)
        self.mapeador.addMapping(self.comboDepto, 4)        
        self.mapeador.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)

        self.connect(self.tabela.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeador, SLOT("setCurrentModelIndex(QModelIndex)"))    

    # Preence a tabela com os dados que estão no banco de dados
    def abrirTabelaTecnico(self):
        consulta = "SELECT t.id_tecnico,t.nome,t.funcao,t.status,d.nome FROM tecnico t, departamento d WHERE d.id_departamento=t.id_departamento ORDER BY id_tecnico"
        self.tecnicoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
        
        self.tecnicoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.tecnicoModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.tecnicoModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.tecnicoModel.setHeaderData(2, Qt.Horizontal, QString.fromUtf8("Função"))
        self.tecnicoModel.setHeaderData(3, Qt.Horizontal, "Status")
        self.tecnicoModel.setHeaderData(4, Qt.Horizontal, "Departamento")
        
        self.tecnicoModel.select()
        
        self.tabela.setModel(self.tecnicoModel)
        self.tabela.show()
        self.tabela.resizeColumnsToContents()
        self.tabela.sortByColumn(0, Qt.AscendingOrder)

    # Preenche o Combo de Departamentos
    def abrirComboDepto(self):
        self.tecnicoModel.setRelation(4, QSqlRelation("DEPARTAMENTO", "ID_DEPARTAMENTO", "NOME"))
        relacaoModel = self.tecnicoModel.relationModel(4)
        self.comboDepto.setModel(relacaoModel)
        self.comboDepto.setModelColumn(relacaoModel.fieldIndex("NOME"))        

    # Captura do arquivo de login o usuario logado
    def addUsuarioLogado(self):        
        file=open("data/login","r")
        texto=file.readlines()
        last_login=texto[len(texto)-1]
        id_usu=last_login[0]
        
        return id_usu        

    # Ativa o botão de salvar e  cancelar, se o status for True
    def setIncluindo(self,status):
        self.incluindoTecnico = status
        self.btSalvar.setEnabled(self.incluindoTecnico)

    # Ativa o botão de salvar e cancelar, se o status for True
    def setEditando(self,status):
        self.editandoTecnico = status
        self.btSalvar.setEnabled(self.editandoTecnico)

    # Valida todos os campos da tela de tecnicos
    def Valido(self):
        if(self.EditID.text()!=""):
            id=int(self.EditID.text())
        else:
            id=self.EditID.text()

        nome=self.EditNome.text()
        funcao=self.EditFuncao.text()
        departamento=self.comboDepto.currentText()
        status = self.comboStatus.currentText()
        id_usuario = int(self.addUsuarioLogado())
        
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT id_departamento FROM departamento d WHERE d.nome=?")
        query.addBindValue(departamento)
        query.exec_()

        while(query.next()):
            id_depto = query.value(0).toInt()
        
        if (nome=="" or funcao==""):
            msg = QMessageBox.critical(self, "Erro",QString.fromUtf8("Todos os campos são obrigatorios!"), QMessageBox.Close)
            return False, None
        else:
            tec = tecnico(nome,funcao,id_depto[0],status,id_usuario,id)
            return True, tec

    def atualiza(self,obj):
        try:
            tec=obj

            query = QSqlQuery(self.bancoDeDados)
            query.prepare("UPDATE tecnico SET nome=?, funcao=?, status=?, id_usuario=?, id_departamento=? WHERE id_tecnico=?")
            query.addBindValue(tec.nome)
            query.addBindValue(tec.funcao)
            query.addBindValue(tec.status)
            query.addBindValue(tec.usuario)
            query.addBindValue(tec.departamento)
            query.addBindValue(tec.id)
            query.exec_()
            
            if (query.lastError().type() != QSqlError.NoError):
                err = query.lastError()
                QMessageBox.critical(None, QString.fromUtf8("Erro na atualização do tecnico"), err.text())
                return False
            else:
                QMessageBox.information(None, QString.fromUtf8("Atualização do Tecnico"), "Tecnico atualizado com sucesso!" )
                return True
        except AttributeError:
            pass

    # Insere os dados no banco de dados
    def insere(self,obj):
        try:
            tec=obj            

            query = QSqlQuery(self.bancoDeDados)
            query.prepare("INSERT INTO tecnico (nome,funcao,status,id_usuario,id_departamento)" "VALUES (?,?,?,?,?)")
            query.addBindValue(tec.nome)
            query.addBindValue(tec.funcao)
            query.addBindValue(tec.status)
            query.addBindValue(tec.usuario)
            query.addBindValue(tec.departamento)
            query.exec_()

            if (query.lastError().type() != QSqlError.NoError):
                err = query.lastError()
                QMessageBox.critical(None, "Erro no cadastro do tecnico", err.text())
                return False
            else:
                QMessageBox.information(None, "Cadastro de Tecnico", "Tecnico cadastrado com sucesso!" )
                return True
        except AttributeError:
            pass

    # Insere o altualiza os dados no banco de dados
    @pyqtSignature("")
    def on_btSalvar_clicked(self):
        is_valid, tecnico=self.Valido()

        if (is_valid and tecnico.id!=""):
            if(self.atualiza(tecnico)):
                if (self.incluindoTecnico):
                    self.setIncluindo(False)
                if (self.editandoTecnico):
                    self.setEditando(False)
                self.abrirTabelaTecnico()
        elif(is_valid):
            if(self.insere(tecnico)):
                if (self.incluindoTecnico):
                    self.setIncluindo(False)
                if (self.editandoTecnico):
                    self.setEditando(False)
                self.abrirTabelaTecnico()


    # Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma.
    @pyqtSignature("")
    def on_btCancelar_clicked(self):        
        self.setIncluindo(False)
        self.setEditando(False)
        self.EditID.clear()
        self.EditNome.clear()
        self.EditFuncao.clear()
        self.abrirTabelaTecnico()

    # Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado
    @pyqtSignature("QString")
    def on_EditNome_textEdited(self, text):
        if (not(self.incluindoTecnico or self.editandoTecnico)):
            self.setEditando(True)

    @pyqtSignature("QString")
    def on_EditFuncao_textEdited(self, text):
        if (not(self.incluindoTecnico or self.editandoTecnico)):
            self.setEditando(True)


    


#-& CLASSE &-#
class CadastroEquipamento(QWidget, Ui_equipamento):
    def __init__(self, parent=None):
        super(CadastroEquipamento, self).__init__(parent)
        self.setupUi(self)

        self.EditID.setVisible(False)        
        self.id_usuario = self.addUsuarioLogado()

        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")
        self.departamentoModel = QSqlTableModel(self, self.bancoDeDados)

        self.equipamentoModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        self.abrirComboResponsavel()

        self.abrirTabelaEquipamento()

        self.mapeador = QDataWidgetMapper()
        self.mapeador.setModel(self.equipamentoModel)

        self.relacionalDelegate = QSqlRelationalDelegate(self.mapeador)

        self.mapeador.setItemDelegate(self.relacionalDelegate)
        self.mapeador.addMapping(self.EditID, 0)
        self.mapeador.addMapping(self.EditNome, 1)
        self.mapeador.addMapping(self.EditMarca, 2)
        self.mapeador.addMapping(self.EditUnidade, 3)
        self.mapeador.addMapping(self.spinQtd, 4)
        self.mapeador.addMapping(self.spinEstMin, 5)
        self.mapeador.addMapping(self.comboReponsavel, 6)
        self.mapeador.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        
        self.connect(self.tabela.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeador, SLOT("setCurrentModelIndex(QModelIndex)"))

    #Mostra os dados que estão na tabela
    def abrirTabelaEquipamento(self):
        consulta = "select e.id_equipamento, e.nome, e.marca_modelo, e.unidade, e.quantidade_inicial, e.estoque_min, t.nome from equipamento e , tecnico t where e.id_tecnico = t.id_tecnico order by e.id_equipamento"
        self.equipamentoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
        
        self.equipamentoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.equipamentoModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.equipamentoModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.equipamentoModel.setHeaderData(2, Qt.Horizontal, QString.fromUtf8("Marca"))
        self.equipamentoModel.setHeaderData(3, Qt.Horizontal, "Unidade")
        self.equipamentoModel.setHeaderData(4, Qt.Horizontal, "Qtd")        
        self.equipamentoModel.setHeaderData(5, Qt.Horizontal, "Estoque Min")
        self.equipamentoModel.setHeaderData(6, Qt.Horizontal, "Responsavel")

        self.equipamentoModel.select()
        
        self.tabela.setModel(self.equipamentoModel)
        self.tabela.show()
        self.tabela.resizeColumnsToContents()
        self.tabela.sortByColumn(0, Qt.AscendingOrder)
            

    # Preenche o Combo de Departamentos
    def abrirComboResponsavel(self):
        self.equipamentoModel.setRelation(1, QSqlRelation("TECNICO", "ID_TECNICO", "NOME"))
        relacaoModel = self.equipamentoModel.relationModel(1)
        self.comboReponsavel.setModel(relacaoModel)
        self.comboReponsavel.setModelColumn(relacaoModel.fieldIndex("NOME"))


    # Captura do arquivo de login o usuario logado
    def addUsuarioLogado(self):        
        file=open("data/login","r")
        texto=file.readlines()
        last_login=texto[len(texto)-1]
        id_usu=last_login[0]
        
        return id_usu

    # Insere o altualiza os dados no banco de dados
    @pyqtSignature("")
    def on_btSalvar_clicked(self): 
        verifica, equip = self.validaEquipamento()
        if (verifica and equip.id_equip == ""):
            self.inserirEquipamento(equip)
            self.abrirTabelaEquipamento()
            self.EditNome.clear()
            self.EditMarca.clear()
            self.EditUnidade.clear()
            self.spinQtd.clear()
            self.PesquisaNome.clear()  
            self.PesquisaMarca.clear()
        else:
            self.atualizaEquipamento(equip)
            self.abrirTabelaEquipamento()
            self.EditNome.clear()
            self.EditMarca.clear()
            self.EditUnidade.clear()
            self.spinQtd.clear()
            self.PesquisaNome.clear() 
            self.PesquisaMarca.clear()
        
    #Insere os dados no banco de dados
    def inserirEquipamento(self, equip):
        equip = equip
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("insert into equipamento (nome, marca_modelo, unidade, quantidade_inicial, estoque_min, id_usuario, id_tecnico)" "values ( ?,?,?,?,?,?,?)")
        query.addBindValue(equip.nome)
        query.addBindValue(equip.marca)
        query.addBindValue(equip.unidade)
        query.addBindValue(equip.quantidade)
        query.addBindValue(equip.estoque)
        query.addBindValue(equip.usuario)
        query.addBindValue(equip.id_resp)
        query.exec_()      
        
        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(None, QString.fromUtf8("Erro na inserção do equipamento"), err.text())
        else:
            QMessageBox.information(None, QString.fromUtf8("Inserção do Equipamento"), "Equipamento inserido com sucesso!" )


    @pyqtSignature("")
    def on_btCancelar_clicked(self):
        self.EditID.clear()
        self.EditNome.clear()
        self.EditMarca.clear()
        self.EditUnidade.clear()
        self.spinQtd.clear()
        self.spinEstMin.clear()
        self.PesquisaNome.clear()
        self.PesquisaMarca.clear()
        self.abrirTabelaEquipamento()

    #Atualiza os dados do equipamento
    def atualizaEquipamento(self, equip):
        equip = equip
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("update equipamento set nome =?, marca_modelo = ?, unidade = ?, quantidade_inicial = ?, estoque_min = ?, id_usuario = ?, id_tecnico = ? where id_equipamento = ?")
        query.addBindValue(equip.nome)
        query.addBindValue(equip.marca)
        query.addBindValue(equip.unidade)
        query.addBindValue(equip.quantidade)
        query.addBindValue(equip.estoque)
        query.addBindValue(equip.usuario)
        query.addBindValue(equip.id_resp)
        query.addBindValue(equip.id_equip)
        query.exec_()

        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(None, QString.fromUtf8("Erro ao alterar equipamento"), err.text())
        else:
            QMessageBox.information(None, QString.fromUtf8("Atualização do Equipamento"), "Equipamento alterado com sucesso!" )
            

    #Captura o ID do responsavel
    def capturaResponsavel(self):

        responsavel = self.comboReponsavel.currentText()
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT id_tecnico FROM tecnico t WHERE t.nome=?")
        query.addBindValue(responsavel)
        query.exec_()

        while(query.next()):
            id_resp = query.value(0).toInt()

        return id_resp[0]

    # Valida todos os campos da tela de equipamento 
    def validaEquipamento(self):
        id_equip = self.EditID.text()
        if (id_equip == ""):
            pass
        else:
            id_equip = int(id_equip)
        
        nome = self.EditNome.text()
        marca_modelo = self.EditMarca.text()
        unidade = self.EditUnidade.text()
        quantidade_inicial = self.spinQtd.value()
        estoque_min = self.spinEstMin.value()    

        id_resp = self.capturaResponsavel()

        if (nome == "" or marca_modelo == "" or quantidade_inicial == "" or estoque_min == ""):
            QMessageBox.critical(None, QString.fromUtf8("Erro"), QString.fromUtf8("Alguns desses campos estão vazios:\n nome\n marca\n quantidade\n estoque minimo" ))
            return False, None
        else:
            equip = equipamento(nome, marca_modelo, unidade, quantidade_inicial, estoque_min, id_resp,self.id_usuario, id_equip)
            return True, equip

    # Faz uma busca no banco de dados, o tipo de busca varia de acordo com o parametro sql
    def buscaIncremental(self, sql):
        consulta = sql

        self.equipamentoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
        
        self.equipamentoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.equipamentoModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.equipamentoModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.equipamentoModel.setHeaderData(2, Qt.Horizontal, QString.fromUtf8("Marca"))
        self.equipamentoModel.setHeaderData(3, Qt.Horizontal, "Unidade")
        self.equipamentoModel.setHeaderData(4, Qt.Horizontal, "Qtd")        
        self.equipamentoModel.setHeaderData(5, Qt.Horizontal, "Estoque Min")
        self.equipamentoModel.setHeaderData(6, Qt.Horizontal, "Responsavel")

        self.equipamentoModel.select()
        
        self.tabela.setModel(self.equipamentoModel)
        self.tabela.show()
        self.tabela.resizeColumnsToContents()
        self.tabela.sortByColumn(0, Qt.AscendingOrder)

    # Capitura o que o usuario digitou e monta um comando sql, para busca pelo nome do equipamento
    @pyqtSignature("QString")
    def on_PesquisaNome_textChanged(self, text):
        texto = '%'+text+'%'
        consulta = "select e.id_equipamento, e.nome, e.marca_modelo, e.unidade, e.quantidade_inicial, e.estoque_min, t.nome from equipamento e , tecnico t where e.id_tecnico = t.id_tecnico and e.nome like '%s' order by e.id_equipamento" % texto

        self.buscaIncremental(consulta)

    # Capitura o que o usuario digitou e monta um comando sql, para busca pela marca do equipamento
    @pyqtSignature("QString")
    def on_PesquisaMarca_textChanged(self, text):
        texto = '%'+text+'%'
        consulta = "select e.id_equipamento, e.nome, e.marca_modelo, e.unidade, e.quantidade_inicial, e.estoque_min, t.nome from equipamento e , tecnico t where e.id_tecnico = t.id_tecnico and e.marca_modelo like '%s' order by e.id_equipamento" % texto

        self.buscaIncremental(consulta)



#-& CLASSE &-#
class PedidoDeCompra(QWidget, Ui_pedidodecompra):
    def __init__(self, parent=None):
        super(PedidoDeCompra, self).__init__(parent)
        self.setupUi(self)


        


    
        

    


        
        
        
