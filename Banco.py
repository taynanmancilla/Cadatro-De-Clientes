import sqlite3
from sqlite3 import Error
import os

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
