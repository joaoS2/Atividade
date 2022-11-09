import os

#Declaração de Variáveis: 
numeros = []
multDe2 = []
multDe3 = []
multDe2E3 = []

os.system("clear")

#Entrada de Dados:
for n in range(0,7):
    numeros.append(int(input(f"Insira o {n + 1}º número: ")))

#Processamento de Dados:
for n in range(0,7):
    #Verificar se o número é multiplo de 2
    if numeros[n] % 2 == 0:
        multDe2.append(numeros[n])

    #Verificar se o número é multiplo de 3
    if numeros[n] % 3 == 0:
        multDe3.append(numeros[n])
        
    #Verificar se o número é multiplo de 2 e de 3
    if numeros[n] % 2 == 0 and numeros[n] % 3 == 0:
       multDe2E3.append(numeros[n])
      

os.system("clear") 

#Saída de Dados:
print("=" * 100)
print(f"Os números multiplos de 2 são: →{multDe2}←")
print("»" * 100)
print(f"Os números multiplos de 3 são: →{multDe3}←")
print("»" * 100)
print(f"Os números multiplos de 2 e 3 são: →{multDe2E3}←")
print("=" * 100)
