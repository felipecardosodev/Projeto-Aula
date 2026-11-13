
import tkinter as tk


def criar_dashboard(conteudo, clientes, planos, assinaturas):

    # Limpar conteudo anterior
    for widget in conteudo.winfo_children():
        widget.destroy()

    # Titulo
    tk.Label(
        conteudo,
        text="Painel de Controle",
        bg="#F1F5F9",
        fg="#172554",
        font=("Arial", 23, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 5))

    tk.Label(
        conteudo,
        text="Gerenciamento de clientes, planos e assinaturas",
        bg="#F1F5F9",
        fg="#64748B",
        font=("Arial", 11)
    ).pack(anchor="w", padx=30)

    # Area dos cards
    cards = tk.Frame(conteudo, bg="#F1F5F9")
    cards.pack(fill="x", padx=20, pady=35)

    # Criar cards
    def criar_card(titulo, quantidade, cor):

        card = tk.Frame(
            cards,
            bg="white",
            padx=25,
            pady=25,
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        tk.Label(
            card,
            text=titulo,
            bg="white",
            fg="#64748B",
            font=("Arial", 11)
        ).pack()

        tk.Label(
            card,
            text=str(quantidade),
            bg="white",
            fg=cor,
            font=("Arial", 27, "bold")
        ).pack(pady=10)

    # Indicadores
    criar_card("Clientes", len(clientes), "#2563EB")
    criar_card("Planos", len(planos), "#0D9488")
    criar_card("Assinaturas", len(assinaturas), "#7C3AED")

    # Mensagem
    tk.Label(
        conteudo,
        text="Bem-vindo ao Sistema de Faturamento!",
        bg="#F1F5F9",
        fg="#172554",
        font=("Arial", 15, "bold")
    ).pack(anchor="w", padx=30, pady=20)

    tk.Label(
        conteudo,
        text="Utilize o menu lateral para acessar as funcionalidades.",
        bg="#F1F5F9",
        fg="#64748B",
        font=("Arial", 11)
    ).pack(anchor="w", padx=30)
