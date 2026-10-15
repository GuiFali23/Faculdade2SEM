class Proprietario:
    def __init__(self, nome, cpf, telefone, email):
        self.nome=nome
        self.cpf=cpf
        self.telefone=telefone
        self.email=email

    def exibir_dados(self):
        print("=== DADOS DO PROPRIETÁRIO ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")

class Corretor:
    def __init__(self, nome, creci, percentual_comissao):
        self.nome = nome
        self.creci = creci
        self.percentual_comissao = percentual_comissao

    def vender_imovel(self, imovel, valor_final):
        imovel.alterar_status("Vendido")
        comissao = valor_final * (self.percentual_comissao / 100)
        print("=== VENDA REALIZADA ===")
        print(f"Imóvel: {imovel.codigo}")
        print(f"Valor da venda: R$ {valor_final:,.2f}")
        print(f"Corretor: {self.nome}")
        print(f"Percentual de comissão: {self.percentual_comissao}%")
        print(f"Comissão gerada: R$ {comissao:,.2f}")
        print()
        return comissao


class Imovel:
    status_permitidos = ["Disponível", "Alugado", "Vendido"]

    def __init__(self, codigo, endereco, tipo, valor, proprietario, corretor=None):
        self.codigo = codigo
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor
        self.status = "Disponível"
        self.proprietario = proprietario
        self.corretor = corretor

    def alterar_status(self, novo_status):
        if novo_status in self.status_permitidos:
            self.status = novo_status
            print(f"Status do imóvel {self.codigo} alterado para: {self.status}")
        else:
            print(
                f"Erro: status '{novo_status}' inválido. "
                f"Use: {', '.join(self.status_permitidos)}."
            )

    def exibir_ficha(self):
        print("========================================")
        print("           FICHA DO IMÓVEL")
        print("========================================")
        print(f"Código: {self.codigo}")
        print(f"Endereço: {self.endereco}")
        print(f"Tipo: {self.tipo}")
        print(f"Valor: R$ {self.valor:,.2f}")
        print(f"Status: {self.status}")
        print(f"Proprietário: {self.proprietario.nome}")

        if self.corretor is not None:
            print(f"Corretor: {self.corretor.nome}")
            print(f"CRECI: {self.corretor.creci}")
        else:
            print("Corretor: Não definido")

        print("========================================")
        print()


###############################################################################################


proprietario1 = Proprietario("Guilherme", "123", "40028922", "guigui@gmail.com")
proprietario2 = Proprietario("Bernardo", "456", "9676767676", "bebe@gmail.com")

corretor1 = Corretor( "Carlos Souza", "CRECI 12345", 6.0 )
corretor2 = Corretor( "Ana Santos", "CRECI 67890", 5.0 )

imovel1 = Imovel( 101, "Rua dos Andradas, 1000", "Apartamento", 450000.00, proprietario1, corretor1 )
imovel2 = Imovel( 102, "Av. Ipiranga, 2500", "Casa", 650000.00, proprietario2, corretor2 )
imovel3 = Imovel( 103, "Rua Padre Chagas, 500", "Apartamento", 800000.00, proprietario1, corretor1 )

###############################################################################################

proprietario1.exibir_dados() 
proprietario2.exibir_dados()


imovel1.exibir_ficha() 
imovel2.exibir_ficha() 
imovel3.exibir_ficha()


valor_venda = 440000.00

comissao = corretor1.vender_imovel( imovel1, valor_venda )

print("=== FICHA ATUALIZADA APÓS A VENDA ===") 
imovel1.exibir_ficha()


imovel2.alterar_status("Alugado")

print("=== FICHA DO IMÓVEL APÓS ALTERAÇÃO DE STATUS ===") 
imovel2.exibir_ficha()

imovel3.alterar_status("Reservado") 
imovel3.exibir_ficha()