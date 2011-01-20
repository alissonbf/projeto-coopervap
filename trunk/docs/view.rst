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

- 22/12/2010		                   
						                                   
Descrição

- Este modulo contém as classes que se comunicam com as interfaces graficas e da vida aos seus botões        


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


.. _cadatrousuario:


Classes
=======

CadastroUsuario
---------------

.. _metodos:

-------
Metodos
-------

__init__
********

Metodo que é executado quando o classe banco é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


abrirTabelaUsuario
******************

Metodo que traz todos os usuarios cadastrados no sistema::

    abrirTabelaUsuario(self)   


setIncluindo
************

Ativa o botão de salvar e cancelar, se o status for True::

    setIncluindo(self,status)

:ref:`status`: Parâmetro que recebe um tipo de dado boolean


setEditando
***********

Aiva o botão de salvar e cancelar, se o status for True::

    setEditando(self,status)

:ref:`status`: Parâmetro que recebe um tipo de dado boolean

valido
******

Valida os dados, digitados pelo usuario::

    valido(self)

    return valor,usu

:ref:`return`: Este metodo retorna uma variavel valor, que pode ser True se todos os campos digitados forem validos, senão forem ela fica com o valor False. O metodo também retorna o objeto usu, que é uma instancia da classe usuario, criada se todos os campos forem validos. 

inclusao
********

Insere os dados do usuario no banco::

    inclusao(self,usu)
    
    return False
    
    return True

:ref:`usu`: Objeto contendo os dados do usuario que será cadastrado

:ref:`return`: Este metodo retorna True, se o usuario for inserido com sucesso, senão retorna False

atualizacao
***********

Atualiza os dados do usuario que estão no banco::

    atualizacao(self,usu)

    return False
    
    return True

:ref:`usu`: Objeto contendo os dados do usuario que será atualizado

:ref:`return`: Este metodo retorna True, se o usuario for atualizado com sucesso, senão retorna False

destrava
********

Ativa todos os campos de inserção de dados::

    destrava(self)


on_Novo_clicked
***************

Cria uma nova linha na tabela e limpa o formulario de departamentos::

    @pyqtSignature("")        
    on_Novo_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_Salvar_clicked
*****************

Salva os dados no banco de dados depois de validados::

    @pyqtSignature("")        
    on_Salvar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_Deletar_clicked
******************

Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma::

    @pyqtSignature("")        
    on_Deletar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_EditNome_textEdited
**********************

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditNome_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget



on_EditEmail_textEdited
***********************

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditEmail_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget



on_EditFuncao_textEdited
************************

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditFuncao_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget


on_EditLogin_textEdited
***********************

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_EditLogin_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget


on_ComboStatus_activated
************************

Desativa os campos de texto de senha e confirmar senha::

    @pyqtSignature("QString")        
    on_ComboStatus_activated(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

:ref:`text`: texto que esta no widget


on_Fechar_clicked
*****************

Fecha a janela::

    @pyqtSignature("")        
    on_Fechar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


CadastroDepartamento
--------------------

-------
Metodos
-------

__init__
********

Metodo que é executado quando o classe banco é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


abrirTabelaDepartamento
***********************
Preence a tabela com os dados que estão no banco de dados::

    abrirTabelaDepartamento(self)

setIncluindo
************

Ativa o botão de salvar e  cancelar, se o status for True::

    setIncluindo(self,status)

:ref:`status`: variavel do tipo booleano, True se o usuario estiver incluindo ou False se não estiver incluindo.

setEditando
***********

Ativa o botão de salvar e cancelar, se o status for True::

    setEditando(self,status)

:ref:`status`: variavel do tipo booleano, True se o usuario estiver editando ou False se não estiver editando.


Valido
******

Valida todos os campos da tela de departamento::

    Valido(self)

:ref:`return`: Este metodo retorna uma variavel valor, que pode ser True se todos os campos digitados forem validos, senão forem ela fica com o valor False. O metodo também retorna o objeto departamento, que é uma instancia da classe departamento, criada se todos os campos forem validos. 

atualiza
********

Atualiza os dados no banco de dados::

    atualiza(self,obj)

:ref:`obj`: Objeto da instanciado da classe departamento.

insere
********

Insere os dados no banco de dados::

    insere(self,obj)

:ref:`obj`: Objeto da instanciado da classe departamento.


on_btSalvar_clicked
*******************

Insere ou atualiza os dados no banco de dados::

    @pyqtSignature("")        
    on_btSalvar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_btCancelar_clicked
*********************

Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma.::

    @pyqtSignature("")        
    on_btCancelar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_EditNome_textEdited
**********************

Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado::

    @pyqtSignature("QString")        
    on_EditNome_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_EditCentroCusto_textEdited
*****************************

Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado::

    @pyqtSignature("QString")        
    on_EditCentroCusto_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget
 enviará>.

CadastroTecnico
---------------

-------
Metodos
-------

__init__
********

Metodo que é executado quando o classe banco é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


abrirTabelaTecnico
******************
Preence a tabela com os dados que estão no banco de dados::

    abrirTabelaTecnico(self)


abrirComboDepto
***************

Preenche o Combo de Departamentos::

    abrirComboDepto(self)


addUsuarioLogado
****************

Captura do arquivo de login o usuario logado::

    addUsuarioLogado(self)

:ref:`return`: Retorna o id co usuario que esta logado


setIncluindo
************

Ativa o botão de salvar e  cancelar, se o status for True::

    setIncluindo(self,status)

:ref:`status`: variavel do tipo booleano, True se o usuario estiver incluindo ou False se não estiver incluindo.


setEditando
***********

Ativa o botão de salvar e cancelar, se o status for True::

    setEditando(self,status)

:ref:`status`: variavel do tipo booleano, True se o usuario estiver editando ou False se não estiver editando.



Valido
******

Valida todos os campos da tela de tecnico::

    Valido(self)

:ref:`return`: Este metodo retorna uma variavel valor, que pode ser True se todos os campos digitados forem validos, senão forem ela fica com o valor False. O metodo também retorna o objeto tecnico, que é uma instancia da classe tecnico, criada se todos os campos forem validos. 

atualiza
********

Atualiza os dados no banco de dados::

    atualiza(self,obj)

:ref:`obj`: Objeto da instanciado da classe tecnico.

insere
********

Insere os dados no banco de dados::

    insere(self,obj)

:ref:`obj`: Objeto da instanciado da classe tecnico.


on_btSalvar_clicked
*******************

Insere ou atualiza os dados no banco de dados::

    @pyqtSignature("")        
    on_btSalvar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_btCancelar_clicked
*********************

Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma.::

    @pyqtSignature("")        
    on_btCancelar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_EditNome_textEdited
**********************

Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado::

    @pyqtSignature("QString")        
    on_EditNome_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_EditFuncao_textEdited
************************

Abilita os botões de salvar e cancelar, quando um line edit começa a ser editado::

    @pyqtSignature("QString")        
    on_EditFuncao_textEdited(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.



CadastroEquipamento
-------------------

-------
Metodos
-------

__init__
********

Metodo que é executado quando o classe banco é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


abrirTabelaTecnico
******************

Preence a tabela com os dados que estão no banco de dados::

    abrirTabelaEquipamento(self)


abrirComboResponsavel
*********************

Preenche o Combo de Departamentos::

    abrirComboResponsavel(self)

addUsuarioLogado
****************

Captura do arquivo de login o usuario logado::

    addUsuarioLogado(self)

:ref:`return`: Retorna o id co usuario que esta logado


validaEquipamento
*****************

Valida todos os campos da tela de equipamento::

    validaEquipamento(self)

:ref:`return`: Retorna o id co usuario que esta logado

atualizaEquipamento
*******************

Atualiza os dados no banco de dados::

    atualizaEquipamento(self, equip)

:ref:`return`: Este metodo retorna uma variavel valor, que pode ser True se todos os campos digitados forem validos, senão forem ela fica com o valor False. O metodo também retorna o objeto equip, que é uma instancia da classe equipamento, criada se todos os campos forem validos. 

inserirEquipamento
******************

Insere os dados no banco de dados::

    inserirEquipamento(self, equip)

:ref:`obj`: Objeto da instanciado da classe tecnico.


capturaResponsavel
******************

Captura o ID do responsavel::

    capturaResponsavel(self)

:ref:`return`: Este metodo retorna o id do responsavel pelo equipamento.


buscaIncremental
****************

Faz uma busca no banco de dados, o tipo de busca varia de acordo com o parametro sql::

    buscaIncremental(self, sql)

:ref:`sql`: Instrução sql que define que tipo de busca o metodo vai executar.


on_btSalvar_clicked
*******************

Insere ou atualiza os dados no banco de dados::

    @pyqtSignature("")        
    on_btSalvar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_btCancelar_clicked
*********************

Desabilita os botões de salvar e cancelar, limpa os campos e se existe uma linha vazia na coluna, limpa a mesma.::

    @pyqtSignature("")        
    on_btCancelar_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_PesquisaNome_textChanged
***************************

Capitura o que o usuario digitou e monta um comando sql, para busca pelo nome do equipamento::

    @pyqtSignature("QString")        
    on_PesquisaNome_textChanged(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.

on_PesquisaMarca_textChanged
****************************

Capitura o que o usuario digitou e monta um comando sql, para busca pela marca do equipamento::

    @pyqtSignature("QString")        
    on_PesquisaMarca_textChanged(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


PedidoDeCompra
--------------

-------
Metodos
-------

__init__
********

Metodo que é executado quando o classe é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


addUsuarioLogado
****************

Captura do arquivo de login o usuario logado::

    addUsuarioLogado(self)

:ref:`return id_usu`: Retorna o id do usuario logado


abrirComboResponsavel
*********************

Preenche o Combo de Responsaveis::

    abrirComboResponsavel(self)


capturaResponsavel
******************

Captura o ID do responsavel::

    capturaResponsavel(self)

:ref:`return id_resp[0]`: Retorna o id do responsavel


validaPedido
************

Valida os dados da primeira etapa do pedido de compra::

    validaPedido(self)


validaEquipamento
*****************

Valida os dados da primeira etapa do pedido de compra::

    validaEquipamento(self)


abrirTabelaPedidoCompra
***********************

Mostra o pedido que acabou de ser inserido::

    abrirTabelaPedidoCompra(self,obj)

:ref:`obj`: Objeto da classe pedidocompra


abrirTabelaEquipamentoPedido
****************************

Mostra o equipamento que acabou de ser inserido no pedido::

    abrirTabelaEquipamentoPedido(self,obj)

:ref:`obj`: Objeto da classe equipamentopedido


montarTabelaPedidoCompra
************************

Monta as colunas da tabela da primeira fase do pedido de compra::

    montarTabelaPedidoCompra(self)


montarTabelaEquipamentoPedido
*****************************

Monta as colunas da tabela da primeira fase do pedido de compra::

    montarTabelaEquipamentoPedido(self)


inserirPedido
*************

Insere a primeira fase do pedido no banco de dados::

    inserirPedido(self,obj)

:ref:`obj`: Objeto da classe pedidocompra


inserirEquipamentoPedido
************************

Insere um pedido no banco de dados::

    inserirEquipamentoPedido(self,obj)

:ref:`obj`: Objeto da classe equipamentopedido


atualizarPedido
***************

Atualiza os dados da primeira fase do realizar pedido de compra::

    atualizarPedido(self,obj)

:ref:`obj`: Objeto da classe pedidocompra


atualizarEquipamentoPedido
**************************

Atualiza os dados da segunda fase do realizar pedido de compra::

    atualizarEquipamentoPedido(self,obj)

:ref:`obj`: Objeto da classe equipamentopedido


Busca_Responsavel
*****************

captura o que o usuario escolheu no combobox e retorna a ID do responsavel para a ser utilizado na busca::

    Busca_Responsavel(self)

:ref:`return id_resp[0]`: Retorna o id do responsavel


montar_tabela_de_busca_pedido
*****************************

monta as colunas da tabela que será visualizada na tela::

    montar_tabela_de_busca_pedido(self, sql)

:ref:`sql`: Instrução sql que define que tipo de busca o metodo vai executar.


on_btInserirPedido_clicked
**************************

Insere  os dados da primeira fase do pedido no banco de dados::

    @pyqtSignature("")
    on_btInserirPedido_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>.


on_btInserirEquipamento_clicked
*******************************

Insere  os dados da segunda fase do pedido no banco de dados::

    @pyqtSignature("")
    on_btInserirEquipamento_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>


on_btAtualizarPedido_clicked
****************************

Atualiza os dados da primeira fase do pedido::

    @pyqtSignature("")
    on_btAtualizarPedido_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>


on_btAtualizarEquipamento_clicked
*********************************

Altualiza os dados da segunda fase do pedido::

    @pyqtSignature("")
    on_btAtualizarEquipamento_clicked(self)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>


on_BuscaNome_textChanged
************************

Captura o nome do equipamento que o usuario digitou e monta um comando sql, para busca pela marca do equipamento::

    @pyqtSignature("QString")
    on_BuscaNome_textChanged(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>



on_BuscaCodigo_textChanged
**************************

Captura o codigo do pedido que o usuario digitou e monta um comando sql, para busca pela marca do equipamento::

    @pyqtSignature("QString")
    on_BuscaCodigo_textChanged(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>


on_BuscaStatus_activated
************************

Captura o status do pedido que o usuario digitou e monta um comando sql, para busca pela marca do equipamento::

    @pyqtSignature("QString")
    on_BuscaStatus_activated(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>

on_BuscaResponsavel_activated
*****************************

captura o responsavel que o usuario escolhei e monta um select para buscar o pedido realizado::

    @pyqtSignature("QString")
    on_BuscaResponsavel_activated(self, text)

:ref:`@pyqtSignature("")`: Assinatura padão do python, que faz com que este metodo seja conectado ao widget "Novo" automaticamente. Todo metodo que irá conectar automaticamente ao widget, além de ter a assinatura padrão do python, deverá seguir o seguinte padrão em seu nome, on_<nome do widget>_<sinal que o widget enviará>


on_btMostrarEquip_clicked
*************************

Pega o numero do Pedido de compra e mostra os equipamentos do pedido::

    @pyqtSignature("")
    on_btMostrarEquip_clicked(self)


BaixaMaterial
-------------

-------
Metodos
-------

__init__
********

Metodo que é executado quando o classe é instanciada, ele é o construtor da classe::

  __init__(self, parent=None)


addUsuarioLogado
****************

Captura do arquivo de login o usuario logado::

    addUsuarioLogado(self)

:ref:`return id_usu`: Retorna o id do usuario logado


abrirComboTecnico
*****************

Preenche o Combo de Tecnicos::

    abrirComboTecnico(self)


abrirComboDepto
***************

Preenche o Combo de Departamentos::

    abrirComboDepto(self)


montarTabelas
*************

Monta as colunas das tabelas das abas de busca de equipamento e baixa::

    montarTabelas(self)


buscaIncremental
****************

Faz uma busca no banco de dados, o tipo de busca varia de acordo com o parametro sql::

    buscaIncremental(self, sql)

:ref:`sql`: Instrução sql que define que tipo de busca o metodo vai executar.


capturaTecnico
**************

Captura o ID do responsavel::

    capturaTecnico(self,tec)

:ref:`tec`: Nome do tecnico, que terá seu id identificado

:ref:`return id_tec[0]`: Retorna o id do tecnico


capturaDepto
************

Captura o ID do departamento::

    capturaDepto(self)

:ref:`return id_depto[0]`: Retorna o id do departamento


validaBaixa
***********

Valida os dados da tela de baixa no estoque::

    validaBaixa(self)


insere
******

Insere os dados no banco::

    insere(self,obj)

:ref:`obj`: Objeto da classe baixamaterial


atualiza
********

Atualiza os dados no banco de dados::

    atualiza(self,obj)

:ref:`obj`: Objeto da classe baixamaterial


deleta
******

Deleta os dados no banco de dados::

    deleta(self,obj)

:ref:`obj`: Objeto da classe baixamaterial


on_btInserirBaixa_clicked
*************************

Insere os dados no banco, se os campos estiverem validos::

    @pyqtSignature("")
    on_btInserirBaixa_clicked(self)


on_btAtualizarBaixa_clicked
***************************

Atualiza os dados no banco, se os campos estiverem validos::

    @pyqtSignature("")
    on_btAtualizarBaixa_clicked(self)

