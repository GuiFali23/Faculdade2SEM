class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.pedidos = []  # Lista para armazenar os pedidos associados a este cliente

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        # Estabelecendo a associação bidirecional (se desejado)
        if pedido.cliente != self:
            pedido.cliente = self

    def exibir_informacoes(self):
        print(f"Cliente: {self.nome} (CPF: {self.cpf})")
        if self.pedidos:
            print("Pedidos:")
            for pedido in self.pedidos:
                print(f"- ID: {pedido.id}, Data: {pedido.data}, Valor Total: R$ {pedido.valor_total:.2f}")
        else:
            print("Nenhum pedido realizado.")
class Itens:
    def __init__(self,cod,nome,qtd,valor):
        self.cod=cod
        self.nome=nome
        self.qtd=qtd
        self.valor=valor





class Pedido:
    contador_id = 1

    def __init__(self, data,cliente=None):
        self.id = Pedido.contador_id
        Pedido.contador_id += 1
        self.data = data
        self.valor_total = 0
        self.cliente = cliente  # Referência ao cliente que fez o pedido
        self.itens=[] #lista de itens
        # Estabelecendo a associação bidirecional (se o cliente for fornecido)
        if cliente:
            cliente.adicionar_pedido(self)

    def exibir_detalhes(self):
        print(f"Detalhes do Pedido ID: {self.id}")
        print(f"Data: {self.data}")

        if self.cliente:
            print(f"Cliente: {self.cliente.nome}")
        else:
            print("Cliente não associado.")
        total = 0
        for i in self.itens:
            print(f' Código: {i.cod}\n Nome: {i.nome}\n Quantidade: {i.qtd}\n Valor: {i.valor}\n TOTAL= {i.qtd*i.valor}')
            total+=i.qtd*i.valor
        print(f"Valor Total: R$ {self.valor_total:.2f}\n")
        # print(f'Total Pedido {total}')
    def adicionar_item(self,item):
        self.itens.append(item)
        totalItem=item.qtd * item.valor
        self.valor_total+=totalItem

# Exemplo de uso:
if __name__ == "__main__":
    # Criando clientes
    cliente1 = Cliente("Ana Souza", "123.456.789-00")
    cliente2 = Cliente("Pedro Alves", "987.654.321-11")
    item1=Itens(123,'Mouse',1,39.90)
    item2=Itens(2424,'Teclado',3,50.40)
    item3=Itens(677, "Monitor", 1, 799.99 )
    item4=Itens(244,"MousePad", 1, 29.99)
    item5=Itens(171,"RAM16GB", 2, 4000)


    # Criando pedidos e associando aos clientes
    pedido1 = Pedido("2025-04-10", cliente1)
    pedido1.adicionar_item(item1)
    pedido1.adicionar_item(item2)
    pedido1.adicionar_item(item4)
    pedido1.exibir_detalhes()


    pedido2 = Pedido("2025-04-05", cliente1)
    pedido2.adicionar_item(item3)
    pedido2.adicionar_item(item2)
    pedido2.adicionar_item(item4)
    pedido2.exibir_detalhes()


    pedido3 = Pedido("2025-04-08",  cliente2)
    pedido3.adicionar_item(item2)
    pedido3.adicionar_item(item5)
    pedido3.adicionar_item(item3)
    pedido3.exibir_detalhes()



    pedido4 = Pedido("2025-04-01") # Pedido sem cliente inicial
    # Associando um pedido a um cliente posteriormente
    cliente2.adicionar_pedido(pedido4)
    pedido4.adicionar_item(item5)
    pedido4.exibir_detalhes()
    #  pedido4.cliente = cliente2 # Garantindo a bidirecionalidade


    print("--- Informações dos Clientes ---")
    cliente1.exibir_informacoes()
    print("\n")
    cliente2.exibir_informacoes()
    print("\n")

    print("--- Detalhes dos Pedidos ---")
    pedido1.exibir_detalhes()
    print("\n")
    pedido3.exibir_detalhes()
    print("\n")
    pedido4.exibir_detalhes()
