CREATE DATABASE IF NOT EXISTS cabeleleila_leila_db;

USE cabeleleila_leila_db;

CREATE TABLE IF NOT EXISTS usuarios (
usuario_cod INT AUTO_INCREMENT,
usuario_nome VARCHAR(255) NOT NULL,
usuario_telefone INT NOT NULL,
PRIMARY KEY (usuario_cod)
);

CREATE TABLE IF NOT EXISTS usuarios_login (
login VARCHAR(255),
senha VARCHAR(255) NOT NULL,
usuario_cod_fk INT NOT NULL,
PRIMARY KEY (login),
FOREIGN KEY (usuario_cod_fk) REFERENCES usuarios(usuario_cod)
);

