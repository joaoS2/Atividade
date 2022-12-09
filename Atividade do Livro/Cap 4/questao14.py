import os
os.system("clear")

#Faça um programa que receba o salário de um funcionário e
#usando a tabela a seguir, calcule e mostre
#o novo salário.
 
#FAIXA SALARIAL             % DE AUMENTO
#Até R$ 300,00               50%
#R$ 300,00 R$ 500,00         40%
#R$ 500,00 R$ 700,00         30%
#R$ 700,00 R$ 800,00         20%
#R$ 800,00 R$ 1.000,00       10%
#Acima de R$ 1.000,00        5%


#Definição de Variáveis:

salFuncionario: float
salAumento: float

#Entrada de Dados:
salFuncionario = float(input("Insira o salário do funcionário: "))

os.system("clear")

#Processamento de Dados:

if salFuncionario <= 300: 
    print("=" * 50)
    print("Porcentagem de aumento de 50%")
    print("")
    salAumento = salFuncionario * 1.5
    print(f"O seu salário com o aumento será de R${salAumento: .2f}")
    print("=" * 50)
    print("")

elif salFuncionario > 300 and salFuncionario <= 500 :
    print("=" * 50)
    print("Porcentagem de aumento de 40%")
    print("")
    salAumento = salFuncionario * 1.4
    print(f"O seu salário com o aumento será de R${salAumento: .2f}")
    print("=" * 50)
    print("")

elif salFuncionario > 500 and salFuncionario <= 700:
    print("=" * 50)
    print("Porcentagem de aumento de 30%")
    print("")
    salAumento = salFuncionario * 1.3
    print(f"O seu salário com o aumento será de R${salAumento: .2f}")
    print("=" * 50)
    print("")

elif salFuncionario > 700 and salFuncionario <= 800:
    print("=" * 50)
    print("Porcentagem de aumento de 20%")
    print("")
    salAumento = salFuncionario * 1.2
    print(f"O seu salário com o aumento será de R${salAumento: .2f}")
    print("=" * 50)
    print("")

elif salFuncionario > 800 and salFuncionario <= 1000:
    print("=" * 50)
    print("Porcentagem de aumento de 10%")
    print("")
    salAumento = salFuncionario * 1.1
    print(f"O seu salário com o aumento será de R${salAumento: .2f}")
    print("=" * 50)
    print("")

else:
    print("=" * 50)
    print("Porcentagem de aumento de 5%")
    print("")
    salAumento = salFuncionario * 1.05
    print(f"O seu salário com o aumento será de R${salAumento: .2f}")
    print("=" * 50)
    print("")