import sqlite3

# Criando o banco de dados e a tabela
conn = sqlite3.connect('cadastros.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastros (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
''')
conn.commit()

# Função para cadastrar um novo cliente
def cadastrar_cliente(nome, cpf, endereco):
    cursor.execute('INSERT INTO cadastros (nome, cpf, endereco) VALUES (?, ?, ?)', (nome, cpf, endereco))
    conn.commit()
    print('Cliente cadastrado com sucesso!')

# Função para listar todos os clientes cadastrados
def listar_clientes():
    cursor.execute('SELECT * FROM cadastros')
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

# Função para atualizar as informações de um cliente
def atualizar_cliente(id, nome, cpf, endereco):
    cursor.execute('UPDATE cadastros SET nome=?, cpf=?, endereco=? WHERE id=?', (nome, cpf, endereco, id))
    conn.commit()
    print('Informações do cliente atualizadas com sucesso!')

# Função para buscar um cliente pelo id
def buscar_cliente_por_id(id):
    cursor.execute('SELECT * FROM cadastros WHERE id=?', (id,))
    cliente = cursor.fetchone()
    if cliente:
        return cliente
    else:
        print('Cliente não encontrado')


# Interface do usuário
while True:
    print('1 - Cadastrar cliente')
    print('2 - Listar clientes')
    print('3 - Atualizar informações de um cliente')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        nome = input('Digite o nome do cliente: ')
        cpf = input('Digite o CPF do cliente: ')
        endereco = input('Digite o endereço do cliente: ')
        cadastrar_cliente(nome, cpf, endereco)
    if opcao == '3':
        id = input('Digite o ID do cliente que deseja atualizar: ')
        cliente = buscar_cliente_por_id(id)
        if cliente:
            nome = input('Digite o novo nome do cliente: ')
            cpf = input('Digite o novo CPF do cliente: ')
            endereco = input('Digite o novo endereço do cliente: ')
            atualizar_cliente(id, nome, cpf, endereco)
    elif opcao == '2':
        print('Clientes cadastrados:')
        listar_clientes()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
        
conn.close()