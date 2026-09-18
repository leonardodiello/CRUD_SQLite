from conexao_criar_tabela import conn, cursor

def excluir_registro(conn, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conn.commit()
    
id = int(input("Digite o ID do cliente que deseja excluir: "))

excluir_registro(conn, cursor, id)