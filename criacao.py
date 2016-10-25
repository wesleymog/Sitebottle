import sqlite3


conn = sqlite3.connect('vozdaufrj.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE noticias (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        conteudo LONGTEXT NOT NULL,
        imagem longblob 
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
