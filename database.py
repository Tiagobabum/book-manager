
import sqlite3


conexao =  sqlite3.connect("livros.db")
cursor = conexao.cursor()

cursor.execute('''    
        CREATE TABLE IF NOT EXISTS usuario (
        
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE

        )
''')

cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS livro (

        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        nome_livro TEXT,
        paginas_lidas INTEGER DEFAULT 0,
        paginas_totais INTEGER NOT NULL,
        genero TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        UNIQUE (usuario_id, nome_livro)
        )
''')

conexao.commit()
conexao.close()
