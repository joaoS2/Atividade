import math

#Definição de Variáveis:

num : int;
somaPares: int;
somaPrimos: int ;
contadorDePrimos: int; 

somaPares = 0 
somaPrimos = 0 
contadorDePrimos = 0 

#Entrada de Dados:
for n in range (1, 10 + 1):
    num = int(input("Insira um némero: "))
    if num % 2 == 0:
        somaPares += num

for m in range (1,int(math.sqrt (num) + 1)):
    if num % m == 0:
        contadorDePrimos += 1

    if contadorDePrimos == 0:
        somaPrimos += num

print("=" * 30)
print(f"A soma de números pares é: {somaPares}")
print("-" * 30)
print(f"A soma de números primos é: {somaPrimos}")
print("=" * 30)