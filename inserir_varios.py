from conexao_criar_tabela import conn, cursor

def inserir_varios(conn, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conn.commit()

dados = [
    ("João Antônio", "joaocharao@gmail.com"), 
    ("Leda Diello", "ledadiello@gmail.com"), 
    ("Valdemar Borges", "valdemarborges@gmail.com")
    ]

inserir_varios(conn, cursor, dados)