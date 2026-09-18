from conexao_criar_tabela import cursor

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    return cursor.fetchall()

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)