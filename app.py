from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Banco
import re
from Banco import TelefonesBr

def email():
    pass

def popular():
    tv.delete(*tv.get_children())                   # Deletando os registros do TreeView
    Vquery = "SELECT * FROM tb_nomes order by ID"   # Pesquisa do SQL q traz todos os nomes ordenados por ID
    linhas = Banco.dql(Vquery)
    for i in linhas:                                # Puxando os dados do banco
        tv.insert("", "end", values=i)
        
def inserir():
    if Vnome.get()=="" or Vendereco.get()=="" or Vcidade.get()=="" or Vestado.get()=="" or Vfone.get()=="" or Vemail.get()=="":  # Verificando se os campos estao digitados
        messagebox.showinfo(title="ERRO", message="Digite todos os dados!")
        return
    try:
        Vquery = "INSERT INTO tb_nomes (nome, endereco, cidade, estado, fone, email) \
                  VALUES ('"+Vnome.get()+"','"+Vendereco.get()+"','"+Vcidade.get()+"','"+Vestado.get()+"' ,'"+Vfone.get()+"', '"+Vemail.get()+"')"
        Banco.dml(Vquery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro as Inserir")
        return
    

    popular()
    Vnome.delete(0, END)
    Vendereco.delete(0, END)
    Vcidade.delete(0, END)
    Vestado.delete(0, END)
    Vfone.delete(0, END)
    Vemail.delete(0, END)
    Vnome.focus()
    
def deletar():
    if VidDel.get()=="":  # Verificando se os campos estao digitados
        messagebox.showinfo(title="ERRO", message="Digite todos os dados!")
        return
    try:
        Vquery = "DELETE FROM tb_nomes WHERE ID="+VidDel.get()
        Banco.dml(Vquery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao Deletar")
        return
    popular()
    VidDel.delete(0, END)
    VidDel.focus()
    
def pesquisar():
    tv.delete(*tv.get_children())
    Vquery = "SELECT * FROM tb_nomes WHERE nome LIKE '%"+VnomeSearch.get()+"%' order by ID"
    linhas = Banco.dql(Vquery)
    for i in linhas:
        tv.insert("", "end", values=i)
    
    
app = Tk()
app.title("Lista Telefonica")
app.geometry("900x600")

############# LABEL DA GRADE DE CLIENTES ################
FrameGrade = LabelFrame(app, text="Contatos")
FrameGrade.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(FrameGrade, columns=('id', 'nome', 'endereco', 'cidade', 'estado', 'fone', 'email'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=100)
tv.column('endereco', minwidth=0, width=200)
tv.column('cidade', minwidth=0, width=100)
tv.column('estado', minwidth=0, width=50)
tv.column('fone', minwidth=0, width=100)
tv.column('email', minwidth=0, width=150)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('endereco', text='ENDERECO')
tv.heading('cidade', text='CIDADE')
tv.heading('estado', text='ESTADO')
tv.heading('fone', text='TELEFONE')
tv.heading('email', text='EMAIL')
tv.pack()
popular()


############# LABEL DA INSERIR ################
FrameInserir = LabelFrame(app, text="Inserir Novos Contatos")
FrameInserir.pack(fill="both", expand="yes", padx=10, pady=10)

LBnome = Label(FrameInserir, text="Nome")
#LBnome.pack(side="top")
Vnome = Entry(FrameInserir, text="Nome")
#Vnome.pack(side="top", padx=10)
LBnome.grid(row=1, column=1)
Vnome.grid(row=1, column=2, padx=10)
LBendereco = Label(FrameInserir, text="Endereco")
#LBendereco.pack(side="top")
LBendereco.grid(row=1, column=3)
Vendereco = Entry(FrameInserir)
#Vendereco.pack(side="right", padx=10)
Vendereco.grid(row=1, column=4, padx=10)
LBcidade = Label(FrameInserir, text="Cidade")
#LBcidade.pack(side="right")
LBcidade.grid(row=2, column=3)
Vcidade = Entry(FrameInserir)
#Vcidade.pack(side="right", padx=10)

Vcidade.grid(row=2, column=4, padx=10)
LBestado = Label(FrameInserir, text="Estado")
#LBestado.pack(side="right")
LBestado.grid(row=3, column=3)
Vestado = StringVar(FrameInserir)
TipEstado = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
Vestado.set("Selecione:")
popUpEstado = OptionMenu(FrameInserir, Vestado, *TipEstado)
popUpEstado.grid(row=3, column=4, padx=10)


LBfone = Label(FrameInserir, text="Fone")
#LBfone.pack(side="top")
LBfone.grid(row=2, column=1)
Vfone = Entry(FrameInserir)
#Vfone.pack(side="top", padx=10)
Vfone.grid(row=2, column=2, padx=10)
LBemail = Label(FrameInserir, text="Email")
#LBemail.pack(side="top")
LBemail.grid(row=3, column=1)
Vemail = Entry(FrameInserir)
#Vemail.pack(side="top", padx=10)
Vemail.grid(row=3, column=2, padx=10)
ButInserir = Button(FrameInserir, text="Inserir", command=inserir)
#ButInserir.pack(side="top", padx=10)
ButInserir.grid(row=2, column=5, padx=10)



############# LABEL DE PESQUISAR ################
FramePesquisar = LabelFrame(app, text = "Pesquisar Contatos")
FramePesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

LBid = Label(FramePesquisar, text="Nome")
LBid.pack(side="left")
VnomeSearch = Entry(FramePesquisar)
VnomeSearch.pack(side="left", padx=10)
ButPesquisar = Button(FramePesquisar, text="Pesquisar", command=pesquisar)
ButPesquisar.pack(side="left", padx=10)
ButAll = Button(FramePesquisar, text="Mostrar Todos", command=popular)
ButAll.pack(side="left", padx=10)

############# LABEL DE DELETAR ################
FrameDeletar = LabelFrame(app, text = "Deletar Contato")
FrameDeletar.pack(fill="both", expand="yes", padx=10, pady=10)

LBid = Label(FrameDeletar, text="ID")
LBid.pack(side="left")
VidDel = Entry(FrameDeletar)
VidDel.pack(side="left", padx=10)
ButDeletar = Button(FrameDeletar, text="Deletar", command=deletar)
ButDeletar.pack(side="left", padx=10)


app.mainloop()