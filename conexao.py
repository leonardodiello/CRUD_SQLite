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

def atualizar_registro(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("update clientes set nome = ?, email = ? where id = ?", data)
    conn.commit()

atualizar_registro(conn, cursor, "Eduarda Daou", "eduardadaou@gmail.com", 2)