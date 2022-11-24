from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Banco
import re


def ValidarFone(fone):
    padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
    resposta = re.findall(padrao, fone)
    if resposta:
        return True
    else:
        return False
def ValidarEmail(email):
    padrao = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    resposta = re.findall(padrao, email)
    if resposta:
        return True
    else:
        return False

def popular():
    tv.delete(*tv.get_children())                   # Deletando os registros do TreeView
    Vquery = "SELECT * FROM tb_nomes order by ID"   # Pesquisa do SQL q traz todos os nomes ordenados por ID
    linhas = Banco.dql(Vquery)
    for i in linhas:                                # Puxando os dados do banco
        tv.insert("", "end", values=i)

def verificaPhone(phone):
    #tv.delete(*tv.get_children())
    Vquery = "SELECT fone FROM tb_nomes WHERE fone='{}'".format(phone)
    linhas = Banco.dql(Vquery)
    if len(linhas)!=0:
        return False
    else:
        return True
    
def formataFone(phone):
    return '+{}({}){}-{}'.format(phone[:2], phone[2:4], phone[4:9], phone[9:])

def inserir():

    phone = Vfone.get()
    email = Vemail.get()

    if Vnome.get()=="" or Vendereco.get()=="" or Vcidade.get()=="" or Vestado.get()=="" or Vfone.get()=="" or Vemail.get()=="":  # Verificando se os campos estao digitados
        messagebox.showinfo(title="ERRO", message="Digite todos os dados!")
        return
    elif ValidarFone(phone) == False:
        messagebox.showinfo(title="ERRO", message="Digite um Telefone Valido!")
        return
    elif ValidarEmail(email) == False:
        messagebox.showinfo(title="ERRO", message="Digite um Email Valido!")
        return
    elif verificaPhone(phone) == False:
        messagebox.showinfo(title="ERRO", message="Telefone Ja Cadastrado!")
        return
    try:
        altera = formataFone(phone)
        Vquery = "INSERT INTO tb_nomes (nome, endereco, cidade, estado, fone, email) \
                  VALUES ('"+Vnome.get()+"','"+Vendereco.get()+"','"+Vcidade.get()+"','"+Vestado.get()+"' ,'"+altera+"', '"+Vemail.get()+"')"
        Banco.dml(Vquery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro as Inserir")
        return
    
    popular()
    Vemail.delete(0, END)
    Vfone.delete(0, END)
    Vnome.delete(0, END)
    Vendereco.delete(0, END)
    Vcidade.delete(0, END)
    Vestado.delete(0, END)
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