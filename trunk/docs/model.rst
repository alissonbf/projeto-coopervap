.. _model:


************
Modulo Model
************

Escrito por: 

* Alisson Barbosa Ferreira, alissonbf@gmail.com                   
* Alisson Oliveira Ferreira, linukiss@gmail.com                  
* Victor Hugo Neiva, victorhugoneiva@gmail.com                          
* Wesley Junior                              
                                                          
Criado em: 

- 30/08/2010			                       
						                                   
Ultima atualização: 

- 22/12/2010		                   
						                                   
Descrição

- Este modulo contem as classes dos objetos que são usados pelo programa.

.. _usuario:

--------------
Classe Usuario
--------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe usuario é instanciada, ele é o construtor da classe::

  __init__(self, nome,email,funcao,status,login,senha, id_usu=None)

:ref:`nome`: Parâmetro que recebe o nome do usuario

:ref:`email`: Parâmetro que recebe o e-mail do usuario

:ref:`funcao`: Parâmetro que recebe a função do usuario

:ref:`status`: Parâmetro que recebe o status do usuario, o status pode ser ativo, ainda trabalha na empresa, ou inativo, não trabalha mais na empresa

:ref:`login`: Parâmetro que recebe o login do usuario

:ref:`senha`: Parâmetro que recebe a senha do usuario

:ref:`id_usu`: Parâmetro que recebe o id do usuario, se o id não for passado ele recebe None

-------------------
Classe Departamento
-------------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe departamento é instanciada, ele é o construtor da classe::

  __init__(self,nome,centro,id=None)

:ref:`nome`: Parâmetro que recebe o nome do departamento

:ref:`centro`: Parâmetro que recebe o valor do centro de custo do departamento

:ref:`id`: Parâmetro que recebe o id do departamento, se o id não for passado ele recebe None


--------------
Classe Tecnico
--------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe tecnico é instanciada, ele é o construtor da classe::

  __init__(self,nome,funcao,departamento,status,usuario,id=None)

:ref:`nome`: Parâmetro que recebe o nome do tecnico

:ref:`funcao`: Parâmetro que recebe a função do tecnico

:ref:`departamento`: Parâmentro que recebe o departamento onde o tecnico trabalha

:ref:`status`: Parâmetro que recebe o status do tecnico

:ref:`id`: Parâmetro que recebe o id do tecnico, se o id não for passado ele recebe None


------------------
Classe Equipamento
------------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe equipamento é instanciada, ele é o construtor da classe::

  __init__(self, nome, marca, unidade, quantidade, estoque, id_resp, usuario, id_equip=None)

:ref:`nome`: Parâmetro que recebe o nome do equipamento

:ref:`marca`: Parâmetro que recebe a marca do equipamento

:ref:`unidade`: Parâmetro que recebe a unidade do equipamento

:ref:`quantidade`: Parâmetro que recebe a quantidade de equipamentos que estão sendo cadastrados

:ref:`estoque`: Parâmetro que recebe a quantidade minima de equipamentos que pode-se ter

:ref:`id_resp`: Parâmetro que recebe o id do responsavel pelo equipamento

`usuario`: Parâmetro que recebe o id do usuario que cadastrou o equipamento

:ref:`id_equip`: Parâmetro que recebe o id do equipamento, se o id não for passado ele recebe None


-------------------
Classe PedidoCompra
-------------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe pedidocompra é instanciada, ele é o construtor da classe::

  __init__(self,data,status,id_usu,id_resp,id=None)

:ref:`data`: Parâmetro que recebe a data do pedido de compra

:ref:`status`: Parâmetro que recebe o status do pedido de compra

:ref:`id_usu`: Parâmetro que recebe o id do usuario que fez o pedido de compra

:ref:`id_resp`: Parâmetro que recebe o id do responsavel pelo pedido de compra

:ref:`id`: Parâmetro que recebe o id do pedido de compra, se o parametro não for passado a variavel recebe None


------------------------
Classe EquipamentoPedido
------------------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe equipamentopedido é instanciada, ele é o construtor da classe::

  __init__(self,nome,descricao,unidade,entrega,id_pedido,id=None)


:ref:`nome`: Parâmetro que recebe o nome do equipamento

:ref:`descricao`: Parâmetro que recebe a descrição do equipamento

:ref:`unidade`: Parâmetro que recebe a unidade do equipamento

:ref:`entrega`: Parâmetro que recebe a entrega do equipamento

:ref:`id_pedido`: Parâmetro que recebe o id do pedido

:ref:`id`: Parâmetro que recebe o id do equipamento do pedido, se o parametro não for passado a variavel recebe None


--------------------
Classe BaixaMaterial
--------------------

Metodos
=======

__init__
--------

Metodo que é executado quando o classe baixaMaterial é instanciada, ele é o construtor da classe::

  __init__(self, equipamento, qtd,id_depto,data,id_tec,motivo,id_usu,id=None)

:ref:`equipamento`: Parâmetro que recebe o nome do equipamento

:ref:`qtd`: Parâmetro que recebe a quantidade de equipamentos

:ref:`id_depto`: Parâmetro que recebe o id do departamento

:ref:`data`: Parâmetro que recebe a data da baixa

:ref:`id_tec`: Parâmetro que recebe o id do tecnico

:ref:`motivo`: Parâmetro que recebe o motivo da baixa

:ref:`id_usu`: Parâmetro que recebe o id do usuario que fez a baixa 

:ref:`id`: Parâmetro que recebe o id da baixa do material, se o parametro não for passado a variavel recebe None
