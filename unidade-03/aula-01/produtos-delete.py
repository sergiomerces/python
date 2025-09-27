import sqlite3

conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

produto_id = 2

excluir_produto = "DELETE FROM Produtos WHERE id = ?"

cursor.execute(excluir_produto, (produto_id))
conn.commit()

conn.close()
