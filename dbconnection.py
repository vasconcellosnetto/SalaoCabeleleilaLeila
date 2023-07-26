from mysql.connector import (connection)
import settings

class DBConnection():

    def __init__(self):
        self.conexao = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='cabeleleila_leila_db')


    def testeLogin(self, login, senha):
        c = self.conexao.cursor()
        c.execute(f"SELECT * FROM (SELECT cliente_login AS login, cliente_nome AS nome, cliente_senha AS senha FROM clientes UNION ALL SELECT funcionario_login AS login, funcionario_nome AS nome, funcionario_senha AS senha FROM funcionarios) AS users WHERE login = '{login}' AND senha = '{senha}'")
        resultado = c.fetchone()
        c.close()
        if resultado is not None:
            settings.usuario = resultado[0]
            return True
        else:
            return False
        
    def listarFuncionarios(self):
        c = self.conexao.cursor()
        c.execute("SELECT * FROM funcionarios")
        resultado = c.fetchall()
        c.close()
        return resultado
    
    def verificarClientes(self):
        c = self.conexao.cursor()
        c.execute(f"SELECT cliente_nome FROM clientes WHERE cliente_login = '{settings.usuario}'")
        resultado = c.fetchone() 
        c.close() 
        return resultado[0]
    
    def cadastrarAgendamento(self, funcionario, data, hora, procedimentos):
        c = self.conexao.cursor()
        c.execute(f"SELECT funcionario_login FROM funcionarios WHERE funcionario_nome = '{funcionario}'")
        resultado = c.fetchone()
        data_hora = str(data) + "T" + str(hora)
        c.execute(f"INSERT INTO agendamentos (cliente_login, funcionario_login, agendamento_data, agendamento_servicos) VALUES ('{settings.usuario}', '{resultado[0]}', '{data_hora}', '{procedimentos}')")
        self.conexao.commit()
        c.close()
        return True
    
    def atualizarAgendamento(self, data, procedimentos):
        c = self.conexao.cursor()
        c.execute(f"UPDATE agendamentos SET agendamento_servicos = '{procedimentos}' WHERE agendamentos.cliente_login = '{settings.usuario}' AND agendamento_data = '{data}'")
        self.conexao.commit()
        c.close()
        return True
    
    def listarAgendamentosAll(self):
        c = self.conexao.cursor()
        c.execute(f"SELECT agendamento_data, agendamento_servicos, cliente_nome, funcionario_nome FROM agendamentos JOIN clientes ON (clientes.cliente_login = agendamentos.cliente_login) JOIN funcionarios ON (funcionarios.funcionario_login = agendamentos.funcionario_login) WHERE agendamentos.cliente_login = '{settings.usuario}'")
        resultado = c.fetchall() 
        c.close() 
        return resultado
    
    def listarAgendamentosData(self, data):
        c = self.conexao.cursor()
        c.execute(f"SELECT agendamento_data, agendamento_servicos, cliente_nome, funcionario_nome FROM agendamentos JOIN clientes ON (clientes.cliente_login = agendamentos.cliente_login) JOIN funcionarios ON (funcionarios.funcionario_login = agendamentos.funcionario_login) WHERE agendamentos.cliente_login = '{settings.usuario}' AND agendamento_data = '{data}'")
        resultado = c.fetchall() 
        c.close() 
        return resultado
    
    def listarAgendamentosUpdate(self):
        c = self.conexao.cursor()
        c.execute(f"SELECT agendamento_data, agendamento_servicos, cliente_nome, funcionario_nome FROM agendamentos JOIN clientes ON (clientes.cliente_login = agendamentos.cliente_login) JOIN funcionarios ON (funcionarios.funcionario_login = agendamentos.funcionario_login) WHERE agendamentos.cliente_login = '{settings.usuario}' AND DATE(agendamento_data) > DATE_ADD(DATE(NOW()), INTERVAL 2 DAY)")
        resultado = c.fetchall() 
        c.close() 
        return resultado