import sqlite3 as conector

conexao = conector.connect("banco.db")
cursor = conexao.cursor()
produtos = [
    {"cod": 1, "nome": "Carro A", "desc": "Quatro portas e motor 1.0", "preco": 10000},
    {"cod": 2, "nome": "Carro B", "desc": "Duas portas e motor 2.0", "preco": 20000},
    {"cod": 3, "nome": "Carro C", "desc": "Sem portas e motor 5.0", "preco": 30000},
    {"cod": 4, "nome": "Carro D", "desc": "Teto solar e motor 1.4", "preco": 40000}
]

cmd_produto = ?
for produto in produtos:
    cursor.execute(cmd_produto, produto)

conexao.commit()
cursor.close()
conexao.close()
