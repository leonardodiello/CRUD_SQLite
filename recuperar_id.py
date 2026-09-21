from conexao_criar_tabela import cursor

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchall()

id = int(input("Digite o ID do cliente que deseja recuperar: "))

cliente = recuperar_cliente(cursor, id)

for cliente in cliente:
    print(f"ID: {cliente[0]}\nNome: {cliente[1]}\nEmail: {cliente[2]}\n")