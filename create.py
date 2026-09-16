from conexao_criar_tabela import conn, cursor



def inserir_registro(conn, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (?,?)", data)
    conn.commit()

nome = input("Digite o nome do cliente que deseja cadastrar: ")
email = input("Digite o email do cliente: ")

inserir_registro(conn, cursor, nome, email)