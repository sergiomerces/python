import sqlite3

# CREATE (cria a tabela de naco de dados de exemplo)

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Contatos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
    )
''')

dados_exemplo = [
    ('Izabel', 'izamerces@hotmail.com', '1197750663'),
    ('Pablo', 'pablo@gmail.com', '119751257878'),
    ('Pietra', 'pietra@gmail.com', '11985203697')
]

cursor.executemany('INSERT INTO Contatos(nome, email, telefone) VALUES(?, ?, ?)', dados_exemplo)
conn.commit()

# READ (leitura e exibição dos dados)

cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print('Contatos:')
for contato in contatos:
    print(contato)

# UPDATE (Atualização do número de telefone do contato com ID 2)

novo_telefone = '11975361691'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()

# DELETE (Exclusão do contato com ID 1)

contato_id_para_excluir = 1
cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir))
conn.commit()

# Fechando conexão
conn.close()
