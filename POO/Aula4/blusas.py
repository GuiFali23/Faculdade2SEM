class Blusao:

    def __init__(self, cor, tamanho, preco, possui_capuz, quantidade_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.possui_capuz = possui_capuz
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        print(f"Cor: {self.cor}")
        print(f"Tamanho: {self.tamanho}")
        print(f"Preço: R$ {self.preco:.2f}")

        if self.possui_capuz:
            print("Possui capuz: Sim")
        else:
            print("Possui capuz: Não")

        print(f"Quantidade em estoque: {self.quantidade_estoque}")

    def repor_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        print(f"Estoque atualizado: {self.quantidade_estoque}")


# ÁREA DE TESTE

produto = Blusao("Cinza", "G", 180.00, True, 4)

produto.exibir_informacoes()

produto.repor_estoque(6)

produto.exibir_informacoes()