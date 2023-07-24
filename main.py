from tkinter import *
from dbconnection import DBConnection
import settings


class Application:
    db = DBConnection()

    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.erroLabel = Label(self.primeiroContainer, text="", font = ("Arial", "10", "bold"), fg="red")
        self.erroLabel.pack()

        Label(self.primeiroContainer, text="Login no Sistema", font = ("Arial", "10", "bold")).pack()

        Label(self.segundoContainer,text="Login: ", font=self.fontePadrao, width = 5).pack(side=LEFT)
        self.login = Entry(self.segundoContainer, width = 20, font = self.fontePadrao)
        self.login.pack(side=LEFT)

        Label(self.terceiroContainer, text="Senha: ", font=self.fontePadrao, width = 5).pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer, width = 20, font = self.fontePadrao, show = "*")
        self.senha.pack(side=LEFT)

        Button(self.quartoContainer, text = "Autenticar", font = ("Arial", "8"), width = 12, command = self.verificaSenha).pack(side=LEFT)
        Button(self.quartoContainer, text="Fechar", font = ("Arial", "8"), width = 12, command = root.destroy).pack(side=LEFT)

    #Método verificar senha
    def verificaSenha(self):
        if self.db.teste_login(self.login.get(), self.senha.get()):
            root.destroy()
        else:
            self.erroLabel["text"] = "Usuário/senha incorreto!"

root = Tk()
root.eval('tk::PlaceWindow . center')
root.title("Cabeleleila Leila")
Application(root)
root.mainloop()