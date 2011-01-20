CREATE SEQUENCE usuario_id_usuario_seq;

CREATE TABLE usuario (
                ID_usuario INTEGER NOT NULL DEFAULT nextval('usuario_id_usuario_seq'),
                nome VARCHAR(100) NOT NULL,
                status VARCHAR(10) NOT NULL,
                email VARCHAR(100) NOT NULL,
                funcao VARCHAR(100) NOT NULL,
                login VARCHAR(100) unique NOT NULL,
                senha VARCHAR(50) NOT NULL,
                CONSTRAINT usuario_pk PRIMARY KEY (ID_usuario)
);


ALTER SEQUENCE usuario_id_usuario_seq OWNED BY usuario.ID_usuario;

CREATE SEQUENCE departamento_id_departamento_seq;

CREATE TABLE departamento (
                ID_departamento INTEGER NOT NULL DEFAULT nextval('departamento_id_departamento_seq'),
                nome VARCHAR(100) unique NOT NULL,
                centro_de_custo VARCHAR(9) NOT NULL,
                ID_usuario INTEGER NOT NULL,
                CONSTRAINT departamento_pk PRIMARY KEY (ID_departamento)
);


ALTER SEQUENCE departamento_id_departamento_seq OWNED BY departamento.ID_departamento;

CREATE SEQUENCE tecnico_id_tecnico_seq;

CREATE TABLE tecnico (
                ID_tecnico INTEGER NOT NULL DEFAULT nextval('tecnico_id_tecnico_seq'),
                nome  VARCHAR(100) unique NOT NULL,
                funcao VARCHAR(100) NOT NULL,
                status VARCHAR(10) NOT NULL,
                ID_usuario INTEGER NOT NULL,
                ID_departamento INTEGER NOT NULL,
                CONSTRAINT tecnico_pk PRIMARY KEY (ID_tecnico)
);


ALTER SEQUENCE tecnico_id_tecnico_seq OWNED BY tecnico.ID_tecnico;


CREATE SEQUENCE equipamento_id_equipamento_seq;

CREATE TABLE equipamento (
                ID_equipamento INTEGER NOT NULL DEFAULT nextval('equipamento_id_equipamento_seq'),
                nome VARCHAR(90) NOT NULL,
                marca_modelo VARCHAR(100) NOT NULL,
                unidade VARCHAR(70),
                quantidade_inicial INTEGER NOT NULL,
                estoque_min INTEGER NOT NULL,
                ID_usuario INTEGER NOT NULL,
                ID_tecnico INTEGER NOT NULL,
                CONSTRAINT equipamento_pk PRIMARY KEY (ID_equipamento)
);


ALTER SEQUENCE equipamento_id_equipamento_seq OWNED BY equipamento.ID_equipamento;

CREATE SEQUENCE baixa_id_baixa_seq;

CREATE TABLE baixa (
                ID_baixa INTEGER NOT NULL DEFAULT nextval('baixa_id_baixa_seq'),
                data DATE NOT NULL,
                motivo VARCHAR(400) NOT NULL,
                quantidade INTEGER NOT NULL,
                ID_usuario INTEGER NOT NULL,
                ID_departamento INTEGER NOT NULL,
                ID_tecnico INTEGER NOT NULL,
                CONSTRAINT baixa_pk PRIMARY KEY (ID_baixa)
);


ALTER SEQUENCE baixa_id_baixa_seq OWNED BY baixa.ID_baixa;

CREATE SEQUENCE baixa_por_equipamento_id_be_seq;

CREATE TABLE baixa_por_equipamento (
                id_be INTEGER NOT NULL DEFAULT nextval('baixa_por_equipamento_id_be_seq'),
                ID_baixa INTEGER NOT NULL,
                ID_equipamento INTEGER NOT NULL,
                CONSTRAINT baixa_por_equipamento_pk PRIMARY KEY (id_be)
);


ALTER SEQUENCE baixa_por_equipamento_id_be_seq OWNED BY baixa_por_equipamento.id_be;

CREATE TABLE pedido_compra (
                codigo INTEGER NOT NULL,
                data VARCHAR(10) NOT NULL,
                ID_usuario INTEGER NOT NULL,
                ID_tecnico INTEGER NOT NULL,
                status VARCHAR(10) NOT NULL,
                CONSTRAINT pedido_compra_pk PRIMARY KEY (codigo)
);


CREATE SEQUENCE pedido_equipamento_id_seq;

CREATE TABLE pedido_equipamento (
                id INTEGER NOT NULL DEFAULT nextval('pedido_equipamento_id_seq'),
                codigo INTEGER NOT NULL,
                nome VARCHAR(90) NOT NULL,
                descricao VARCHAR(400) NOT NULL,
                unidade VARCHAR(70),
                entrega VARCHAR(10),
                CONSTRAINT pedido_equipamento_pk PRIMARY KEY (id, codigo)
);


ALTER SEQUENCE pedido_equipamento_id_seq OWNED BY pedido_equipamento.id;

ALTER TABLE tecnico ADD CONSTRAINT usuario_tecnico_fk
FOREIGN KEY (ID_usuario)
REFERENCES usuario (ID_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pedido_compra ADD CONSTRAINT usuario_new_table_fk
FOREIGN KEY (ID_usuario)
REFERENCES usuario (ID_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE departamento ADD CONSTRAINT usuario_departamento_fk
FOREIGN KEY (ID_usuario)
REFERENCES usuario (ID_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE equipamento ADD CONSTRAINT usuario_equipamento_fk
FOREIGN KEY (ID_usuario)
REFERENCES usuario (ID_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE baixa ADD CONSTRAINT usuario_baixa_de_estoque_fk
FOREIGN KEY (ID_usuario)
REFERENCES usuario (ID_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE baixa ADD CONSTRAINT departamento_baixa_fk
FOREIGN KEY (ID_departamento)
REFERENCES departamento (ID_departamento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE tecnico ADD CONSTRAINT departamento_tecnico_fk
FOREIGN KEY (ID_departamento)
REFERENCES departamento (ID_departamento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pedido_compra ADD CONSTRAINT tecnico_new_table_fk
FOREIGN KEY (ID_tecnico)
REFERENCES tecnico (ID_tecnico)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE baixa ADD CONSTRAINT tecnico_baixa_fk
FOREIGN KEY (ID_tecnico)
REFERENCES tecnico (ID_tecnico)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE equipamento ADD CONSTRAINT tecnico_equipamento_fk
FOREIGN KEY (ID_tecnico)
REFERENCES tecnico (ID_tecnico)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE baixa_por_equipamento ADD CONSTRAINT equipamento_baixa_por_equipamento_fk
FOREIGN KEY (ID_equipamento)
REFERENCES equipamento (ID_equipamento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE baixa_por_equipamento ADD CONSTRAINT baixa_baixa_por_equipamento_fk
FOREIGN KEY (ID_baixa)
REFERENCES baixa (ID_baixa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pedido_equipamento ADD CONSTRAINT pedido_compra_pedido_equipamento_fk
FOREIGN KEY (codigo)
REFERENCES pedido_compra (codigo)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
