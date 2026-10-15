# #Função sem parâmetro e sem retorno

# def alo():
#     print("Hello World!!!")

# for i  in range(10):
#     alo() #chamda da função
# print("Fim do programa")


#Função com paramêtro sem retorno
# def alo(nome):
#     print(f"Olá, {nome}!")
#     print("Bem Vindo a POO!!")
#     if nome == "GABRIEL":
#         print("Você é um lindão")
# while True:
#     nome = input("Digite um nome: ").upper()
#     if nome == "Fim":
#         break
#     alo(nome)


# Função sem paramêtro com retorno d e valor
# def soma():
#     while True:
#         try:
#             n1 = int(input("Digite um valor: "))
#             n2 = int(input("Digite outro valor valor: "))
#             break
#         except:
#             print("Digite números inteiros")
#     return (n1+ n2)
# ############ INICIO DO PRO0GRAMA #################
# for i in range(5):
#     print(f"A soma é {soma()}")

# def soma(n1,n2):
#     return (n1+n2)

# def subtracao(n1,n2):
#     return (n1 - n2)

# def divisao(n1,n2):
#     return (n1 / n2)

# def multiplicacao(n1,n2):
#     return (n1 * n2)

# def potencia(n1,n2):
#     return (n1 ** n2)


# continua = "S"
# operacoes = ["+", "-", "/", "*", "**"]
# ############################################
# while True: ############### LOOP PRINCIPAL
#     if continua != "S":
#         break
#     while True:
#         try:
#             op = "k"
#             n1 = float(input("Digite um número: "))
#             while op not in operacoes:
#                 op = input("Digite uma operação (+ - / * **): " )
#                 if op not in operacoes:
#                     print("TEU ANIMAL DIGITA UMA OPERAÇÃO ❤️")
#             n2 = float(input("Digite outro número: "))
#             break
#         except:
#             print('Digite números inteiros!')
#     if op == '+':
#         print(f"soma {n1} + {n2} = {soma(n1,n2)}")
#     if op == '-':
#         print(f"subtração {n1} = {n2} = {subtracao(n1,n2)}")
#     if op == '/':
#         print(f"divisão {n1} / {n2} = {divisao(n1,n2)}")
#     if op == '*':
#         print(f"multiplicação {n1} * {n2} = {multiplicacao(n1,n2)}")
#     if op == '**':
#         print(f"potencia {n1} ** {n2} = {potencia(n1,n2)}")
#     continua=input('Continua (S/N):').upper()
# print('Tchau!')

# 📝 Exercício Prático: Calculadora de Desconto da
# ByteShop
# 🎯 Objetivo:
# Praticar a criação de funções em Python com parâmetros, retorno de valores e estruturas
# condicionais simples.
# 📄 Contexto do Problema:
# A loja de eletrônicos ByteShop está oferecendo descontos especiais para seus clientes. Para
# agilizar o atendimento no caixa, você foi contratado para criar um pequeno script em Python
# que calcule o valor final das compras após a aplicação do desconto.
# 💻 Requisitos do Exercício:
# 1. Crie uma função chamada calcular_desconto que receba dois parâmetros:
# ○ valor_compra (float): O valor total da compra em reais.
# ○ cupom (string): O código do cupom de desconto digitado pelo cliente.
# 2. Regras do Cupom de Desconto:
# ○ Se o cupom for "DESCONTO10", a função deve aplicar 10% de desconto sobre o valor
# da compra.
# ○ Se o cupom for "DESCONTO20", a função deve aplicar 20% de desconto sobre o valor
# da compra.
# ○ Se o cupom for qualquer outro valor (ou vazio), nenhum desconto deve ser aplicado
# (0%).
# 3. Retorno da Função:
# ○ A função deve calcular e retornar (return) apenas o valor final da compra já com o
# desconto aplicado.
# 4. Programa Principal (Testes):
# ○ Escreva um programa principal que chame a função pelo menos três vezes com valores
# e cupons diferentes e imprima o resultado na tela de forma organizada.

# 🌟 Desafio Extra (Opcional):
# Modifique a função para que ela também aceite cupons digitados em letras minúsculas (ex:
# "desconto10"), utilizando o método .upper() para tratar o texto


# Chamadas da função no programa principal:
# valor1 = calcular_desconto(100.0, "DESCONTO10")
# valor2 = calcular_desconto(200.0, "DESCONTO20")
# valor3 = calcular_desconto(150.0, "SEMDESCONTO")
# Impressão dos resultados:
# Compra de R$ 100.00 com 'DESCONTO10' -> Valor final: R$ 90.00
# Compra de R$ 200.00 com 'DESCONTO20' -> Valor final: R$ 160.00
# Compra de R$ 150.00 com 'SEMDESCONTO' -> Valor final: R$ 150.00