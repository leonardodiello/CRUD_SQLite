import sqlite3

conn = sqlite3.connect('meu_BD.db')

cursor = conn.cursor()

def criar_tabela(conn, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conn.commit()

def inserir_registro(conn, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (?,?)", data)
    conn.commit()

#inserir_registro(conn, cursor, "Ivone Diello", "ivonecharao@gmail.com")


def atualizar_registro(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("update clientes set nome = ?, email = ? where id = ?", data)
    conn.commit()

#atualizar_registro(conn, cursor, "Eduarda Daou", "eduardadaou@gmail.com", 2)

def excluir_registro(conn, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conn.commit()

#excluir_registro(conn, cursor, 5)

def inserir_varios(conn, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conn.commit()

#dados = [
#    ("João Antônio", "joaocharao@gmail.com"), 
#    ("Leda Diello", "ledadiello@gmail.com"), 
#    ("Valdemar Borges", "valdemarborges@gmail.com")
#    ]

#inserir_varios(conn, cursor, dados)

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchall()

#cliente = recuperar_cliente(cursor, 1)

#print(cliente)

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    return cursor.fetchall()

#cliente = listar_clientes(cursor)

#print(cliente)