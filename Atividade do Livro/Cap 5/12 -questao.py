#Definição de Variáveis:

numeros: int;
qtdNumPrimos: int; 
contadorPrimos : int;

qtdNumPrimos = 0
contadorDePrimos = 0
numPrimos = 0
#Entrada de Dados: 

for n in range (0 , 3):
    print("")
    print(f"{n + 1}º número!")
    numeros = int(input("Insira um número: "))

for m in range (2, numeros + 1):
    if numeros % m == 0:
        contadorDePrimos += 1

    if contadorDePrimos == 0 :
        numPrimos += 1

print("")

#Saída de Dados:

print(f"A quantidade de números primos é: {contadorDePrimos}")