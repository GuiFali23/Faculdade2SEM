class Veiculo:
    marca =""
    modelo=""
    ano=0
    motor= ""
    velocidade = 0
    
    def listar(self):
        print(f"Marca {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Ano {self.ano}")
        print(f"Motor {self.motor}")
        print(f"velocidade {self.velocidade}\n{'em movimento' if self.velocidade>0 else 'parado'}\n")
        
        
    def acelerar(self):
        if self.velocidade >= 150:
            print(f"Alcançou o Limite Máximo!!!{self.velocidade}")
        else:
            self.velocidade+=10
            
    def freiar(self):
        self.velocidade -= 10
        
    
fusca = Veiculo()
fusca.marca = "volkswagen"
fusca.modelo = "2 portas"
fusca.ano = 1978
fusca.motor = "Gasolina 1300"

fusca.listar()

for i in range(16):
    fusca.acelerar()
    
fusca.listar()

for i in range(12):
    fusca.freiar()
fusca.listar()
