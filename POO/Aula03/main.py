# **Exercício Prático: Primeira Classe em Python (POO)**

# **Objetivo:** Criar e manipular sua primeira classe em Python, compreendendo na prática como funcionam os atributos, a instanciação de objetos e a execução de métodos.

# ---

# **Descrição da Atividade:**

# Você foi contratado para desenvolver a estrutura inicial de um sistema de cadastro. Para isso, você deve criar uma classe chamada `Pessoa` seguindo os passos abaixo:

# 1. **Definição da Classe e Atributos:**
# No método construtor `__init__`, inicialize a classe com **5 atributos**:
# * `nome` (texto)
# * `idade` (número inteiro)
# * `cpf` (texto)
# * `email` (texto)
# * `celular` (texto)


# 2. **Criação dos Métodos:**
# * `exibir_dados(self)`: Método que imprime na tela todos os 5 dados cadastrados da pessoa de forma organizada.
# * `alterar_celular(self, novo_celular)`: Método que recebe um novo número de telefone como parâmetro e atualiza o atributo `celular` do objeto.


# 3. **Código Principal (Teste prático):**
# * Crie (instancie) um objeto da classe `Pessoa` com dados fictícios.
# * Chame o método `exibir_dados()` para mostrar as informações iniciais.
# * Chame o método `alterar_celular(...)` passando um novo número.
# * Chame novamente o método `exibir_dados()` para confirmar se o número do celular foi realmente atualizado.



# ---

# **Exemplo de Saída Esperada no Console:**

# ```text
# --- DADOS DA PESSOA ---
# Nome: Ana Souza
# Idade: 20
# CPF: 123.456.789-00
# E-mail: ana.souza@email.com
# Celular: (51) 98888-1111

# Número de celular atualizado com sucesso!

# --- DADOS DA PESSOA ---
# Nome: Ana Souza
# Idade: 20
# CPF: 123.456.789-00
# E-mail: ana.souza@email.com
# Celular: (51) 99999-2222

# ```


class Pessoa:

    def exibir_dados(self):
        print("--- DADOS DA PESSOA ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Celular: {self.celular}")

    def alterar_celular(self, novo_celular):
        self.celular = novo_celular


# Criando o objeto
pessoa = Pessoa()

# Definindo os atributos
pessoa.nome = input("Digite seu nome: ")
pessoa.idade = int(input("Digite sua idade: "))
pessoa.cpf = int(input("Digite seu CPF: "))
pessoa.email = input("Digite seu email: ")
pessoa.celular = int(input("Digite seu Telefone: "))

# Mostrando os dados iniciais
pessoa.exibir_dados()

# Alterando o celular
pessoa.alterar_celular("(51) 99999-2222")
print("\nNúmero de celular atualizado com sucesso!\n")

# Mostrando os dados atualizados
pessoa.exibir_dados()


