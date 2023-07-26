from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from tktimepicker import SpinTimePickerOld, constants
from dbconnection import DBConnection

class Application:    

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

        Label(self.primeiroContainer, text="Login no Sistema", font = ("Arial", "10", "bold")).pack()

        Label(self.segundoContainer,text="Login: ", font=self.fontePadrao, width = 5).pack(side=LEFT)
        self.login = Entry(self.segundoContainer, width = 20, font = self.fontePadrao)
        self.login.pack(side=LEFT)

        Label(self.terceiroContainer, text="Senha: ", font=self.fontePadrao, width = 5).pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer, width = 20, font = self.fontePadrao, show = "*")
        self.senha.pack(side=LEFT)

        Button(self.quartoContainer, text = "Autenticar", font = ("Arial", "8"), width = 12, command = self.verificarLogin).pack(side=LEFT)
        Button(self.quartoContainer, text="Fechar", font = ("Arial", "8"), width = 12, command = root.destroy).pack(side=LEFT)
    
    db = DBConnection()

    def verificarLogin(self):
        if self.db.testeLogin(self.login.get(), self.senha.get()):  
            self.telaInicial()
        else:
            messagebox.showerror("Erro!","Usuário/senha incorreto!")

    def telaInicial(self):
        self.primeiroContainer.destroy()
        self.segundoContainer.destroy()
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()

        root.state('zoomed')

        barra_menu = Menu(root)

        agendamento_opcao = Menu(barra_menu, tearoff=0)            
        barra_menu.add_cascade(label="Agendamento", menu=agendamento_opcao)
        agendamento_opcao.add_command(label="Novo agendamento", command=self.novoAgendamento)
        agendamento_opcao.add_command(label="Alterar agendamento", command=self.alterarAgendamento)
        agendamento_opcao.add_command(label="Histórico de agendamentos", command="x = 0")

        operacao_opcao = Menu(barra_menu, tearoff=0)            
        barra_menu.add_cascade(label="Operações", menu=operacao_opcao)
        operacao_opcao.add_command(label="Alterar agendamento", command="x = 0", state=DISABLED)
        operacao_opcao.add_command(label="Listar agendamentos", command="x = 0")

        gerencia_opcao = Menu(barra_menu, tearoff=0)            
        barra_menu.add_cascade(label="Gerência", menu=gerencia_opcao, state=DISABLED)
        gerencia_opcao.add_command(label="Desempenho semanal", command="x = 0")
        gerencia_opcao.add_command(label="Listar agendamentos", command="x = 0")
            
        barra_menu.add_command(label="Sair", command=root.quit)
            
        root.config(menu=barra_menu)        

    def novoAgendamento(self):
        self.fonte = ("Verdana", "8")

        novoAgendamento = Toplevel(root)
        novoAgendamento.title("Novo agendamento")

        self.container1 = Frame(novoAgendamento)
        self.container1["pady"] = 20
        self.container1.pack()

        self.container2 = Frame(novoAgendamento)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(novoAgendamento)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(novoAgendamento)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(novoAgendamento)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(novoAgendamento)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(novoAgendamento)
        self.container7["pady"] = 15
        self.container7.pack()

        Label(self.container1, text="Novo agendamento:", font = ("Arial", "10", "bold")).pack()

        Label(self.container2, text="Cliente: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.txt_cliente_login = Entry(self.container2, width = 50, font = self.fonte)
        self.txt_cliente_login.pack(side=LEFT)
        self.txt_cliente_login.insert(INSERT, self.db.verificarClientes())
        self.txt_cliente_login.config(state=DISABLED)

        Label(self.container3, text="Cabelereiro(a): ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.funcionarios_cbb = ttk.Combobox(self.container3, textvariable=StringVar(), width = 50)

        funcionarios = []
        valores = self.db.listarFuncionarios()
        for x in range(len(valores)):
            funcionarios.append(valores[x][2])
        self.funcionarios_cbb['values'] = funcionarios
        self.funcionarios_cbb.pack(side=LEFT)

        Label(self.container4, text="Procedimentos: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.txt_procedimentos = Entry(self.container4, width = 50, font = self.fonte)
        self.txt_procedimentos.pack(side=LEFT)

        Label(self.container5, text="Data: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.data_cbb = DateEntry(self.container5, textvariable=StringVar(), width = 50, date_pattern="yyyy-MM-dd")
        self.data_cbb.pack(side=LEFT)

        Label(self.container6, text="Horário: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.hora = SpinTimePickerOld(self.container6)
        self.hora.addAll(constants.HOURS24)
        self.hora.pack(expand=True, fill="both", side=LEFT)

        Button(self.container7, text = "Agendar", font = ("Arial", "8"), width = 12, command = self.cadastrarAgendamento).pack(side=LEFT)
        Button(self.container7, text="Cancelar", font = ("Arial", "8"), width = 12, command = novoAgendamento.destroy).pack(side=LEFT)

    def alterarAgendamento(self):
        self.fonte = ("Verdana", "8")

        alterarAgendamento = Toplevel(root)
        self.container1 = Frame(alterarAgendamento)
        self.container1["pady"] = 20
        self.container1.pack()

        self.container2 = Frame(alterarAgendamento)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(alterarAgendamento)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(alterarAgendamento)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(alterarAgendamento)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container7 = Frame(alterarAgendamento)
        self.container7["pady"] = 15
        self.container7.pack()

        Label(self.container1, text="Alterar agendamento:", font = ("Arial", "10", "bold")).pack()

        Label(self.container2, text="Cliente: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.txt_cliente_login = Entry(self.container2, width = 50, font = self.fonte)
        self.txt_cliente_login.pack(side=LEFT)
        self.txt_cliente_login.insert(INSERT, self.db.verificarClientes())
        self.txt_cliente_login.config(state=DISABLED)        

        Label(self.container3, text="Data: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.data_cbb = ttk.Combobox(self.container3, textvariable=StringVar(), width = 50)
        datas = []
        valores = self.db.listarAgendamentosUpdate()
        for x in range(len(valores)):
            datas.append(valores[x][0])
        self.data_cbb['values'] = datas
        self.data_cbb.pack(side=LEFT)
        self.data_cbb.bind("<<ComboboxSelected>>", lambda _ : self.buscarAgendamento())

        Label(self.container4, text="Cabelereiro(a): ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.funcionarios_cbb = ttk.Combobox(self.container4, textvariable=StringVar(), width = 50)

        funcionarios = []
        valores = self.db.listarFuncionarios()
        for x in range(len(valores)):
            funcionarios.append(valores[x][2])
        self.funcionarios_cbb['values'] = funcionarios
        self.funcionarios_cbb.pack(side=LEFT)

        Label(self.container5, text="Procedimentos: ", font = ("Arial", "10", "bold")).pack(side=LEFT)
        self.txt_procedimentos = Entry(self.container5, width = 50, font = self.fonte)
        self.txt_procedimentos.pack(side=LEFT)

        Button(self.container7, text = "Atualizar", font = ("Arial", "8"), width = 12, command = self.atualizarAgendamento).pack(side=LEFT)
        Button(self.container7, text="Cancelar", font = ("Arial", "8"), width = 12, command = alterarAgendamento.destroy).pack(side=LEFT)

    def cadastrarAgendamento(self):
        hora = str(self.hora.hours24()) + ":" + str(self.hora.minutes())
        try:
            if self.db.cadastrarAgendamento(self.funcionarios_cbb.get(), self.data_cbb.get(), hora, self.txt_procedimentos.get()):  
                messagebox.showinfo("Sucesso!","Agendamento feito com sucesso!")      
            else:
                messagebox.showerror("Erro!","Erro ao agendar!")
        except:
            messagebox.showerror("Erro!","Erro ao agendar!")

    def atualizarAgendamento(self):
        try:
            if self.db.atualizarAgendamento(self.data_cbb.get(), self.txt_procedimentos.get()):  
                messagebox.showinfo("Sucesso!","Atualização feita com sucesso!") 
            else:
                messagebox.showerror("Erro!","Erro ao atualizar!")
        except:
            messagebox.showerror("Erro!","Erro ao atualizar!")
    
    def buscarAgendamento(self):
        info = self.db.listarAgendamentosData(self.data_cbb.get())
        
        self.funcionarios_cbb.config(state=NORMAL)
        self.funcionarios_cbb.delete(0, END)
        self.funcionarios_cbb.set(info[0][3])
        self.funcionarios_cbb.config(state=DISABLED) 

        self.txt_procedimentos.delete(0, END)
        self.txt_procedimentos.insert(INSERT, info[0][1]) 

root = Tk()
root.eval('tk::PlaceWindow . center')
root.title("Cabeleleila Leila")
Application(root)
root.mainloop()