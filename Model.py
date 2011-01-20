#!/bin/env python                         
# -*- coding: utf-8 -*-             

## [Ficha]##################################################
#	                                                   #					           
#  Nome: Modulo Model				           #
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
#  Este modulo contem as classes dos objetos que são       #
#  usados pelo programa.                                   #
#					                   #
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
    def __init__(self, nome, marca, unidade, quantidade, estoque, id_resp, usuario, id_equip=None):
        self.nome = nome
        self.marca = marca
        self.unidade = unidade
        self.quantidade = quantidade
        self.estoque = estoque
        self.id_equip = id_equip
        self.id_resp = id_resp
        self.usuario = usuario

class departamento():
    def __init__(self,nome,centro,id=None):
        self.nome = nome
        self.centro = centro
        self.id = id

class tecnico():
    def __init__(self,nome,funcao,departamento,status,usuario,id=None):
        self.nome=nome
        self.funcao=funcao
        self.departamento=departamento
        self.status=status
        self.usuario=usuario
        self.id=id

class pedidocompra():
    def __init__(self,data,status,id_usu,id_resp,id=None):
        self.data=data
        self.status=status
        self.id_usu=id_usu
        self.id_resp=id_resp
        self.id=id


class equipamentopedido():
    def __init__(self,nome,descricao,unidade,entrega,id_pedido,id=None):
        self.nome=nome
        self.descricao=descricao
        self.unidade=unidade
        self.entrega=entrega
        self.id_pedido=id_pedido
        self.id=id

class baixaMaterial():
    def __init__(self, equipamento, qtd,id_depto,data,id_tec,motivo,id_usu,id=None):
        self.equipamento = equipamento
        self.qtd = qtd
        self.id_depto = id_depto
        self.data = data
        self.id_tec = id_tec
        self.motivo = motivo
        self.id_usu = id_usu
        self.id = id
        
    
       
        
