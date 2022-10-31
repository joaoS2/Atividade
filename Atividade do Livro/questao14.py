import os

#14- Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião
#em relação ao filme: ótimo — 3; bom — 2; regular — 1. Faça um programa que receba a idade e a opinião
#de quinze espectadores, calcule e mostre:
#    || a média das idades das pessoas que responderam ótimo;
#    || a quantidade de pessoas que responderam regular; e
#    || a percentagem de pessoas que responderam bom, entre todos os espectadores analisados. 


#Definição de Variáveis:
idade : int; 
opniao: int;
mediaOtimo: float;
bom: int;
otimo: int;

regular = 0
bom = 0
otimo = 0
mediaOtimo = 0
porcentagemBom = 0
somaOtimo = 0

for n in range (1, 3 + 1):
    print(f"{n}ª pessoa!")
    idade = int(input("Insira a sua idade: "))
    opniao = int(input("Dê a sua avaliação em relação ao filme: ótimo — 3|bom — 2|regular — 1: "))

    if opniao == 1: 
        regular += 1

    if opniao == 2:
        bom += 1
        porcentagemBom = bom / 15 * 100

    if opniao == 3:
        otimo += 1
        somaOtimo += 1
        mediaOtimo = somaOtimo / otimo

print()
print("=" * 100)
print(f"A média das idades das pessoas que responderam Ótimo é: {mediaOtimo} ")
print("-"* 100)
print(f"A quantidade de pessoas que responderam regular é: {regular}")
print("-" * 100)
print(f"A percentagem de pessoas que responderam bom, entre todos os espectadores analisados é: {porcentagemBom}%")
print("=" * 100)