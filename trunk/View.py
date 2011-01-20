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
#  Ultima atualizacao: 31/12/2010		           #
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
import sys

from PyQt4.QtCore import *                 
from PyQt4.QtGui import *         

from telas.GuiPrincipal import *

from telas.GuiCadastroUsuario import *
from telas.GuiCadastroEquipamento import *
from telas.GuiCadastroDepartamento import *
from telas.GuiCadastroTecnico import *
from telas.GuiPedidoDeCompra import *
from telas.GuiBaixaMaterial import *

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
        
        # Posiciona a janela no centro da tela
        self.posicao_central_w = int(QApplication.desktop().screen().width()/2)
        self.posicao_central_h = int(QApplication.desktop().screen().height()/2)
    
        self.setGeometry(
            self.posicao_central_w - (self.width()/2),
            self.posicao_central_h - (self.height()/2),
            self.width(),
            self.height())      

        abrirBancoDeDados(self)
        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")

        # Abre o arquivo de login do sistema
        arq = sys.path[0]+ '/data/login'
        self.file=open(arq,'a')

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
    def on_actionRealizar_Baixa_no_Estoque_triggered(self):
        baixa = BaixaMaterial()
        self.mostrarSubwindow(baixa)

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
        verifica = QMessageBox.warning(self, "Sair do Programa", u"Deseja realmente Sair?\n Verifique se não existe nenhuma operação pedente\n ou se todas as janelas estão fechadas!", buttons=QMessageBox.Ok | QMessageBox.Cancel, defaultButton=QMessageBox.Cancel)
        if verifica == QMessageBox.Ok:
                self.close()




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
            

    # Preenche o Combo de Responsaveis
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

    # Limpa os dados do formulario
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
        try:
            responsavel = self.comboReponsavel.currentText()
            query = QSqlQuery(self.bancoDeDados)
            query.prepare("SELECT id_tecnico FROM tecnico t WHERE t.nome=?")
            query.addBindValue(responsavel)
            query.exec_()

            while(query.next()):
                id_resp = query.value(0).toInt()

            return id_resp[0]
        except(UnboundLocalError):
            QMessageBox.warning(None, QString.fromUtf8("Erro"), QString.fromUtf8("Não foi escolhido nenhum responsavel!" ))

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
            QMessageBox.warning(None, QString.fromUtf8("Erro"), QString.fromUtf8("Alguns desses campos estão vazios:\n nome\n marca\n quantidade\n estoque minimo" ))
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

        self.EditID.setVisible(False)        
        self.id_usuario = self.addUsuarioLogado()

        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")

              
        
        #-- Mapeador, Model e configuração para os dados da primeira fase do pedido de compra --#
        self.pedidocombraModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        self.montarTabelaPedidoCompra()


        self.mapeadorPedidoCompra = QDataWidgetMapper()
        self.mapeadorPedidoCompra.setModel(self.pedidocombraModel)

        self.relacionalDelegate = QSqlRelationalDelegate(self.mapeadorPedidoCompra)

        self.mapeadorPedidoCompra.setItemDelegate(self.relacionalDelegate)
        self.mapeadorPedidoCompra.addMapping(self.EditPedido, 0)
        self.mapeadorPedidoCompra.addMapping(self.EditData, 1)
        self.mapeadorPedidoCompra.addMapping(self.comboResponsavel, 2)
        self.mapeadorPedidoCompra.addMapping(self.comboStatus, 3)
        self.mapeadorPedidoCompra.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        
        self.connect(self.TabelaPedido.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeadorPedidoCompra, SLOT("setCurrentModelIndex(QModelIndex)"))     

        # Chama o metodo que preenche o combo de responsaveis
        self.abrirComboResponsavel()

        #-- Mapeador, Model e configuração para os dados da segunda fase do pedido de compra --#
        self.equipamentopedidoModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        self.montarTabelaEquipamentoPedido()

        self.mapeadorEquipamentoPedido = QDataWidgetMapper()
        self.mapeadorEquipamentoPedido.setModel(self.equipamentopedidoModel)

        self.relacionalDelegate = QSqlRelationalDelegate(self.mapeadorEquipamentoPedido)

        self.mapeadorEquipamentoPedido.setItemDelegate(self.relacionalDelegate)
        self.mapeadorEquipamentoPedido.addMapping(self.EditID, 0)
        self.mapeadorEquipamentoPedido.addMapping(self.EditPedidoEq, 1)
        self.mapeadorEquipamentoPedido.addMapping(self.EditNome, 2)
        self.mapeadorEquipamentoPedido.addMapping(self.EditUnidade, 3)
        self.mapeadorEquipamentoPedido.addMapping(self.EditEntrega, 4)
        self.mapeadorEquipamentoPedido.addMapping(self.EditDescricao, 5)
        self.mapeadorEquipamentoPedido.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)

        self.connect(self.TabelaEquipamento.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeadorEquipamentoPedido, SLOT("setCurrentModelIndex(QModelIndex)"))

        #-- Mapeador, Model e configuração para os dados para busca do pedido de compra --#

        self.pedidobuscaModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        
        self.mapeadorbuscaPedidoCompra = QDataWidgetMapper()
        self.mapeadorbuscaPedidoCompra.setModel(self.pedidobuscaModel)

        self.relacionalDelegate = QSqlRelationalDelegate(self.mapeadorbuscaPedidoCompra)

        self.mapeadorbuscaPedidoCompra.setItemDelegate(self.relacionalDelegate)
        self.mapeadorbuscaPedidoCompra.addMapping(self.EditPedido, 0)
        self.mapeadorbuscaPedidoCompra.addMapping(self.EditData, 2)
        self.mapeadorbuscaPedidoCompra.addMapping(self.comboResponsavel, 3)
        self.mapeadorbuscaPedidoCompra.addMapping(self.comboStatus, 4)
        

        self.mapeadorbuscaPedidoCompra.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)


        self.montar_tabela_de_busca_pedido( "select p.codigo, pe.nome, p.data, t.nome, p.status from pedido_compra p, tecnico t, pedido_equipamento pe where t.id_tecnico = p.id_tecnico AND pe.codigo = p.codigo")

        self.connect(self.TabelaBusca.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeadorbuscaPedidoCompra, SLOT("setCurrentModelIndex(QModelIndex)"))
        

        
    # Captura do arquivo de login o usuario logado
    def addUsuarioLogado(self):        
        file=open("data/login","r")
        texto=file.readlines()
        last_login=texto[len(texto)-1]
        id_usu=last_login[0]
        
        return id_usu

    # Preenche o Combo de Responsaveis
    def abrirComboResponsavel(self):
        self.pedidocombraModel.setRelation(1, QSqlRelation("TECNICO", "ID_TECNICO", "NOME"))
        relacaoModel = self.pedidocombraModel.relationModel(1)
        self.comboResponsavel.setModel(relacaoModel)             
        self.comboResponsavel.setModelColumn(relacaoModel.fieldIndex("NOME"))
        self.BuscaResponsavel.setModel(relacaoModel)
        self.BuscaResponsavel.setModelColumn(relacaoModel.fieldIndex("NOME"))

   
    
    # Captura o ID do responsavel
    def capturaResponsavel(self):
        responsavel = self.comboResponsavel.currentText()
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT id_tecnico FROM tecnico t WHERE t.nome=?")
        query.addBindValue(responsavel)
        query.exec_()

        while(query.next()):
            id_resp = query.value(0).toInt()

        return id_resp[0]

    # Valida os dados da primeira etapa do pedido de compra
    def validaPedido(self):
        try:
            id_pedido = int(self.EditPedido.text())
            id_resp = self.capturaResponsavel()            
            data = self.EditData.text()
            status = self.comboStatus.currentText()

            if (data == ''):
                QMessageBox.critical(None, QString.fromUtf8("Erro"), QString.fromUtf8("Todos os campos são obrigatórios!" ))
                return False, None
            else:
                pedido = pedidocompra(data,status,self.id_usuario,id_resp,id_pedido)
                return True, pedido

        except(ValueError):
            QMessageBox.critical(None, QString.fromUtf8("Erro"), QString.fromUtf8("Digite apenas numeros no campo Nº do pedido de compra!" ))


    # Valida os dados da primeira etapa do pedido de compra
    def validaEquipamento(self):
        id = self.EditID.text()
        id_pedido = int(self.EditPedidoEq.text())
        nome = self.EditNome.text()
        unidade = self.EditUnidade.text()
        entrega = self.EditEntrega.text()
        descricao = self.EditDescricao.toPlainText()

        if (len(descricao)>400):
            QMessageBox.critical(None, QString.fromUtf8("Erro"), QString.fromUtf8("O campo descricação tem mais que 400 caracteres!" ))
            return False, None
        elif(nome=='' or entrega == '' or descricao == ''):
            QMessageBox.critical(None, QString.fromUtf8("Erro"), QString.fromUtf8("Algum desses campos está em branco:\n-Nome\n-entregar até\n-Descrição!" ))
            return False, None
        else:
            equipedido = equipamentopedido(nome,descricao,unidade,entrega,id_pedido,id)
            return True, equipedido
        

    # Mostra o pedido que acabou de ser inserido
    def abrirTabelaPedidoCompra(self,obj):
        pedido = obj
        consulta = "SELECT p.codigo,p.data,t.nome,p.status FROM pedido_compra p, tecnico t WHERE p.codigo = %s AND t.id_tecnico = p.id_tecnico AND p.codigo = p.codigo "  %(pedido.id)
        self.pedidocombraModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
        
        self.pedidocombraModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.pedidocombraModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.pedidocombraModel.setHeaderData(1, Qt.Horizontal, "Data")
        self.pedidocombraModel.setHeaderData(2, Qt.Horizontal, QString.fromUtf8("Responsável"))
        self.pedidocombraModel.setHeaderData(3, Qt.Horizontal, "Status")

        self.pedidocombraModel.select()
        
        self.TabelaPedido.setModel(self.pedidocombraModel)
        self.TabelaPedido.show()
        self.TabelaPedido.resizeColumnsToContents()
        self.TabelaPedido.sortByColumn(0, Qt.AscendingOrder)

    # Mostra o equipamento que acabou de ser inserido no pedido
    def abrirTabelaEquipamentoPedido(self,obj):
        equipedido = obj
        consulta = "SELECT pe.id, pe.codigo, pe.nome, pe.unidade, pe.entrega, pe.descricao FROM pedido_equipamento pe WHERE pe.codigo = %i" %(equipedido.id_pedido)
        self.equipamentopedidoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.equipamentopedidoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.equipamentopedidoModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.equipamentopedidoModel.setHeaderData(1, Qt.Horizontal, "Pedido")
        self.equipamentopedidoModel.setHeaderData(2, Qt.Horizontal, "Nome")
        self.equipamentopedidoModel.setHeaderData(3, Qt.Horizontal, "Unidade")
        self.equipamentopedidoModel.setHeaderData(4, Qt.Horizontal, QString.fromUtf8("entregar até"))
        self.equipamentopedidoModel.setHeaderData(5, Qt.Horizontal, QString.fromUtf8("Descrição"))

        self.equipamentopedidoModel.select()

        self.TabelaEquipamento.setModel(self.equipamentopedidoModel)
        self.TabelaEquipamento.show()
        self.TabelaEquipamento.resizeColumnsToContents()
        self.TabelaEquipamento.sortByColumn(0, Qt.AscendingOrder)
        
    # Monta as colunas da tabela da primeira fase do pedido de compra
    def montarTabelaPedidoCompra(self):
        consulta = "SELECT p.codigo,p.data,t.nome,p.status FROM pedido_compra p, tecnico t WHERE p.codigo = %i" %(0)
        self.pedidocombraModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
        
        self.pedidocombraModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        self.pedidocombraModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.pedidocombraModel.setHeaderData(1, Qt.Horizontal, "Data")
        self.pedidocombraModel.setHeaderData(2, Qt.Horizontal, QString.fromUtf8("Responsável"))
        self.pedidocombraModel.setHeaderData(3, Qt.Horizontal, "Status")

        self.pedidocombraModel.select()

        self.TabelaPedido.setModel(self.pedidocombraModel)
        self.TabelaPedido.show()
        self.TabelaPedido.resizeColumnsToContents()
        self.TabelaPedido.sortByColumn(0, Qt.AscendingOrder)

    # Monta as colunas da tabela da primeira fase do pedido de compra
    def montarTabelaEquipamentoPedido(self):
        consulta = "SELECT pe.id, pe.codigo, pe.nome, pe.descricao, pe.unidade, pe.entrega FROM pedido_equipamento pe, pedido_compra pc WHERE pe.codigo=%i AND pc.codigo = pe.codigo" %(0)
        self.equipamentopedidoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.equipamentopedidoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.equipamentopedidoModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.equipamentopedidoModel.setHeaderData(1, Qt.Horizontal, "Pedido")
        self.equipamentopedidoModel.setHeaderData(2, Qt.Horizontal, "Nome")
        self.equipamentopedidoModel.setHeaderData(3, Qt.Horizontal, "Unidade")
        self.equipamentopedidoModel.setHeaderData(4, Qt.Horizontal, QString.fromUtf8("entregar até"))
        self.equipamentopedidoModel.setHeaderData(5, Qt.Horizontal, QString.fromUtf8("Descrição"))

        self.equipamentopedidoModel.select()

        self.TabelaEquipamento.setModel(self.equipamentopedidoModel)
        self.TabelaEquipamento.show()
        self.TabelaEquipamento.resizeColumnsToContents()
        self.TabelaEquipamento.sortByColumn(0, Qt.AscendingOrder)

    # Insere a primeira fase do pedido no banco de dados
    def inserirPedido(self,obj):
        pedido = obj
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("INSERT INTO pedido_compra (codigo,data,id_usuario,id_tecnico,status)" "values (?,?,?,?,?)")
        query.addBindValue(pedido.id)
        query.addBindValue(pedido.data)
        query.addBindValue(pedido.id_usu)
        query.addBindValue(pedido.id_resp)
        query.addBindValue(pedido.status)
        query.exec_()      
        
        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(None, QString.fromUtf8("Erro na inserção do pedido"), err.text())
            return False
        else:
            QMessageBox.information(None, QString.fromUtf8("Inserção do Pedido"), QString.fromUtf8("Parte do pedido inserido com sucesso!\n Agora insira os equipamentos neste pedido, clicando no botão 'Equipamentos do pedido'." ))
            return True

    # Insere um pedido no banco de dados
    def inserirEquipamentoPedido(self,obj):
        equipedido = obj
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("INSERT INTO pedido_equipamento (codigo,nome,descricao,unidade,entrega)" "values (?,?,?,?,?)")
        query.addBindValue(equipedido.id_pedido)
        query.addBindValue(equipedido.nome)
        query.addBindValue(equipedido.descricao)
        query.addBindValue(equipedido.unidade)
        query.addBindValue(equipedido.entrega)
        query.exec_()

        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(None, QString.fromUtf8("Erro na inserção do equipamento no pedido"), err.text())
            return False
        else:
            QMessageBox.information(None, QString.fromUtf8("Inserção do equipamento no pedido"), QString.fromUtf8("Equipamento inserido no pedido com sucesso!" ))
            return True


    # Atualiza os dados da primeira fase do realizar pedido de compra
    def atualizarPedido(self,obj):
        pedido = obj
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("UPDATE pedido_compra SET data=?,id_usuario=?,id_tecnico=?,status=? WHERE codigo=?")
        query.addBindValue(pedido.data)
        query.addBindValue(pedido.id_usu)
        query.addBindValue(pedido.id_resp)
        query.addBindValue(pedido.status)
        query.addBindValue(pedido.id)
        query.exec_()      
        
        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(None, QString.fromUtf8("Erro na atualização do pedido"), err.text())
            return False
        else:
            QMessageBox.information(None, QString.fromUtf8("Atualização do Pedido"), QString.fromUtf8("Pedido atualizado com sucesso!"))
            return True

    # Atualiza os dados da segunda fase do realizar pedido de compra
    def atualizarEquipamentoPedido(self,obj):
        equipedido = obj
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("UPDATE pedido_equipamento SET nome=?,descricao=?,unidade=?,entrega=? WHERE id=?")
        query.addBindValue(equipedido.nome)
        query.addBindValue(equipedido.descricao)
        query.addBindValue(equipedido.unidade)
        query.addBindValue(equipedido.entrega)
        query.addBindValue(equipedido.id)
        query.exec_()

        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(None, QString.fromUtf8("Erro na atualização do equipamento do pedido"), err.text())
            return False
        else:
            QMessageBox.information(None, QString.fromUtf8("Atualização do Equipamento do Pedido"), QString.fromUtf8("Equipamento do pedido atualizado com sucesso!"))
            return True

    # captura o que o usuario escolheu no combobox e retorna a ID do responsavel para a ser utilizado na busca
    def Busca_Responsavel(self):
        responsavel = self.BuscaResponsavel.currentText()
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT id_tecnico FROM tecnico t WHERE t.nome=?")
        query.addBindValue(responsavel)
        query.exec_()

        while(query.next()):
            id_resp = query.value(0).toInt()

        return id_resp[0]

    # monta as colunas da tabela que será visualizada na tela
    def montar_tabela_de_busca_pedido(self, sql):

        consulta = sql
        self.pedidobuscaModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

        self.pedidobuscaModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.pedidobuscaModel.setHeaderData(0, Qt.Horizontal, QString.fromUtf8("Nº do Pedido"))
        self.pedidobuscaModel.setHeaderData(1, Qt.Horizontal, "Nome do equipamento")
        self.pedidobuscaModel.setHeaderData(2, Qt.Horizontal, "Data do pedido")
        self.pedidobuscaModel.setHeaderData(3, Qt.Horizontal, QString.fromUtf8("Responsavel"))
        self.pedidobuscaModel.setHeaderData(4, Qt.Horizontal, QString.fromUtf8("Status"))

        self.pedidobuscaModel.select()

        self.TabelaBusca.setModel(self.pedidobuscaModel)
        self.TabelaBusca.show()
        self.TabelaBusca.resizeColumnsToContents()
        self.TabelaBusca.sortByColumn(0, Qt.AscendingOrder)
        
    # Insere  os dados da primeira fase do pedido no banco de dados
    @pyqtSignature("")
    def on_btInserirPedido_clicked(self):
        try: 
            valid, pedido = self.validaPedido()
            if(valid):
                if(self.inserirPedido(pedido)):
                    self.abrirTabelaPedidoCompra(pedido)
                    self.EditPedidoEq.setText(str(pedido.id))
        except(TypeError):
            pass

    # Insere  os dados da segunda fase do pedido no banco de dados
    @pyqtSignature("")
    def on_btInserirEquipamento_clicked(self):
        try:
            valid, equipedido = self.validaEquipamento()
            if(valid):
                if(self.inserirEquipamentoPedido(equipedido)):
                    self.abrirTabelaEquipamentoPedido(equipedido)
        except(TypeError):
            pass

    # Atualiza os dados da primeira fase do pedido
    @pyqtSignature("")
    def on_btAtualizarPedido_clicked(self):
        try: 
            valid, pedido = self.validaPedido()
            if(valid):
                if(self.atualizarPedido(pedido)):
                    self.abrirTabelaPedidoCompra(pedido)
                    self.EditPedidoEq.setText(str(pedido.id))                    
        except(TypeError):
            pass

    # Altualiza os dados da segunda fase do pedido
    @pyqtSignature("")
    def on_btAtualizarEquipamento_clicked(self):
        try:
            valid, equipedido = self.validaEquipamento()
            if(valid):
                if(self.atualizarEquipamentoPedido(equipedido)):
                    self.abrirTabelaEquipamentoPedido(equipedido)
        except(TypeError):
            pass

    # Captura o nome do equipamento que o usuario digitou e monta um comando sql, para busca pela marca do equipamento
    @pyqtSignature("QString")
    def on_BuscaNome_textChanged(self, text):
        texto = '%'+text+'%'
        consulta = "select p.codigo, pe.nome, p.data, t.nome, p.status from pedido_compra p, tecnico t, pedido_equipamento pe where pe.nome like '%s'" % texto
        
        self.montar_tabela_de_busca_pedido(consulta)

    # Captura o codigo do pedido que o usuario digitou e monta um comando sql, para busca pela marca do equipamento
    @pyqtSignature("QString")
    def on_BuscaCodigo_textChanged(self, text):
        texto = int(str(text))
        consulta = "select p.codigo, pe.nome, p.data, t.nome, p.status from pedido_compra p, tecnico t, pedido_equipamento pe where p.codigo = %i AND t.id_tecnico = p.id_tecnico AND pe.codigo = p.codigo" % texto
        

        self.montar_tabela_de_busca_pedido(consulta)


    # Captura o status do pedido que o usuario digitou e monta um comando sql, para busca pela marca do equipamento
    @pyqtSignature("QString")
    def on_BuscaStatus_activated(self, text):
        texto = text
        consulta = "select p.codigo, pe.nome, p.data, t.nome, p.status from pedido_compra p, tecnico t, pedido_equipamento pe where p.status = '%s' AND t.id_tecnico = p.id_tecnico AND pe.codigo = p.codigo" % texto
        
        self.montar_tabela_de_busca_pedido(consulta)

    # captura o responsavel que o usuario escolhei e monta um select para buscar o pedido realizado
    @pyqtSignature("QString")
    def on_BuscaResponsavel_activated(self, text):
        texto= text

        query = QSqlQuery(self.bancoDeDados)
        query.prepare("SELECT id_tecnico FROM tecnico t WHERE t.nome=?")
        query.addBindValue(texto)
        query.exec_()

        while(query.next()):
            id_resp = query.value(0).toInt()

        consulta = "select p.codigo, pe.nome, p.data, t.nome, p.status from pedido_compra p, tecnico t, pedido_equipamento pe where p.id_tecnico = %i AND t.id_tecnico = p.id_tecnico AND pe.codigo = p.codigo" % id_resp[0]

        self.montar_tabela_de_busca_pedido(consulta)


    # Pega o numero do Pedido de compra e mostra os equipamentos do pedido
    @pyqtSignature("")
    def on_btMostrarEquip_clicked(self):

        try:
            pedido = self.EditPedido.text()
            

            if (pedido == ""):
                QMessageBox.warning(None, QString.fromUtf8("Aviso"), QString.fromUtf8("O campo Nº Pedido de compra está em branco!" ))
            else:
                id_pedido = int(pedido)
                consulta = "SELECT pe.id, pe.codigo, pe.nome, pe.unidade,  pe.entrega, pe.descricao FROM pedido_equipamento pe, pedido_compra pc WHERE pe.codigo=%i AND pc.codigo = pe.codigo" %(id_pedido)

                self.equipamentopedidoModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))

                self.equipamentopedidoModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

                self.equipamentopedidoModel.setHeaderData(0, Qt.Horizontal, "ID")
                self.equipamentopedidoModel.setHeaderData(1, Qt.Horizontal, "Pedido")
                self.equipamentopedidoModel.setHeaderData(2, Qt.Horizontal, "Nome")
                self.equipamentopedidoModel.setHeaderData(3, Qt.Horizontal, "Unidade")
                self.equipamentopedidoModel.setHeaderData(4, Qt.Horizontal, QString.fromUtf8("entregar até"))
                self.equipamentopedidoModel.setHeaderData(5, Qt.Horizontal, QString.fromUtf8("Descrição"))

                self.equipamentopedidoModel.select()

                self.TabelaEquipamento.setModel(self.equipamentopedidoModel)
                self.TabelaEquipamento.show()
                self.TabelaEquipamento.resizeColumnsToContents()
                self.TabelaEquipamento.sortByColumn(0, Qt.AscendingOrder)
        except:
            pass
    



#-& CLASSE &-#
class BaixaMaterial(QWidget, Ui_baixamaterial):
    def __init__(self, parent=None):
        super(BaixaMaterial, self).__init__(parent)
        self.setupUi(self)

        self.EditID.setVisible(False)
        self.id_usuario = self.addUsuarioLogado()

        self.bancoDeDados = QSqlDatabase.database("coopervap-bd")

        
        self.baixaModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        self.equipamentoBaixaModel = QSqlRelationalTableModel(self, self.bancoDeDados)
        self.abrirComboTecnico()
        self.abrirComboDepto()
        self.montarTabelas()

        self.mapeador = QDataWidgetMapper()
        self.mapeador.setModel(self.baixaModel)

        self.relacionalDelegate = QSqlRelationalDelegate(self.mapeador)
        self.mapeador.setItemDelegate(self.relacionalDelegate)

        self.mapeador.addMapping(self.EditID, 0)
        self.mapeador.addMapping(self.EditEquipamento, 1)
        self.mapeador.addMapping(self.spinQtd, 2)
        self.mapeador.addMapping(self.comboDepto, 3)
        self.mapeador.addMapping(self.EditData, 4)
        self.mapeador.addMapping(self.comboTecnico, 5)
        self.mapeador.addMapping(self.EditMotivo, 6)
        self.mapeador.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)

        self.connect(self.TabelaBaixa.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeador, SLOT("setCurrentModelIndex(QModelIndex)"))

        #- Mapeamento da tabela de busca de equipamento
        self.mapeador2 = QDataWidgetMapper()
        self.mapeador2.setModel(self.equipamentoBaixaModel)

        self.relacionalDelegate2 = QSqlRelationalDelegate(self.mapeador2)
        self.mapeador2.setItemDelegate(self.relacionalDelegate2)
        
        self.mapeador2.addMapping(self.EditEquipamento, 1)
        self.mapeador2.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)

        self.connect(self.TabelaBusca.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"), self.mapeador2, SLOT("setCurrentModelIndex(QModelIndex)"))

    # Captura do arquivo de login o usuario logado
    def addUsuarioLogado(self):
        file=open("data/login","r")
        texto=file.readlines()
        last_login=texto[len(texto)-1]
        id_usu=last_login[0]

        return id_usu
    
    # Preenche o Combo de Tecnicos
    def abrirComboTecnico(self):
        self.baixaModel.setRelation(1, QSqlRelation("TECNICO", "ID_TECNICO", "NOME"))
        relacaoModel = self.baixaModel.relationModel(1)

        self.comboTecnico.setModel(relacaoModel)
        self.comboTecnico.setModelColumn(relacaoModel.fieldIndex("NOME"))
        
        self.BuscaEquipResp.setModel(relacaoModel)
        self.BuscaEquipResp.setModelColumn(relacaoModel.fieldIndex("NOME"))

        self.BuscaBaixaResp.setModel(relacaoModel)
        self.BuscaBaixaResp.setModelColumn(relacaoModel.fieldIndex("NOME"))

    # Preenche o Combo de Departamentos
    def abrirComboDepto(self):
        self.baixaModel.setRelation(4, QSqlRelation("DEPARTAMENTO", "ID_DEPARTAMENTO", "NOME"))
        relacaoModel = self.baixaModel.relationModel(4)
        
        self.comboDepto.setModel(relacaoModel)
        self.comboDepto.setModelColumn(relacaoModel.fieldIndex("NOME"))
        
    # Monta as colunas das tabelas das abas de busca de equipamento e baixa
    def montarTabelas(self):
        # monta tabela equipamento
        consulta1 = "select e.id_equipamento, e.nome, e.marca_modelo, e.unidade, e.quantidade_inicial, e.estoque_min, t.nome from equipamento e , tecnico t where e.id_tecnico = t.id_tecnico AND e.id_equipamento = 0 order by e.id_equipamento"
        self.equipamentoBaixaModel.setQuery(QSqlQuery(consulta1, self.bancoDeDados))

        self.equipamentoBaixaModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.equipamentoBaixaModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.equipamentoBaixaModel.setHeaderData(1, Qt.Horizontal, "Nome")
        self.equipamentoBaixaModel.setHeaderData(2, Qt.Horizontal, "Marca")
        self.equipamentoBaixaModel.setHeaderData(3, Qt.Horizontal, "Unidade")
        self.equipamentoBaixaModel.setHeaderData(4, Qt.Horizontal, "Qtd")
        self.equipamentoBaixaModel.setHeaderData(5, Qt.Horizontal, "Estoque Min")
        self.equipamentoBaixaModel.setHeaderData(6, Qt.Horizontal, "Responsavel")

        self.equipamentoBaixaModel.select()

        self.TabelaBusca.setModel(self.equipamentoBaixaModel)
        self.TabelaBusca.show()
        self.TabelaBusca.resizeColumnsToContents()
        self.TabelaBusca.sortByColumn(0, Qt.AscendingOrder)

        # monta tabela baixa
        consulta2 = "SELECT b.id_baixa, b.equipamento, b.quantidade,d.nome,b.data,t.nome,b.motivo, u.nome FROM baixa_material_informatica b, departamento d, tecnico t, usuario u WHERE b.id_baixa =0"
        self.baixaModel.setQuery(QSqlQuery(consulta2, self.bancoDeDados))

        self.baixaModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.baixaModel.setHeaderData(0, Qt.Horizontal, "Codigo")
        self.baixaModel.setHeaderData(1, Qt.Horizontal, "Equipamento")
        self.baixaModel.setHeaderData(2, Qt.Horizontal, "Qtd")
        self.baixaModel.setHeaderData(3, Qt.Horizontal, "Departamento")
        self.baixaModel.setHeaderData(4, Qt.Horizontal, "Data")
        self.baixaModel.setHeaderData(5, Qt.Horizontal, "Responsavel")
        self.baixaModel.setHeaderData(6, Qt.Horizontal, "Motivo")
        self.baixaModel.setHeaderData(7, Qt.Horizontal, "Usuario")

        self.baixaModel.select()

        self.TabelaBaixa.setModel(self.baixaModel)
        self.TabelaBaixa.show()
        self.TabelaBaixa.resizeColumnsToContents()
        self.TabelaBaixa.sortByColumn(0, Qt.AscendingOrder)


    # Faz uma busca no banco de dados, o tipo de busca varia de acordo com o parametro sql
    def buscaIncremental(self, sql):
        consulta = sql
        if (consulta[7]=='e'):
            self.equipamentoBaixaModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
            self.equipamentoBaixaModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

            self.equipamentoBaixaModel.setHeaderData(0, Qt.Horizontal, "Codigo")
            self.equipamentoBaixaModel.setHeaderData(1, Qt.Horizontal, "Nome")
            self.equipamentoBaixaModel.setHeaderData(2, Qt.Horizontal, QString.fromUtf8("Marca"))
            self.equipamentoBaixaModel.setHeaderData(3, Qt.Horizontal, "Unidade")
            self.equipamentoBaixaModel.setHeaderData(4, Qt.Horizontal, "Qtd")
            self.equipamentoBaixaModel.setHeaderData(5, Qt.Horizontal, "Estoque Min")
            self.equipamentoBaixaModel.setHeaderData(6, Qt.Horizontal, "Responsavel")

            self.equipamentoBaixaModel.select()

            self.TabelaBusca.setModel(self.equipamentoBaixaModel)
            self.TabelaBusca.show()
            self.TabelaBusca.resizeColumnsToContents()
            self.TabelaBusca.sortByColumn(0, Qt.AscendingOrder)
        else:
            self.baixaModel.setQuery(QSqlQuery(consulta, self.bancoDeDados))
            self.baixaModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

            self.baixaModel.setHeaderData(0, Qt.Horizontal, "Codigo")
            self.baixaModel.setHeaderData(1, Qt.Horizontal, "Equipamento")
            self.baixaModel.setHeaderData(2, Qt.Horizontal, "Qtd")
            self.baixaModel.setHeaderData(3, Qt.Horizontal, "Departamento")
            self.baixaModel.setHeaderData(4, Qt.Horizontal, "Data")
            self.baixaModel.setHeaderData(5, Qt.Horizontal, "Responsavel")
            self.baixaModel.setHeaderData(6, Qt.Horizontal, "Motivo")
            self.baixaModel.setHeaderData(7, Qt.Horizontal, "Usuario")

            self.baixaModel.select()

            self.TabelaBaixa.setModel(self.baixaModel)
            self.TabelaBaixa.show()
            self.TabelaBaixa.resizeColumnsToContents()
            self.TabelaBaixa.sortByColumn(0, Qt.AscendingOrder)
            

    # Captura o ID do responsavel
    def capturaTecnico(self,tec):
        try:
            tecnico = tec
            query = QSqlQuery(self.bancoDeDados)
            query.prepare("SELECT id_tecnico FROM tecnico t WHERE t.nome=?")
            query.addBindValue(tecnico)
            query.exec_()

            while(query.next()):
                id_tec = query.value(0).toInt()

            return id_tec[0]
        except(UnboundLocalError):
            QMessageBox.warning(None, QString.fromUtf8("Erro"), QString.fromUtf8("Não foi escolhido nenhum tecnico!" ))

    # Captura o ID do departamento
    def capturaDepto(self):
        try:
            departamento = self.comboDepto.currentText()
            query = QSqlQuery(self.bancoDeDados)
            query.prepare("SELECT id_departamento FROM departamento d WHERE d.nome=?")
            query.addBindValue(departamento)
            query.exec_()

            while(query.next()):
                id_depto = query.value(0).toInt()

            return id_depto[0]
        except(UnboundLocalError):
            QMessageBox.warning(None, QString.fromUtf8("Erro"), QString.fromUtf8("Não foi escolhido nenhum departamento!" ))

    # Valida os dados da tela de baixa no estoque
    def validaBaixa(self):
        if(self.EditID.text()==""):
            id = self.EditID.text()
        else:
            id = int(self.EditID.text())
            
        equipamento = self.EditEquipamento.text()
        qtd = self.spinQtd.value()
        data = self.EditData.text()
        tecnico = self.comboTecnico.currentText()
        id_tec = self.capturaTecnico(tecnico)
        id_depto = self.capturaDepto()
        motivo = self.EditMotivo.toPlainText()
        id_usu = self.id_usuario

        if (len(motivo)>400):
            QMessageBox.warning(self, QString.fromUtf8("Erro"), QString.fromUtf8("O campo motivo tem mais que 400 caracteres!" ))
            return False, None
        elif(equipamento=='' or qtd == 0 or data == '//' or motivo == ''):
            QMessageBox.warning(self, QString.fromUtf8("Erro"), QString.fromUtf8("Algum desses campos está em branco:\n-Equipamento\n-Quantidade\n-Data\n-Motivos" ))
            return False, None
        else:
            baixa = baixaMaterial(equipamento,qtd,id_depto,data,id_tec,motivo,id_usu,id)
            return True, baixa

    def limpar(self):
        self.EditID.clear()
        self.EditEquipamento.clear()
        self.spinQtd.clear()
        self.EditData.clear()
        self.EditMotivo.clear()

    # Insere os dados no banco
    def insere(self,obj):
        baixa=obj

        query = QSqlQuery(self.bancoDeDados)
        query.prepare("INSERT INTO baixa_material_informatica (equipamento,quantidade,id_departamento,data,id_tecnico,motivo,id_usuario)" "VALUES (?,?,?,?,?,?,?)")
        query.addBindValue(baixa.equipamento)
        query.addBindValue(baixa.qtd)
        query.addBindValue(baixa.id_depto)
        query.addBindValue(baixa.data)
        query.addBindValue(baixa.id_tec)
        query.addBindValue(baixa.motivo)
        query.addBindValue(baixa.id_usu)
        query.exec_()

        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(self, "Erro no cadastro do baixa", err.text())
            return False
        else:
            QMessageBox.information(self, "Cadastro de Baixa", "Baixa cadastrada com sucesso!" )
            return True
        
    # Atualiza os dados no banco de dados
    def atualiza(self,obj):
        baixa = obj
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("UPDATE baixa_material_informatica SET equipamento=?,quantidade=?,id_departamento=?,data=?,id_tecnico=?,motivo=?,id_usuario=? WHERE id_baixa=?")
        query.addBindValue(baixa.equipamento)
        query.addBindValue(baixa.qtd)
        query.addBindValue(baixa.id_depto)
        query.addBindValue(baixa.data)
        query.addBindValue(baixa.id_tec)
        query.addBindValue(baixa.motivo)
        query.addBindValue(baixa.id_usu)
        query.addBindValue(baixa.id)
        query.exec_()

        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(self, QString.fromUtf8("Erro na atualização da baixa"), err.text())
            return False
        else:
            QMessageBox.information(self, QString.fromUtf8("Atualização da Baixa"), QString.fromUtf8("Baixa atualizada com sucesso!"))
            return True
            
    # Deleta os dados no banco de dados
    def deleta(self,obj):
        baixa = obj
        query = QSqlQuery(self.bancoDeDados)
        query.prepare("DELETE FROM baixa_material_informatica WHERE id_baixa=?")
        query.addBindValue(baixa.id)
        query.exec_()

        if (query.lastError().type() != QSqlError.NoError):
            err = query.lastError()
            QMessageBox.critical(self, QString.fromUtf8("Erro na deleção da baixa"), err.text())
            return False
        else:
            QMessageBox.information(self, QString.fromUtf8("Deleção da Baixa"), QString.fromUtf8("Baixa deletada com sucesso!"))
            return True


    # Insere os dados no banco, se os campos estiverem validos
    @pyqtSignature("")
    def on_btInserirBaixa_clicked(self):        
        valido, baixa = self.validaBaixa()
        if(valido):
            if(self.insere(baixa)):
                self.limpar()

    # Atualiza os dados no banco, se os campos estiverem validos
    @pyqtSignature("")
    def on_btAtualizarBaixa_clicked(self):
        valido, baixa = self.validaBaixa()
        if(valido):
            if(self.atualiza(baixa)):
                self.limpar()

    # Deleta os dados no banco, se os campos estiverem validos
    @pyqtSignature("")
    def on_btDeletarBaixa_clicked(self):        
        valido, baixa = self.validaBaixa()
        if(valido):
            if(self.deleta(baixa)):
                self.limpar()


    # Capitura o que o usuario digitou e monta um comando sql, para busca pelo nome do equipamento
    @pyqtSignature("QString")
    def on_BuscaEquipNome_textChanged(self, text):
        texto = '%'+text+'%'
        consulta = "select e.id_equipamento, e.nome, e.marca_modelo, e.unidade, e.quantidade_inicial, e.estoque_min, t.nome from equipamento e , tecnico t where e.id_tecnico = t.id_tecnico and e.nome like '%s' order by e.id_equipamento" % texto
        
        self.buscaIncremental(consulta)

    # Capitura o que o usuario escolheu no combobox e monta um comando sql, para busca pelo nome do tecnico responsavel pelo equipamento
    @pyqtSignature("QString")
    def on_BuscaEquipResp_activated(self, text):
        texto = text
        id_tec = self.capturaTecnico(texto)
        consulta = "select e.id_equipamento, e.nome, e.marca_modelo, e.unidade, e.quantidade_inicial, e.estoque_min, t.nome from equipamento e , tecnico t where e.id_tecnico = t.id_tecnico and e.id_tecnico = %i order by e.id_equipamento" % id_tec

        self.buscaIncremental(consulta)
        
    # Capitura o que o usuario digitou e monta um comando sql, para busca pelo nome do equipamento que consta na baixa
    @pyqtSignature("QString")
    def on_BuscaBaixaNome_textChanged(self, text):
        texto = '%'+text+'%'
        consulta = "SELECT baixa.id_baixa, baixa.equipamento, baixa.quantidade,d.nome,baixa.data,t.nome,baixa.motivo, u.nome FROM baixa_material_informatica baixa, departamento d, tecnico t, usuario u WHERE baixa.id_tecnico = t.id_tecnico AND baixa.id_departamento = d.id_departamento AND baixa.id_usuario  = u.id_usuario AND baixa.equipamento LIKE '%s' order by baixa.id_baixa" % texto
        
        self.buscaIncremental(consulta)

    # Capitura o que o usuario escolheu no combobox e monta um comando sql, para busca pelo nome do tecnico responsavel pela baixa
    @pyqtSignature("QString")
    def on_BuscaBaixaResp_activated(self, text):
        texto = text
        id_tec = self.capturaTecnico(texto)
        consulta = "SELECT baixa.id_baixa, baixa.equipamento, baixa.quantidade,d.nome,baixa.data,t.nome,baixa.motivo,u.nome FROM baixa_material_informatica baixa, departamento d, tecnico t, usuario u WHERE baixa.id_tecnico = t.id_tecnico AND baixa.id_departamento = d.id_departamento AND baixa.id_usuario  = u.id_usuario AND baixa.id_tecnico = %i order by baixa.id_baixa;" % id_tec

        self.buscaIncremental(consulta)
