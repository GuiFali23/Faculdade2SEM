import tkinter as tk

janela2= tk.Tk()
janela2.title("Pagina auxiliar")
janela2.geometry("100x100")

janela = tk.Tk()
janela.title("Minha primeira janela Tkinter")
janela.geometry("400x300")

label_boas_vindas=tk.Label(janela)
label_boas_vindas.pack(pady=20)
label_local= tk.Label(janela, text="UNISENAC")
label_local.pack(pady=20)
label_nome=tk.Label(janela, text="Guilherme")
label_nome.pack(pady=10)

label_auxiliar = tk.Label(janela2, text="Aqui janela 2")
label_auxiliar.pack(pady=20)

#Abre a janela
janela.mainloop()
janela2.mainloop()