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
#  Ultima atualizacao: 21/12/2010		                   #
#						                                   #
#  [Descricao]##############################################
#					                                       #
#  Este modulo contem as classes dos objetos que são       #
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

class equipamento():
    def __init__(self, nome, marca, unidade, quantidade, estoque, id_resp, usuario, id_equip=None, patrimonio=None):
        self.nome = nome
        self.marca = marca
        self.unidade = unidade
        self.quantidade = quantidade
        self.patrimonio = patrimonio
        self.estoque = estoque
        self.id_equip = id_equip
        self.id_resp = id_resp
        self.usuario = usuario

class departamento():
    def __init__(self,nome,centro,id=None):
        self.nome = nome
        self.centro = centro
        self.id = id
       
        
