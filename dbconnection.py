from mysql.connector import (connection)
import settings

class DBConnection():

    def __init__(self):
        self.conexao = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='cabeleleila_leila_db')


    def teste_login(self, login, senha):
        c = self.conexao.cursor()

        c.execute(f"SELECT * FROM usuarios_login WHERE login = '{login}' AND senha = '{senha}'")

        resultado = c.fetchone()

        if resultado is not None:
            settings.usuario = resultado[2]
            return True
        else:
            return False