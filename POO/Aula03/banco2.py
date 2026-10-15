# Definição de classe
class Conta():
    numero=0
    saldo=0
    # Definição de método(função que o objeto vai chamar)    
    def abertura(self,numero,saldo):
        self.numero = numero
        self.saldo = saldo
        print('Conta aberta com sucesso!!')
        
    def listar(self):
        print("\n*************************")
        print(f"Número{self.numero}")
        print(f"Saldo{self.saldo}")
# Incio do programa
# Criar estâncias dos Objetos

mariana_cc=Conta()
raphael_cc=Conta()
daphine_cc=Conta()
    
mariana_cc.abertura(1213131232113, 4000)
raphael_cc.abertura(416426414126, 10000)
daphine_cc.abertura(6767676767, 5000)
mariana_cc.listar()
daphine_cc.listar()
raphael_cc.listar()