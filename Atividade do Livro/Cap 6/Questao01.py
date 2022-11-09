import os
os.system("clear")

#Declaração de variáveis:
numeros = []
pares = []
impares = []

qtdPares: int
qtdImpares: int 
qtdImpares = 0 
qtdPares = 0

#Entrada de dados;
for n in range (0, 6):
    numeros.append(int(input(f"Insira o {n + 1}º número: ")))

#Processamento de dados:
for n in range (0 , 6):
    if numeros[n] % 2 == 0:
        qtdPares += 1 
        pares.append(numeros[n])  
    else:
        qtdImpares +=1 
        impares.append(numeros[n])

os.system("clear")

#Saída de dados:
print(f"Os números pares são: {pares}")
print(f"A quantidade de números pares é: {qtdPares}")
print("")
print(f"Os números ímpares são: {impares}")
print(f"A quantidade de números ímpares é de: {qtdImpares}")