import sqlite3 as conector

conexao = conector.connect("banco.db")
cursor = conexao.cursor()

comando = '''CREATE TABLE Cidade (
                    id INTEGER NOT NULL,
                    nome TEXT,
                    estado TEXT
                    );'''

conexao.commit(comando)
cursor.close()
conexao.close()
