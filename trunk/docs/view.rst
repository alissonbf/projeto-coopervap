.. _view:


************
Modulo View
************
                 
Escrito por: 

* Alisson Barbosa Ferreira, alissonbf@gmail.com                   
* Alisson Oliveira Ferreira, linukiss@gmail.com                  
* Victor Hugo Neiva, victorhugoneiva@gmail.com                          
* Wesley Junior, www.wesley@gmail.com                              
                                                          
Criado em: 

- 30/08/2010			                       
						                                   
Ultima atualização: 

- 06/10/2010		                   
						                                   
Descrição

- Este modulo contém as classes que se comunicam com as interfaces graficas e da vida aos seus botões        

.. _cadatrousuario:

----------------------
Classe CadastroUsuario
----------------------


Importações
===========

Sys
---

Usar metodos para comunicar com o sistema::

    import sys

Re
--

Este módulo oferece uma expressão regular correspondente operações semelhantes às encontradas em Perl. Ambos os padrões e sequências a serem pesquisados podem ser sequências de caracteres Unicode como sequências de 8 bits, saiba mais sobre re `aqui <http://docs.python.org/library/re.html>`_::

    import re


Pyqt4.QtCore
------------

Este modulo contém as classes centrais não-GUI, incluindo o ciclo de eventos e um sinal do Qt e do mecanismo de slot. Também inclui abstrações independentes de plataforma para Unicode, threads, arquivos mapeados, memória compartilhada, as expressões regulares, e de usuário e configurações do aplicativo, saiba mais sobre Pyqt4.QtCore `aqui <http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html>`_::

    from PyQt4.QtCore import *


PyQt4.QtGui
-----------

Este modulo contém a maioria das classes de GUI, saiba mais sobre PyQt4.QtGui `aqui <http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html/>`_::
                 
    from PyQt4.QtGui import *                  


telas.GuiCadastroUsuario
------------------------

No pacote telas, saiba mais sobre pacotes `aqui <http://www.python.org.br/wiki/ModulosPacotes/>`_, existe um modulo que contem os dados da tela de cadastro de usuario. Neste modulo estão todas as declarações dos componentes das telas, como tamanho da janela, quais botões vão estar na tela, etc. Este modulo foi gerado com o comando `pyuic4 <http://www.opendocs.net/pyqt/pyqt4.html#pyuic4/>`_::

    from telas.GuiCadastroUsuario import *

Controller
----------

Este modulo contem os metodos que se comunicam com o banco de dados e que efetivão as regras de negocio::

    from Controller import *

Model
-----

Este modulo contem as classes dos objetos que são usados pelo programa::

    from Model import *


.. _metodos:


Metodos
=======

__init__
--------

Metodo que é executado quando o classe banco é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


abrirTabelaUsuario
------------------

Metodo que traz todos os usuarios cadastrados no sistema::

    abrirTabelaUsuario(self)   


setIncluindo
------------

Ativa o botão de salvar e cancelar, se o status for True::

    setIncluindo(self,status)

:ref:`status`: Parâmetro que recebe um tipo de dado boolean


setEditando
-----------

Aiva o botão de salvar e cancelar, se o status for True::

    setEditando(self,status)

:ref:`status`: Parâmetro que recebe um tipo de dado boolean

valido
------

Valida os dados, digitados pelo usuario::

    valido(self)

    return valor,usu

:ref:`return`: Este metodo retorna uma variavel valor, que pode ser True se todos os campos digitados forem validos, senão forem ela fica com o valor False. O metodo também retorna o objeto usu, que é uma instancia da classe usuario, criada se todos os campos forem validos. 

inclusao
--------

Insere os dados do usuario no banco::

    inclusao(self,usu)
    
    return False
    
    return True

:ref:`usu`: Objeto contendo os dados do usuario que será cadastrado

:ref:`return`: Este metodo retorna True, se o usuario for inserido com sucesso, senão retorna False

atualizacao
-----------

Atualiza os dados do usuario que estão no banco::

    atualizacao(self,usu)

    return False
    
    return True

:ref:`usu`: Objeto contendo os dados do usuario que será atualizado

:ref:`return`: Este metodo retorna True, se o usuario for atualizado com sucesso, senão retorna False

destrava
--------

Ativa todos os campos de inserção de dados::

    destrava(self)


on_Novo_clicked
---------------

Cria uma nova linha na tabela e limpa o formulario de departamentos::

    @pyqtSignature("")        
    on_Novo_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_Salvar_clicked
-----------------

Salva os dados no banco de dados depois de validados::

    @pyqtSignature("")        
    on_Salvar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_Deletar_clicked
------------------

Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma::

    @pyqtSignature("")        
    on_Deletar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_EditNome_textEdited
----------------------

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditNome_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget



on_EditEmail_textEdited
-----------------------

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditEmail_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget



on_EditFuncao_textEdited
------------------------

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditFuncao_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget


on_EditLogin_textEdited
-----------------------

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditLogin_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget


on_ComboStatus_activated
------------------------

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_ComboStatus_activated(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget


on_Fechar_clicked
------------------------

Fecha a janela::

    @pyqtSignature("")        
    on_Fechar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


