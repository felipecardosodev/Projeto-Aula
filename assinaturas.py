
from tkinter import simpledialog, messagebox

from database import clientes, planos, assinaturas


# ==========================================
# CRIAR ASSINATURA
# ==========================================

def criar_assinatura():

    try:
        id_cliente = simpledialog.askinteger(
            "Criar Assinatura",
            "Digite o ID do cliente:"
        )

        if id_cliente is None:
            return

        if id_cliente not in clientes:
            raise KeyError("Cliente não encontrado.")

        id_plano = simpledialog.askinteger(
            "Criar Assinatura",
            "Digite o ID do plano:"
        )

        if id_plano is None:
            return

        if id_plano not in planos:
            raise KeyError("Plano não encontrado.")

        # Gerar identificador
        id_assinatura = max(
            assinaturas.keys(),
            default=0
        ) + 1

        # Calcular valor
        valor_total = (
            planos[id_plano]["valor"] *
            planos[id_plano]["meses"]
        )

        # Armazenar assinatura
        assinaturas[id_assinatura] = {
            "cliente": id_cliente,
            "plano": id_plano,
            "valor_total": valor_total
        }

        messagebox.showinfo(
            "Sucesso",
            f"Assinatura criada!\n\n"
            f"ID: {id_assinatura}\n"
            f"Cliente: {clientes[id_cliente]['nome']}\n"
            f"Plano: {planos[id_plano]['nome']}\n"
            f"Valor total: R$ {valor_total:.2f}"
        )

    except KeyError as erro:
        messagebox.showerror("Erro", str(erro))

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores válidos."
        )


# ==========================================
# ATUALIZAR ASSINATURA
# ==========================================

def atualizar_assinatura():

    try:
        id_assinatura = simpledialog.askinteger(
            "Atualizar Assinatura",
            "Digite o ID da assinatura:"
        )

        if id_assinatura is None:
            return

        if id_assinatura not in assinaturas:
            raise KeyError("Assinatura inexistente.")

        novo_plano = simpledialog.askinteger(
            "Atualizar Assinatura",
            "Digite o novo ID do plano:"
        )

        if novo_plano is None:
            return

        if novo_plano not in planos:
            raise KeyError("Plano não encontrado.")

        # Atualizar plano
        assinaturas[id_assinatura]["plano"] = novo_plano

        # Recalcular valor
        assinaturas[id_assinatura]["valor_total"] = (
            planos[novo_plano]["valor"] *
            planos[novo_plano]["meses"]
        )

        messagebox.showinfo(
            "Sucesso",
            "Assinatura atualizada com sucesso!"
        )

    except KeyError as erro:
        messagebox.showerror("Erro", str(erro))

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores válidos."
        )
