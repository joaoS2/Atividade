import os

#Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um
#programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso
#ele não tenha direito ao aumento.

#Definição de Variáveis:

os.system("clear")

salFuncionario : float
salAumento : float

salAumento = 0

#Entradada de Dados:

salFuncionario = float(input("Insira o seu salário: "))

#Processamento e Saída de Dados:

#verificar se o salário do funcionário é menor que 500
if salFuncionario < 500 :
    salAumento = salFuncionario * 1.30
    os.system("clear")
    print(f"O seu salário final será de R$ {salAumento}.")
else:
    print("Seu salaŕio é superior a R$ 500,00! Você não possui direito ao aumento.")
