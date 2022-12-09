import os
os.system("clear")
#Faça um programa para calcular e mostrar o salário reajustado de um funcionário. O percentual de aumento
#encontra-se na tabela a seguir.

#SALÁRIO              PErCENTuAL dE AuMENTo
#Até R$ 300,00               35%
#Acima de R$ 300,00          15% */

#definição de Variáveis:



salFuncionário : float
perAumento : float

perAumento = 0

#Entrada de Dados:

salFuncionário = float(input("Insira o seu salário: "))

os.system("clear")

#Processamento e Saída: 

#Verificar se o salário digitado é menor ou igual a R$ 300,00
if salFuncionário <= 300 : 
    perAumento = salFuncionário * 1.35
    print("O seu salário atende aos requisitos para o aumento de 35%!")
    print(f"O seu novo salário será de R$ {perAumento: .2f}")

#Verificar se o salário digitado é maior a R$ 300,00
if salFuncionário > 300 :
    perAumento = salFuncionário * 1.15
    print("O seu salário atende aos requisitos para o aumento de 15%!")
    print(f"O seu novo salário será de {perAumento: .2f}")
