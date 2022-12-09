import os 
os.system("clear")

#-Faça um programa que receba dois números 
#-mostre o menor.

#Definição de Variáveis: 

num1 : float
num2 : float

#Entrda de Dados (números):
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

#Verificar qual dos dois números é o menor:

os.system("clear")

if num1 > num2:
    print(f"O maior número é o número {num1}")

if num2 > num1:
    print(f"O maior número é o número {num2}")