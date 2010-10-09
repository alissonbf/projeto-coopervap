#!/bin/env python                         
# -*- coding: utf-8 -*-             

## [Ficha]##################################################
#	                                                       #					           
#  Nome: Modulo main				                       #
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
#  Script principal.                                       #
#					                                       #
############################################################


import sys
from PyQt4.QtCore import *                 
from PyQt4.QtGui import *                  
from View import *     

if __name__ == "__main__":
    app = QApplication(sys.argv)      
    prin = Principal()
    prin.showMaximized()
    app.exec_()
    
