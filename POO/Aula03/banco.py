class Conta:
    # Definição dos atributos(PRIMEIRA LETRA EM MAISUCULO)
    numero = 0
    saldo  = 0.0
    
    
# Inicio do programa
# Criação dos Objetos
mariana_conta=Conta()
mariana_conta.numero=123455463
mariana_conta.saldo=4000.00

daphine_conta=Conta()
daphine_conta.saldo=5000.00
daphine_conta.numero=6767676767

raphael_conta=Conta()
raphael_conta.numero=5454554545
raphael_conta.saldo=10000.00

###### Transferência de uma conta pra outra

raphael_conta.saldo-=100
mariana_conta.saldo+=100
print("****** Conta Mariana *******")
print(f"{mariana_conta.numero} {mariana_conta.saldo}")

print("\n****** Conta Raphael *******")
print(f"{raphael_conta.numero} {raphael_conta.saldo}")

raphael_conta.saldo-=100
daphine_conta.saldo+=100
mariana_conta.saldo-=100
daphine_conta.saldo+=100

print("\n****** Conta Mariana *******")
print(f"{mariana_conta.numero} {mariana_conta.saldo}")

print("\n****** Conta Raphael *******")
print(f"{raphael_conta.numero} {raphael_conta.saldo}")

print("\n****** Conta Mariana *******")
print(f"{mariana_conta.numero} {mariana_conta.saldo}")

print("\n****** Conta Daphine *******")
print(f"{daphine_conta.numero} {daphine_conta.saldo}")