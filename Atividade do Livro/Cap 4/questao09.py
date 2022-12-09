import os
os.system("clear")


# Um banco concederá um crédito especial aos seus clientes, de acordo com o saldo médio no último ano. Faça
#um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a
#seguir. Mostre o saldo médio e o valor do crédito. 

# SALDO                 MÉDIO PERCENTUAL
#Acima de R$ 400,00      30% do saldo médio
#R$ 400,00 e R$ 300,00     25% do saldo médio
#R$ 300,00 e R$ 200,00     20% do saldo médio
#Até R$ 200,00           10% do saldo médio

#Definição de Variáveis: 

salMedioCliente: float
valCredito : float
valCredito = 0

#Entrada de Dados: 

salMedioCliente = float(input("Insira o  saldo médio de um cliente: "))

#Processamento de Dados:

if salMedioCliente > 400:
    valCredito = salMedioCliente * 1.30
    print(F"O seu saldo médio é de {salMedioCliente}, então você terá 30% de crédito.")
    print(f"O seu saldo será de {valCredito: .2f}")

if salMedioCliente <= 400 and salMedioCliente >= 300:
    valCredito = salMedioCliente * 1.25
    print(F"O seu saldo médio é de {salMedioCliente}, então você terá 25% de crédito.")
    print(f"O seu saldo será de {valCredito: .2f}")

if salMedioCliente <= 200:
    valCredito = salMedioCliente * 1.10 
    print(F"O seu saldo médio é de {salMedioCliente}, então você terá 10% de crédito.")
    print(f"O seu saldo será de {valCredito: .2f}")

