import tkinter as tk
from tkinter import messagebox
from datetime import datetime



def calcular_idade():
    ano_atual = datetime.now().year
    ano_nascimento = entry_ano.get()


    if ano_nascimento == "":
        messagebox.showwarning(
            "Atenção",
            "Por favor, informe o ano de nascimento."
        )
        return

    
    if not ano_nascimento.isdigit():
        messagebox.showwarning(
            "Atenção",
            "Digite apenas números para o ano de nascimento."
        )
        return

    ano_nascimento = int(ano_nascimento)

   
    if ano_nascimento > ano_atual:
        messagebox.showwarning(
            "Atenção",
            "O ano de nascimento não pode ser maior que o ano atual."
        )
        return

    
    idade = ano_atual - ano_nascimento

  
    label_resultado.config(
        text=f"Você tem {idade} anos."
    )



janela = tk.Tk()

janela.title("Cálculo de Idade")
janela.geometry("400x220")



label_ano = tk.Label(
    janela,
    text="Informe o ano de nascimento:"
)

label_ano.grid(
    row=0,
    column=0,
    padx=10,
    pady=20
)



entry_ano = tk.Entry(
    janela,
    width=20
)

entry_ano.grid(
    row=0,
    column=1,
    padx=10,
    pady=20
)



botao_calcular = tk.Button(
    janela,
    text="Calcular Idade",
    command=calcular_idade
)

botao_calcular.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)



label_resultado = tk.Label(
    janela,
    text="Você tem X anos"
)

label_resultado.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=20
)



janela.mainloop()