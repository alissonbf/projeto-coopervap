#!/bin/env python                         
# -*- coding: utf-8 -*-             

## [Ficha]##################################################
#	                                                   #					           
#  Nome: Modulo Controler			           #
#  Escrito por: Alisson Barbosa Ferreira                   #
#               Alisson Oliveira Ferreira                  #
#               Victor Hugo Neiva                          #
#               Wesley Junior                              #
#                                                          #
#  Criado em: 30/08/2010			           #
#						           #
#  Ultima atualizacao: 06/10/2010		           #
#						           #
#  [Descricao]##############################################
#					                   #
#  Este modulo contem os metodos que se comunicam com      #
#  o banco de dados e que efetivão as regras de negocio.   #
#					                   #
############################################################

import sys
from PyQt4.QtCore import *                 
from PyQt4.QtGui import *                  
from PyQt4.QtSql import *

def abrirBancoDeDados(self):
    if (driverPostgreOK(self)):
        # Estabelecer conexao com o banco de dados
        bancoDeDados = QSqlDatabase.addDatabase("QPSQL","coopervap-bd")        
        bancoDeDados.setHostName("localhost")
        bancoDeDados.setDatabaseName("coopervap")
        bancoDeDados.setPassword("postgres")
        bancoDeDados.setUserName("postgres")
        bancoDeDados.open()        
    else:
        QMessageBox.critical(None, "Driver Postgre", QString.fromUtf8("Driver Não Encontrado"))       
    

def fecharBancoDeDados(self,bancoDeDados):
    bancoDeDados = bancoDeDados
    # Fechar conexao com o banco de dados
    bancoDeDados.close()
    QSqlDatabase.removeDatabase("coopervap-bd")

def driverPostgreOK(self):
    return QSqlDatabase.isDriverAvailable("QPSQL")

