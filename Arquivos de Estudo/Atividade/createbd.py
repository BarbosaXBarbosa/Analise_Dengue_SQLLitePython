import sqlite3 as conector

conexao = None
cursor = None

try:
    conexao = conector.connect("banco.db")

except conector.DatabaseError as erro:
    print("Erro do Bando de Dados", erro)

finally:

    if cursor:
        cursor.close()
    if conexao:
        conexao.close()