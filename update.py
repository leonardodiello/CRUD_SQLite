from conexao_criar_tabela import conn, cursor

def atualizar_registro(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("update clientes set nome = ?, email = ? where id = ?", data)
    conn.commit()

nome = input("Digite o nome do cliente que deseja atualizar: ")
email = input("Digite o email do cliente: ")
id = int(input("Digite o ID do cliente que deseja atualizar: "))

atualizar_registro(conn, cursor, nome, email, id)