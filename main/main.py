
import tkinter as tk

# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()

janela.title("Sistema de Faturamento")

janela.geometry("1000x600")

janela.configure(bg="#F1F5F9")


# ==========================================
# MENU LATERAL
# ==========================================

menu_lateral = tk.Frame(
    janela,
    bg="#172554",
    width=220
)

menu_lateral.pack(
    side="left",
    fill="y"
)

menu_lateral.pack_propagate(False)


tk.Label(
    menu_lateral,
    text="FATURAMENTO",
    bg="#172554",
    fg="white",
    font=("Arial", 17, "bold")
).pack(pady=30)


# ==========================================
# AREA PRINCIPAL
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


tk.Label(
    conteudo,
    text="Sistema de Assinaturas",
    bg="#F1F5F9",
    fg="#172554",
    font=("Arial", 24, "bold")
).pack(pady=100)


# ==========================================
# INICIALIZACAO
# ==========================================

janela.mainloop()
