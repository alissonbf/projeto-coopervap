.. _controller:


*****************
Modulo Controller
*****************
                 
Escrito por: 

* Alisson Barbosa Ferreira, alissonbf@gmail.com                   
* Alisson Oliveira Ferreira, linukiss@gmail.com                  
* Victor Hugo Neiva, victorhugoneiva@gmail.com                          
* Wesley Junior                              
                                                          
Criado em: 

- 30/08/2010			                       
						                                   
Ultima atualização: 

- 21/12/2010		                   
						                                   
Descrição

-  Este modulo contem os metodos que se comunicam com o banco de dados e que efetivão as regras de negocio


Importações
===========

Sys
---

Usar metodos para comunicar com o sistema::

    import sys


Pyqt4.QtCore
------------

Este modulo contém as classes centrais não-GUI, incluindo o ciclo de eventos e um sinal do Qt e do mecanismo de slot. Também inclui abstrações independentes de plataforma para Unicode, threads, arquivos mapeados, memória compartilhada, as expressões regulares, e de usuário e configurações do aplicativo, saiba mais sobre Pyqt4.QtCore `aqui <http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html>`_::

    from PyQt4.QtCore import *


PyQt4.QtGui
-----------

Este modulo contém a maioria das classes de GUI, saiba mais sobre PyQt4.QtGui `aqui <http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html/>`_::
                 
    from PyQt4.QtGui import * 

PyQt4.QtSql
-----------

Este modulo ajuda a fornecer a integração de banco de dados transparente para seus aplicativos PyQt, saiba mais sobre PyQt4.QtSql `aqui <http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qtsql.html/>`_::
                 
    from PyQt4.QtSql import *



Metodos
=======

abrirBancoDeDados
-----------------

Abre uma conexão com o banco de dados, que será usado pela sua aplicação::
    
    abrirBancoDeDados(self)


fecharBancoDeDados
------------------

Fecha a conexão com o banco de dados, que sua aplicação estava usando::

    fecharBancoDeDados(self,bancoDeDados)

:ref:`bancoDeDados`: Parâmetro que recebe a variavel de conexão do banco de dados


driverPostgreOK
---------------

Testa de o computador tem o driver do PostgreSQL instalado::

    driverPostgreOK(self)

    return QSqlDatabase.isDriverAvailable("QPSQL")

:ref:`Return`: Este metodo retorna True se o driver estiver instalado no computador, senão retorna False 












