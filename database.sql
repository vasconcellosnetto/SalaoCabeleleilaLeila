CREATE DATABASE IF NOT EXISTS cabeleleila_leila_db;

USE cabeleleila_leila_db;

CREATE TABLE IF NOT EXISTS clientes (
    cliente_login VARCHAR(255),
    cliente_senha VARCHAR(255) NOT NULL,
    cliente_nome VARCHAR(255) NOT NULL,
    PRIMARY KEY (cliente_login)
);

CREATE TABLE IF NOT EXISTS funcionarios (
    funcionario_login VARCHAR(255),
    funcionario_senha VARCHAR(255) NOT NULL,
    funcionario_nome VARCHAR(255) NOT NULL,
    PRIMARY KEY (funcionario_login)
);

CREATE TABLE IF NOT EXISTS agendamentos (
    cliente_login VARCHAR(255) NOT NULL,
    funcionario_login VARCHAR(255) NOT NULL,
    agendamento_data DATETIME NOT NULL,
    agendamento_servicos VARCHAR(255) NOT NULL,
    FOREIGN KEY (cliente_login) REFERENCES clientes(cliente_login),
    FOREIGN KEY (funcionario_login) REFERENCES funcionarios(funcionario_login)
);