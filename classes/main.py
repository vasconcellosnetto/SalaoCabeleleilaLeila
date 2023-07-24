from tkinter import *
from dbconnection import DBConnection

class Application:
    def __init__(self, master=None):
        self.db = DBConnection()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
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

        self.titulo = Label(self.primeiroContainer, text="Informações de Login")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.usuarioLabel = Label(self.segundoContainer,text="Login: ", font=self.fontePadrao)
        self.usuarioLabel["width"] = 5
        self.usuarioLabel.pack(side=LEFT)

        self.usuario = Entry(self.segundoContainer)
        self.usuario["width"] = 20
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha: ", font=self.fontePadrao)
        self.senhaLabel["width"] = 5
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 20
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Arial", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

    #Método verificar senha
    def verificaSenha(self):
        self.db.teste_login(self.usuario.get(), self.senha.get())

root = Tk()
root.eval('tk::PlaceWindow . center')
Application(root)
root.mainloop()