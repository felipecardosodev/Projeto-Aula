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

def cadastrar_plano():
    try:
        id_plano = int(input("Digite o ID do plano: "))
        if id_plano < 0:
            raise ValueError("ID inválido.")
        if id_plano in planos:
            raise ValueError("Plano já cadastrado.")
        nome = input("Nome do plano: ")
        valor = float(input("Valor mensal: "))
        meses = int(input("Quantidade de meses: "))
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        if meses <= 0:
            raise ValueError("Quantidade de meses inválida.")

        planos[id_plano] = {
            "nome": nome,
            "valor": valor,
            "meses": meses
        }

    except ValueError as erro:
        print("Erro:", erro)
    else:
        print("Plano cadastrado com sucesso!")
    finally:
        print("Operação de plano finalizada.\n")