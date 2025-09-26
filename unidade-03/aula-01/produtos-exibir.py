import sqlite3

conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"

cursor.execute(selecionar_produtos)
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

conn.close()