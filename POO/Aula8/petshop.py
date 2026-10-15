class Tutor:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def exibir_dados(self):
        print(f"*"*20, "TUTOR", "*"*20)
        print(f"Tutor: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print("*"*47,"\n")


class Pet:
    def __init__(self,nome, especie,tutor):
        self.nome=nome
        self.especie=especie
        self.tutor=tutor
    def exibir_ficha_veterinaria(self):
        print(f"*"*20, "PET", "*"*20)
        print(f"Nome do Pet: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Tutor: {self.tutor.nome}\nTelefone: {self.tutor.telefone}")
        self.tutor.exibir_dados()
        

tutor1=Tutor("Giovanne", "51 40028922") 
pet1=Pet("Jorge", "Cachorro", tutor1)
pet1.exibir_ficha_veterinaria()
