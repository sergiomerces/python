import sqlite3

conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

novo_preco = 24.99
produto_id = 1

atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco, produto_id))

conn.commit()

conn.close()