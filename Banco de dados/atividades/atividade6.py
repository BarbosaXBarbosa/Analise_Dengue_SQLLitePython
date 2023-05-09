import sqlite3 as conector
import psycopg2


conexao = psycopg2.connect("banco.db")
cursor = conexao.cursor()
cursor.lastrowbyid


conexao = conector.connect("banco.db")
cursor = conexao.cursor()

comando = '''SELECT X, Y
             FROM Produto JOIN Arremate ON Z = W
             ORDER BY Produto.codigo;'''
cursor.execute(comando)

registros = cursor.fetchall()
print(registros)

conexao.commit()
cursor.close()
conexao.close()
