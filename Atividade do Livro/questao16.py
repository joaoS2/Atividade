import os

# Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas.
# Finalize digitando idade igual a zero.

#Definição de Variáveis:
idade: int;
somaIdade: int;
contadorIdade: int;
mediaIdade: int;

idade = 1
somaIdade = 0
contadorIdade = 0 
mediaIdade = 0

#Entrada de dados e somatório das idades;
os.system("clear")
while idade != 0:

    idade = int(input("Insira a sua idade (finalize digitando idade igual a zero): "))

    somaIdade += idade
    contadorIdade += 1

#Calculo das médias:
mediaIdade = somaIdade / (contadorIdade - 1)

os.system("clear")

#Saída:
print(f"A média das idades é: {mediaIdade:.2f}")