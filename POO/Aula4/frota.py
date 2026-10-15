class Veiculo():
    # Self define os atributos do objeto
    
    
    # Método __init__ = Método construtor
    def __init__(self,marca,modelo,ano,motor,velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.velocidade = velocidade
        
        
    # Método listar    
    def listar(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Motor: {self.motor}")
        print(f"velocidade: {self.velocidade}\n{'em movimento' if self.velocidade>0 else 'parado'}\n")
        
        
    def acelerar(self):
        if self.velocidade >= 150:
            print(f"Alcançou o Limite Máximo!!!{self.velocidade}")
        else:
            self.velocidade+=10
                    
    def freiar(self):
                self.velocidade -= 10
                
    def troca_motor(self):
        motor_novo = input("Motor novo: ")
        self.motor = motor_novo                
        
# Função do programa (fora da classe)    
def entrada_de_dados():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    motor = input("Motorização: ")
    velocidade = int(input("Velocidade: "))
    return marca,modelo,ano,motor, velocidade
##################### INICIO

# Chama função do programa para entrada dos dados

marca,modelo,ano,motor,velocidade = entrada_de_dados()
# Cria objeto
fusca = Veiculo(marca,modelo,ano,motor,velocidade)
fusca.listar()
print("ACELERANDO!!!")
for i in range(14):   
    fusca.acelerar()
fusca.listar()
print("FREIANDO!!!")
for i in range(12):
    fusca.freiar()   
fusca.listar()

fusca.troca_motor()
fusca.listar()