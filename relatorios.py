
import tkinter as tk
from tkinter import ttk


# ==========================================
# LISTAR DADOS DO SISTEMA
# ==========================================

def listar_dados(conteudo, clientes, planos, assinaturas):

    # Limpar tela anterior
    for widget in conteudo.winfo_children():
        widget.destroy()

    # Titulo
    tk.Label(
        conteudo,
        text="Relatórios e Registros",
        bg="#F1F5F9",
        fg="#172554",
        font=("Arial", 22, "bold")
    ).pack(anchor="w", padx=30, pady=25)

    # Criar tabela
    tabela = ttk.Treeview(
        conteudo,
        columns=("id", "tipo", "nome", "detalhes"),
        show="headings"
    )

    tabela.heading("id", text="ID")
    tabela.heading("tipo", text="TIPO")
    tabela.heading("nome", text="NOME")
    tabela.heading("detalhes", text="DETALHES")

    tabela.column("id", width=80)
    tabela.column("tipo", width=130)
    tabela.column("nome", width=180)
    tabela.column("detalhes", width=300)

    tabela.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    # ======================================
    # LISTAR CLIENTES
    # ======================================

    for id_cliente, dados in clientes.items():

        tabela.insert(
            "",
            "end",
            values=(
                id_cliente,
                "Cliente",
                dados["nome"],
                "-"
            )
        )

    # ======================================
    # LISTAR PLANOS
    # ======================================

    for id_plano, dados in planos.items():

        tabela.insert(
            "",
            "end",
            values=(
                id_plano,
                "Plano",
                dados["nome"],
                f"R$ {dados['valor']:.2f} / "
                f"{dados['meses']} meses"
            )
        )

    # ======================================
    # LISTAR ASSINATURAS
    # ======================================

    for id_assinatura, dados in assinaturas.items():

        nome_cliente = clientes[
            dados["cliente"]
        ]["nome"]

        nome_plano = planos[
            dados["plano"]
        ]["nome"]

        tabela.insert(
            "",
            "end",
            values=(
                id_assinatura,
                "Assinatura",
                nome_cliente,
                f"{nome_plano} - "
                f"R$ {dados['valor_total']:.2f}"
            )
        )
