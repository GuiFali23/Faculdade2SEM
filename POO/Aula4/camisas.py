# Objetivo: Praticar a criação de classes em Python, uso do construtor __init__, atributos de
# instância e métodos com validação condicional.
# Contexto:
# Você foi encarregado de desenvolver o módulo de controle de camisas para o sistema de uma
# loja de roupas. O sistema deve permitir o cadastro de novas peças, a visualização dos dados e
# o registro de vendas com baixa no estoque.
# Requisitos:
# 1. Crie a classe Camisa.
# 2. No método construtor __init__, defina e inicialize os seguintes atributos:
# ○ cor (texto)
# ○ tamanho (texto: "P", "M", "G", "GG")
# ○ preco (número decimal)
# ○ tipo_gola (texto: ex: "Gola Polo", "Gola V", "Gola Redonda")
# ○ quantidade_estoque (número inteiro)
# 3. Implemente os seguintes métodos na classe:
# ○ exibir_informacoes(): Mostra na tela todos os dados da camisa de forma organizada.
# ○ vender(quantidade): Recebe a quantidade de peças a serem vendidas. Se houver
# estoque suficiente, realiza a subtração e exibe o estoque restante; caso contrário, exibe
# uma mensagem avisando que o estoque é insuficiente.


# 4. Área de Teste:
# ○ Crie um objeto da classe Camisa (ex: cor "Azul", tamanho "M", preço 79.90, gola "Polo",
# estoque 10).
# ○ Chame o método exibir_informacoes().
# ○ Realize uma venda válida (ex: 3 unidades).
# ○ Tente realizar uma venda com quantidade maior do que o estoque disponível para testar
# a validação.

# O sistema deve permitir o cadastro de novas peças, a visualização dos dados e
# o registro de vendas com baixa no estoque.
golas = []
class Camisa:
    def __init__(self,cor,tamanho,preco,tipo_gola,qtd_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.tipo_gola = tipo_gola
        self.qtd_estoque = qtd_estoque
        
    def exibir_informacoes(self):
        print(f"Cor:  {self.cor}")
        print(f"Tamanho:  {self.tamanho}")
        print(f"Preço:  {self.preco}")
        print(f"Tipo de Gola:  {self.tipo_gola}")
        print(f"Quantidade em estoque:  {self.qtd_estoque}")
        
        
    def vender_quantidade(self):
        if self.qtd_estoque > 0:
            self.qtd_estoque -= 1
            print("Venda realizada!")
        else:
            print("FORA DE ESTOQUE!!!")
            


produto = Camisa("Azul", "M", 79.90, "Polo", 0)

produto.exibir_informacoes()

produto.vender_quantidade()

produto.exibir_informacoes()