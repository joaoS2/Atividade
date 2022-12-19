#Faça um programa que receba o preço de um produto e seu código de origem e mostre sua procedência.
#A procedência obedece à tabela a seguir.
#CÓDIGO DE ORIGEM    ProCEdêNCiA
#1                   Sul
#2                   Norte
#3                   Leste
#4                   Oeste
#5 ou 6              Nordeste
#7 ou 8 ou 9         Sudeste
#10 a 20             Centro-oeste
#21 a 30             Nordeste

#Definição de Variáveis: 

#Definição de Variávies:

precoProduto : float
codPoduto : int

#Entrada de Dados:

precoProduto = float(input("Insira o preço do produto: "))
codPoduto = int(input("Insira o código do produto: "))

#Processamento: 

#Verificar se o código inserido é igual ao código de origem usando a comparação

if codPoduto == 1:
    print("O produto pertence a região Sul")

if codPoduto == 2:
    print("O produto pertence a região Norte")

if codPoduto == 3:
    print("O produto pertence a região Leste")

if codPoduto == 4:
    print("O produto pertence a região Oeste")

if codPoduto == 5 or codPoduto == 6:
    print("O produto pertence a região Nordeste")

if codPoduto == 7 or codPoduto == 8 or codPoduto == 9:
    print("O produto pertence a região Sudeste")
    
if codPoduto >= 10 and codPoduto <= 20 :
    print("O produto pertence a região centro-Oeste")
    
if codPoduto >= 21 and codPoduto <= 30 :
    print("O produto pertence a região Nordeste")
    