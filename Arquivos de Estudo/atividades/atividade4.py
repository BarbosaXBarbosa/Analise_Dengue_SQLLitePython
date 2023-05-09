import sqlite3 as conector

conexao = conector.connect("banco.db")
cursor = conexao.cursor()

cmd_produto = '''INSERT INTO Produto VALUES (?, ?, ?, ?);'''
cursor.execute(cmd_produto, (10, "Faca", "Faca de aço inox", 50.00))
cursor.execute(cmd_produto, (20, "Garfo", "Garfo de aço inox", 30.00))
cursor.execute(cmd_produto, (30, "Prato", "Prato de porcelana", 100.00))

cmd_arremate = '''INSERT INTO Arremate VALUES (?, ?, ?, ?);'''
cursor.execute(cmd_arremate, (1, "01-10-2020", 10, 55.00))
cursor.execute(cmd_arremate, (2, "01-10-2020", 20, 39.00))
cursor.execute(cmd_arremate, (3, "01-10-2020", 30, 110.00))

cmd_atual_prod = '''UPDATE Produto SET descricao=? WHERE codigo=?;'''
cursor.execute(cmd_atual_prod, ("Faca de ouro", 10))

cmd_atual_arrem = '''UPDATE Arremate SET
                        lance_vencedor=?, data=? WHERE cod_prod=?;'''
cursor.execute(cmd_atual_arrem, (3000, '02-10-2020', 20))

conexao.commit()
cursor.close()
conexao.close()
