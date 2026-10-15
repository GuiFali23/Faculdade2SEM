import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        peso = entry_peso.get().replace(",", ".")
        altura = entry_altura.get().replace(",", ".")

        if peso == "" or altura == "":
            messagebox.showwarning(
                "Atenção",
                "Por favor, preencha todos os campos."
            )
            return

        peso = float(peso)
        altura = float(altura)

        if peso <= 0 or altura <= 0:
            messagebox.showwarning(
                "Atenção",
                "O peso e a altura devem ser maiores que zero."
            )
            return

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade Grau I"
        elif imc < 40:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"

        label_resultado.config(
            text=f"IMC: {imc:.2f}\nClassificação: {classificacao}"
        )

    except ValueError:
        messagebox.showwarning(
            "Atenção",
            "Digite apenas números válidos para peso e altura."
        )


janela = tk.Tk()

janela.title("Calculadora de IMC")
janela.geometry("400x250")
janela.resizable(False, False)

label_peso = tk.Label(
    janela,
    text="Peso (kg):"
)

label_peso.grid(
    row=0,
    column=0,
    padx=20,
    pady=15
)

entry_peso = tk.Entry(
    janela,
    width=25
)

entry_peso.grid(
    row=0,
    column=1,
    padx=20,
    pady=15
)

label_altura = tk.Label(
    janela,
    text="Altura (m):"
)

label_altura.grid(
    row=1,
    column=0,
    padx=20,
    pady=15
)

entry_altura = tk.Entry(
    janela,
    width=25
)

entry_altura.grid(
    row=1,
    column=1,
    padx=20,
    pady=15
)

botao_calcular = tk.Button(
    janela,
    text="Calcular IMC",
    command=calcular_imc
)

botao_calcular.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=15
)

label_resultado = tk.Label(
    janela,
    text="IMC: --\nClassificação: --"
)

label_resultado.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=15
)

janela.mainloop()