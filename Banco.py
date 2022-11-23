import sqlite3
from sqlite3 import Error
import os
import re


app = os.path.dirname(__file__)
nameBank = app+"\\contatos.db"

    # Funcao q faz a conexao #
def ConectBank():
    con = None
    try:
        con = sqlite3.connect(nameBank)
    except Error as ex:
        print(ex)
    return con

    # SELECT #
def dql(query):
    vcon = ConectBank()
    cursor = vcon.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    vcon.close()
    return res

    # INSERT | UPDATE | DELETE #
def dml(query):
    try:
        vcon = ConectBank()
        cursor = vcon.cursor()
        cursor.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)



class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto')

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        numero_formatado = '+{}({}){}-{}'.format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return (numero_formatado)