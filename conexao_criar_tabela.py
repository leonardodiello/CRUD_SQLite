import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

nome_banco = os.getenv("nome_banco")

conn = sqlite3.connect(f"{nome_banco}")

cursor = conn.cursor()

def criar_tabela(conn, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conn.commit()