
import tkinter as tk
from tkinter import simpledialog, messagebox

from database import clientes, planos


# ==========================================
# CADASTRAR CLIENTE
# ==========================================

def cadastrar_cliente():

    try:
        id_cliente = simpledialog.askinteger(
            "Cadastrar Cliente",
            "Digite o ID do cliente:"
        )

        if id_cliente is None:
            return

        if id_cliente < 0:
            raise ValueError("ID não pode ser negativo.")

        if id_cliente in clientes:
            raise ValueError("Cliente já cadastrado.")

        nome = simpledialog.askstring(
            "Cadastrar Cliente",
            "Digite o nome do cliente:"
        )

        if nome is None:
            return

        if not nome.strip():
            raise ValueError("Nome inválido.")

        clientes[id_cliente] = {
            "nome": nome.strip()
        }

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

    except ValueError as erro:
        messagebox.showerror("Erro", str(erro))


# ==========================================
# CADASTRAR PLANO
# ==========================================

def cadastrar_plano():

    try:
        id_plano = simpledialog.askinteger(
            "Cadastrar Plano",
            "Digite o ID do plano:"
        )

        if id_plano is None:
            return

        if id_plano < 0:
            raise ValueError("ID inválido.")

        if id_plano in planos:
            raise ValueError("Plano já cadastrado.")

        nome = simpledialog.askstring(
            "Cadastrar Plano",
            "Digite o nome do plano:"
        )

        if nome is None:
            return

        if not nome.strip():
            raise ValueError("Nome inválido.")

        valor = simpledialog.askfloat(
            "Cadastrar Plano",
            "Digite o valor mensal:"
        )

        if valor is None:
            return

        meses = simpledialog.askinteger(
            "Cadastrar Plano",
            "Digite a quantidade de meses:"
        )

        if meses is None:
            return

        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")

        if meses <= 0:
            raise ValueError("Quantidade de meses inválida.")

        planos[id_plano] = {
            "nome": nome.strip(),
            "valor": valor,
            "meses": meses
        }

        messagebox.showinfo(
            "Sucesso",
            "Plano cadastrado com sucesso!"
        )

    except ValueError as erro:
        messagebox.showerror("Erro", str(erro))


# ==========================================
# PESQUISAR CLIENTE
# ==========================================

def pesquisar_cliente():

    try:
        id_cliente = simpledialog.askinteger(
            "Pesquisar Cliente",
            "Digite o ID do cliente:"
        )

        if id_cliente is None:
            return

        if id_cliente not in clientes:
            raise KeyError("Cliente não cadastrado.")

        nome = clientes[id_cliente]["nome"]

        messagebox.showinfo(
            "Cliente Encontrado",
            f"ID: {id_cliente}\nNome: {nome}"
        )

    except KeyError as erro:
        messagebox.showerror("Erro", str(erro))

    except ValueError:
        messagebox.showerror("Erro", "Digite um ID válido.")
