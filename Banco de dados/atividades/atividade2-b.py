import sqlite3 as conector

conexao = conector.connect("banco.db")

comando = '''CREATE TABLE Cidade (
                    id INTEGER NOT NULL,
                    nome TEXT,
                    estado TEXT
                    );'''

conexao.execute(comando)
conexao.commit()
conexao.close()
