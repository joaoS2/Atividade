import os 
os.system("clear")

#Faça um programa que receba o salário atual de um funcionário e, usando a tabela a seguir,
#calcule e mostre o valor do aumento e o novo salário.

#SALÁRIO                  PERCENTUAL DE AUMENTO
#Até R$ 300,00                     15%
#R$ 300,00 R$ 600,00               10%
#R$ 600,00 R$ 900,00               5%
#Acima de R$ 900,00                0%

#Definição de3 Variáveis;
salFuncionario : float
perAumento : float

#Entrada de Dados:
salFuncionario = float(input("Insira o seu salário atual: "))

os.system("clear")

#Processamento:

if salFuncionario <= 300:
    perAumento = salFuncionario * 1.15
    print("Você receberá um aumento de 15%.")
    print(f"O seu novo salário será de R$ {perAumento: .2f}.")

elif salFuncionario > 300 and salFuncionario < 600:
    perAumento = salFuncionario * 1.10
    print("Você receberá um aumento de 10%.")
    print(f"O seu novo salário será de R$ {perAumento: .2f}.")

elif salFuncionario >= 600 and salFuncionario <= 900:
    perAumento = salFuncionario * 0.5
    print("Você receberá um aumento de 50%.")
    print()
    print(f"O seu novo salário será de R$ {perAumento: .2f}")
    print("─" * 40)

elif salFuncionario > 900:
    print("Você não receberá um aumento!")


