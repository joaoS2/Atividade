import os

#Definição de Variáveis:

numCanal: int
numESpectadores: int
porAudiencia: int
canal4: int
canal5 : int
canal7 : int
canal12 : int
porAudiencia4 : float
porAudiencia5:float
porAudiencia7 : float
porAudiencia12 : float


canal4 = 0
canal5 = 0 
canal7 = 0
canal12 = 0
numCanal = 1
os.system("clear")
#Entrada de Dados:
while numCanal != 0:
    numCanal = int(input("Insira o número do canal fornecido (4, 5, 7, 12): "))
    if numCanal != 0 :
        numESpectadores = int(input("Insira o número de pessoas assitindo o canal: "))
#Processamento:
    if numCanal == 4:
        canal4 += numESpectadores
    if numCanal == 5:
        canal5 += numESpectadores
    if numCanal == 7:
        canal7 += numESpectadores
    if numCanal == 12:
        canal12 += numESpectadores

porAudiencia4 = canal4 / numESpectadores
porAudiencia5 = canal5 / numESpectadores
porAudiencia7 = canal7 / numESpectadores
porAudiencia12 = canal12 / numESpectadores
os.system("clear")
#Saída
print("=" * 50,"|" )
print(f"A porcentagem de audiência do canal 4 é: {porAudiencia4}")
print("-" * 50,"|" )
print(f"A porcentagem de audiência do canal 5 é: {porAudiencia5}")
print("-" * 50,"|")
print(f"A porcentagem de audiência do canal 7 é: {porAudiencia7}")
print("-" * 50,"|")
print(f"A porcentagem de audiência do canal 12 é: {porAudiencia12}")
print("=" * 50,"|")