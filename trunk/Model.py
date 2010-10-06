#!/bin/env python                         
# -*- coding: utf-8 -*-             

## [Ficha]##################################################
#	                                                       #					           
#  Nome: Modulo Model				                       #
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
#  Este script contem as classes dos objetos que são       #
#  usados pelo programa.                                   #
#					                                       #
############################################################


class usuario():
    def __init__(self, nome,email,funcao,status,login,senha, id_usu=None):
        self.nome = nome
        self.email = email
        self.funcao = funcao
        self.status = status
        self.login = login
        self.senha = senha
        self.id = id_usu
       
        
