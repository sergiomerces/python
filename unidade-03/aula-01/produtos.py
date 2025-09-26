import sqlite3

# 1. conectar ao banco de dados (criar banco de dados caso não exista)
conn = sqlite3.connect('produtos.db')

# 2. criar um objeto cursor
cursor = conn.cursor()

# 3. criar tabela com SQL
create_table = ''' 
CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRYMARY KEY,
    nome TEXT NOT NULL,
    preco TEXT NOT NULL,
    estoque INTEGER
)
'''

# 4.executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. confirmar as alterações (commit)
conn.commit()

# 6. fechar a conexão com o banco de dados
conn.close()