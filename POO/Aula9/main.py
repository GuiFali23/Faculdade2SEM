# Enunciado do Exercício:
# Crie um sistema simples de gerenciamento de uma transportadora utilizando programação orientada a objetos em Python.

# Requisitos:

# Classe Caminhão:
# Atributos: modelo, placa, capacidade_carga.
# Métodos: carregar(peso), descarregar(peso). O método carregar deve verificar se o peso a ser carregado não excede a capacidade do caminhão.
# Classe Motorista:
# Atributos: nome, idade, CNH. dataValidade
# Métodos: dirigir(caminhao). Este método deve imprimir uma mensagem indicando que o motorista está dirigindo o caminhão.
# verificarValidade(motorista)
# Associação entre as classes:
# Um caminhão deve ser dirigido por apenas um motorista.
# Um motorista pode dirigir vários caminhões.
# Exercícios:

# Crie pelo menos 3 objetos da classe Caminhão e 2 objetos da classe Motorista.
# Atribua um motorista a cada caminhão.
# Simule a carga e descarga de um caminhão.
# verifique se a CNH do Motorista é stá valida, caso estiver para vencer em 30 dias ou vencida verificar se o motorista está associado a um caminhão e avisar para renovar a CNH
# Imprima na tela informações sobre os caminhões e seus respectivos motoristas.
# Dicas:

# Utilize a associação entre as classes para conectar um objeto caminhão a um objeto motorista.
# Explore os métodos de cada classe para simular as ações da transportadora.
# Utilize a orientação a objetos para modelar o problema de forma clara e organizada.
# Exemplo de saída:

# Caminhão:Modelo: Mercedes BenzPlaca: AAA-1234Capacidade de carga: 10000 kgMotorista: João SilvaCarga atual: 5000 kgCaminhão:...
# Desafios:

# Adicione um atributo "carga_atual" à classe Caminhão para controlar o peso carregado.
# Implemente um método para calcular o frete de um transporte com base na distância e no peso da carga.
# Crie uma classe "Viagem" para armazenar informações sobre as viagens realizadas pelos caminhões.
# Este exercício tem como objetivo:

# Fortalecer a compreensão sobre a associação entre classes em Python.
# Aplicar os conceitos de programação orientada a objetos em um cenário real.
# Desenvolver a lógica de programação e a capacidade de resolver problemas.
# Bons estudos!

# Observações:

# Este enunciado pode ser adaptado para níveis de complexidade diferentes, adicionando mais classes, atributos e métodos.
# Incentive os alunos a utilizarem boas práticas de programação, como nomes de variáveis e funções significativos, comentários e formatação do código.
# Possíveis extensões:

# Adicionar uma classe "Cliente" para representar os clientes da transportadora.
# Implementar um sistema de login para os motoristas.
# Criar um relatório com as informações de todos os caminhões e motoristas.
# Com este exercício, os alunos poderão explorar os conceitos de orientação a objetos de forma prática e divertida, aplicando seus conhecimentos para criar um sistema simples, mas funcional.




class CNH:
    def __init__(self, data_validade):
        self.data_validade = data_validade

    def verificar_validade(self):
        print(f"A CNH é válida até {self.data_validade}")


class Caminhao:
    def __init__(self, modelo, placa, capacidade_carga, motorista):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.motorista = motorista
        self.carga_atual = 0

    def carregar(self, peso):
        if peso <= 0:
            print("Peso inválido!")
        elif self.carga_atual + peso <= self.capacidade_carga:
            self.carga_atual += peso
            print(f"{peso} kg carregados com sucesso!")
        else:
            print("Diminui o peso dessa bomba!")

    def descarregar(self, peso):
        if peso <= 0:
            print("Peso inválido!")
        elif peso <= self.carga_atual:
            self.carga_atual -= peso
            print(f"{peso} kg descarregados com sucesso!")
        else:
            print("Não é possível descarregar mais peso do que o caminhão possui!")


class Motorista:
    def __init__(self, nome, idade, cnh):
        self.nome = nome
        self.idade = idade
        self.cnh = cnh
        self.caminhoes = []

    def dirigir(self, caminhao):
        print(
            f"{self.nome} está dirigindo o caminhão "
            f"{caminhao.modelo} - {caminhao.placa}"
        )

    def verificar_validade(self):
        self.cnh.verificar_validade()


cnh1 = CNH("10/05/2027")
cnh2 = CNH("20/10/2026")


motorista1 = Motorista("João Silva", 35, cnh1)
motorista2 = Motorista("Maria Souza", 29, cnh2)


caminhao1 = Caminhao("Mercedes Benz","AAA-1234",10000,motorista1)

caminhao2 = Caminhao("Volvo FH","BBB-5678",15000,motorista2)

caminhao3 = Caminhao("Scania R450","CCC-9012",12000,motorista1)


motorista1.caminhoes.append(caminhao1)
motorista1.caminhoes.append(caminhao3)

motorista2.caminhoes.append(caminhao2)


caminhao1.carregar(5000)
caminhao1.carregar(3000)

caminhao1.descarregar(2000)


motorista1.dirigir(caminhao1)
motorista2.dirigir(caminhao2)


motorista1.verificar_validade()
motorista2.verificar_validade()


print("\n--- INFORMAÇÕES DOS CAMINHÕES ---")

for caminhao in [caminhao1, caminhao2, caminhao3]:
    print(f"\nModelo: {caminhao.modelo}")
    print(f"Placa: {caminhao.placa}")
    print(f"Capacidade: {caminhao.capacidade_carga} kg")
    print(f"Carga atual: {caminhao.carga_atual} kg")
    print(f"Motorista: {caminhao.motorista.nome}")





