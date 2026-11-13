
import tkinter as tk

from database import clientes, planos, assinaturas

from dashboard import criar_dashboard

from clientes_planos import (
    cadastrar_cliente,
    cadastrar_plano,
    pesquisar_cliente
)

from assinaturas import (
    criar_assinatura,
    atualizar_assinatura
)

from relatorios import listar_dados


# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()

janela.title("Sistema de Faturamento")
janela.geometry("1000x600")
janela.minsize(850, 500)
janela.configure(bg="#F1F5F9")


# ==========================================
# MENU LATERAL
# ==========================================

menu_lateral = tk.Frame(
    janela,
    bg="#172554",
    width=220
)

menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)


tk.Label(
    menu_lateral,
    text="FATURAMENTO",
    bg="#172554",
    fg="white",
    font=("Arial", 17, "bold")
).pack(pady=30)


# ==========================================
# AREA DE CONTEUDO
# ==========================================

conteudo = tk.Frame(
    janela,
    bg="#F1F5F9"
)

conteudo.pack(
    side="right",
    fill="both",
    expand=True
)


# ==========================================
# CRIAR BOTOES DO MENU
# ==========================================

def criar_botao(texto, comando):

    tk.Button(
        menu_lateral,
        text=texto,
        command=comando,
        bg="#1E3A8A",
        fg="white",
        activebackground="#2563EB",
        activeforeground="white",
        font=("Arial", 11),
        relief="flat",
        cursor="hand2",
        height=2
    ).pack(
        fill="x",
        padx=15,
        pady=5
    )


# ==========================================
# NAVEGACAO DO SISTEMA
# ==========================================

criar_botao(
    "Dashboard",
    lambda: criar_dashboard(
        conteudo,
        clientes,
        planos,
        assinaturas
    )
)

criar_botao(
    "Cadastrar Cliente",
    cadastrar_cliente
)

criar_botao(
    "Cadastrar Plano",
    cadastrar_plano
)

criar_botao(
    "Pesquisar Cliente",
    pesquisar_cliente
)

criar_botao(
    "Criar Assinatura",
    criar_assinatura
)

criar_botao(
    "Atualizar Assinatura",
    atualizar_assinatura
)

criar_botao(
    "Relatórios",
    lambda: listar_dados(
        conteudo,
        clientes,
        planos,
        assinaturas
    )
)

criar_botao(
    "Sair",
    janela.destroy
)


# ==========================================
# INICIALIZACAO
# ==========================================

criar_dashboard(
    conteudo,
    clientes,
    planos,
    assinaturas
)

janela.mainloop()
