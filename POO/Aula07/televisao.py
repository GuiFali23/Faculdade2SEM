# Atributos:

# modeloTV: String - representa o modelo da televisão
# canal: Inteiro - representa o canal atual
# volume: Inteiro - representa o volume atual
# estado: String - representa o estado da televisão ("ligada" ou "desligada")
# Métodos:

# __init__: método construtor (self, modeloTV)
#         self.modeloTV = modeloTV
# canal=0
# volume =0
# estado='desligada'
# ligar(): Liga a televisão e define o canal e volume para valores iniciais (especificar os valores iniciais)
# self.canal = 0
# self,volume = 10
# eslf.estado = 'ligada'
# desligar(): Desliga a televisão
# self.estado='desligada
# aumentarVolume(volume): Aumenta o volume em 1 unidade ou valor customizável
# Se volume is null:
# self.volume +=1
# else:
#            self.volume += volume
# diminuirVolume(volume): Diminui o volume em 1 unidade (ou valor customizável)
# Se volume is null:
# self.volume -=1
# else self.volume -= volume

# trocarCanal(novoCanal): Muda o canal para o novoCanal (especificar se o canal tem um limite máximo) ou adiciona 1 no canal
#                  quando for '+'  aumenta 1 do canal quando for '-' diminui 1 do canal  entre os limites 0 e 100

#                 quando for um número muda direto para o canal

#               if novoCanal.isdigit() and novoCanal()>0 and novoCanal <=100:

#                    self.canal = novoCanal

#               elif novoCanal == '+':

#                     self.canal +=1:

#                     if self.canal > 100:

#                          self.canal = 100

#               elif novoCanal == '-':

#                     self.canal -=1

#                      if self.canal < 0:

#                          self.canal = 0

#                else:

#                     print('Canal Inválido')









# estadoTV(): lista atributos do objeto da classe Televisão
# Instruções:

# Crie a classe Televisao com os atributos e métodos descritos.
# Implemente cada método de acordo com sua funcionalidade.
# Crie um objeto Televisao e utilize os métodos para testar a funcionalidade da classe.
# Demonstre como a classe pode ser utilizada em um programa simples, como um menu interativo para controlar a televisão.
# Dicas:

# Utilize comentários para explicar o código e facilitar a compreensão.
# Teste a classe com diferentes valores de entrada para garantir que ela funcione corretamente.
# Explore a possibilidade de adicionar outros atributos e métodos à classe, como controle de brilho, seleção de entrada (HDMI, antena, etc.) e ajuste de imagem.
# Observações:

# Este exercício é direcionado para alunos em introdução à Programação Orientada a Objetos.
# O nível de detalhamento da implementação pode variar de acordo com o conhecimento prévio dos alunos e da linguagem de programação utilizada.
# O professor pode fornecer instruções adicionais ou modificar o enunciado para atender às necessidades específicas da turma.



# modeloTV: String - representa o modelo da televisão
# canal: Inteiro - representa o canal atual
# volume: Inteiro - representa o volume atual
# estado: String - representa o estado da televisão ("ligada" ou "desligada")

class Televisao():
    def __init__(self, modelotv):
        self.modelotv = modelotv
        self.canal=0
        self.volume =0
        self.estado='desligada'

    def ligar(self):
        self.canal = 0
        self.volume = 10
        self.estado = 'ligada'

    def desligar(self): 
        self.estado='desligada'


    def aumentarVolume(self, volume):  
      if volume is None:
        self.volume +=1
      else:
        self.volume += volume

    def diminuirVolume(self, volume):
        if volume is None:
            self.volume -=1
        else: 
            self.volume -= volume

    def trocarCanal(self, novoCanal):
        if isinstance(novoCanal, int) and 0 <= novoCanal <= 100:
            self.canal = novoCanal

        elif novoCanal == '+':
            self.canal += 1

            if self.canal > 100:
                self.canal = 100

        elif novoCanal == '-':
            self.canal -= 1

            if self.canal < 0:
                self.canal = 0

        else:
            print('Canal Inválido')

    def estadoTV(self):
       print(f"Modelo: {self.modelotv}")
       print(f"Canal: {self.canal}")
       print(f"Volume: {self.volume}")
       print(f"Estado: {self.estado}")


#################################################################################


tv = Televisao("Samsung")

tv.estadoTV()


tv.ligar()

tv.aumentarVolume(5)

tv.trocarCanal(10)

print("\nDepois das alterações:")
tv.estadoTV()


tv.desligar()

print("\nDepois de desligar:")
tv.estadoTV()
