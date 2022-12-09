import os 

os.system("clear")

#-Faça um programa que receba três números 
#-e mostre o maior.

#Definicão de Variáveis: 
num1 : float
num2 : float
num3 : float

#Entrda de Dados (números):
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

#Verificar qual dos dois números é o menor:

os.system("clear")

if num1 > num2 and num1 > num3:
    print(f"O maior número dentre os três é o número {num1}")

if num2 > num1 and num2 > num3:
    print(f"O maior número dentre os três é o número {num2}")

if num3 > num1 and num3 > num2:
    print(f"O maior número dentre os três é o número {num3}")