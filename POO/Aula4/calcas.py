class Calca:

    def __init__(self, cor, tamanho, preco, tipo_tecido, quantidade_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.tipo_tecido = tipo_tecido
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        print(f"Cor: {self.cor}")
        print(f"Tamanho: {self.tamanho}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Tipo de tecido: {self.tipo_tecido}")
        print(f"Quantidade em estoque: {self.quantidade_estoque}")

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem / 100)
        self.preco = self.preco - desconto

        print(f"Novo preço com desconto: R$ {self.preco:.2f}")


# Área de teste

produto = Calca("Preta", 42, 120.00, "Jeans", 8)

produto.exibir_informacoes()

produto.aplicar_desconto(10)

produto.exibir_informacoes()