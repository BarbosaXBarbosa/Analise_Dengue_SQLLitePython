import psycopg2 as conector
try:
    conexao = conector.connect("dbname=meu_banco user=post password=post")
    cursor = conexao.cursor()

    comando1 = '''CREATE TABLE Produto (
                    codigo INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    PRIMARY KEY (codigo));'''
    cursor.execute(comando1)
    conexao.commit()

    comando2 = '''CREATE TABLE Arremate (
                    id INTEGER NOT NULL,
                    data DATE NOT NULL,
                    cod_prod INTEGER NOT NULL,
                    FOREIGN KEY(cod_prod) REFERENCES Produto(cod));'''
    cursor.execute(comando2)

    conexao.commit()
    cursor.close()
    conexao.close()

except conector.ProgrammingError as err:
    print("Erro de Programação")
except conector.IntegrityError as err:
    print("Erro de Integridade")
