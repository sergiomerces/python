import sqlite3

conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()
novo_produto = ('Camiseta', 19.99, 50)

inserir_produto = "INSERT INTO Produtos(nome, preco, estoque) VALUES(?, ?, ?)"

cursor.execute(inserir_produto, novo_produto)
conn.commit()

conn.close()