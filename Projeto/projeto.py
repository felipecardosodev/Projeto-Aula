#Projeto Aula 16/10
# Banco de dados em memória utilizando dicionários
clientes = {}
planos = {}
assinaturas = {}

def cadastrar_cliente():
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        if id_cliente < 0:
            raise ValueError("O ID não pode ser negativo.")
        if id_cliente in clientes:
            raise ValueError("Cliente já cadastrado.")
        nome = input("Digite o nome do cliente: ")
        clientes[id_cliente] = {
            "nome": nome
        }

    except ValueError as erro:
        print("Erro:", erro)
    else:
        print("Cliente cadastrado com sucesso!")
    finally:
        print("Operação de cadastro finalizada.\n")