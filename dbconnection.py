from mysql.connector import (connection)
import settings

class DBConnection():

    def __init__(self):
        self.conexao = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='cabeleleila_leila_db')


    def testeLogin(self, login, senha):
        c = self.conexao.cursor()
        c.execute(f"SELECT * FROM( SELECT cliente_login AS login, cliente_nome AS nome, cliente_senha AS senha FROM clientes UNION ALL SELECT funcionario_login AS login, funcionario_nome AS nome, funcionario_senha AS senha FROM funcionarios) AS users WHERE login = '{login}' AND senha = '{senha}';")
        resultado = c.fetchone()
        c.close()
        if resultado is not None:
            settings.usuario = resultado[0]
            return True
        else:
            return False
        
    def listarFuncionarios(self):
        c = self.conexao.cursor()
        c.execute("SELECT funcionario_nome FROM funcionarios")
        resultado = c.fetchall()
        c.close()
        return resultado
    
    def verificarClientes(self):
        c = self.conexao.cursor()
        c.execute(f"SELECT cliente_nome FROM clientes WHERE cliente_login = '{settings.usuario}'")
        resultado = c.fetchone() 
        c.close() 
        return resultado[0]

