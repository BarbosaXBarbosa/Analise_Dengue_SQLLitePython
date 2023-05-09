import sqlite3 as conector
conexao = conector.connect("banco.db")
cursor = conexao.cursor()

comando1 = '''CREATE TABLE Produto (
                codigo INTEGER NOT NULL,
                nome TEXT NOT NULL,
                PRIMARY KEY (codigo));'''
cursor.execute(comando1)

comando2 = '''CREATE TABLE Arremate (
                id INTEGER NOT NULL,
                data DATE NOT NULL,
                cod_prod INTEGER NOT NULL,
                FOREIGN KEY(cod_prod) REFERENCES Produto(codigo));'''
cursor.execute(comando2)

cursor.execute('ALTER TABLE Produto ADD descricao TEXT;')
cursor.execute('ALTER TABLE Produto ADD preco_inicial REAL;')
cursor.execute('ALTER TABLE Arremate ADD lance_vencedor REAL;')

conexao.commit()
cursor.close()
conexao.close()
