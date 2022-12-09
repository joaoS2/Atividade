import os 
os.system(("cls"))

#Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação

#             PERCENTUAL DE AUMENTO
#===============================================
# |Salário  |                      |Porcentagem|
#  ──────────                       ─────────────
# Até R$ 50,00                        5%
#───────────────────────────────────────────
#Entre R$ 50,00 e R$ 100,00           10%
#───────────────────────────────────────────
#Acima de R$ 100,00                   15%
#===============================================

#                  CLASSIFICAÇÕES
#===================================================|
# |NOVO PREÇO |                  |CLASSIFICAÇÃO|    |
#───────────────────────────────────────────────────|
# Até R$ 80,00                        BARATO        |
#───────────────────────────────────────────────────|
#Entre R$ 80,00 e R$ 120,00 (INCLUSIVE)  NORMAL     |
#───────────────────────────────────────────────────| 
#Entre R$ 120,00 e R$ 200,00 (inclusive)  CARO      | 
#───────────────────────────────────────────────────| 
#Maior que R$ 200,00                   MUITO CARO   |
#===================================================|

#Definição de Variáveis:

preco : float
precoAumentado : float

#Entrada de dados:

preco = float(input("Insira o preço do produto: "))

os.system("cls")

#Processamento:

if preco >= 50:
    print("=" * 50)
    print("Porcentagem de aumento de 5%")
    precoAumentado = preco * 1.05
    print("")
    print(f"O novo preço do produto será de {precoAumentado: .2f}")
    print("=" * 50)
    print("")

elif preco > 50 and preco < 100:
    print("")
    print("Porcentagem de aumento de 10%")
    precoAumentado = preco * 1.10
    print(f"O novo preço do produto será de {precoAumentado: .2f}")
    print("")
    print("")

else:
    print("")
    print("Porcentagem de aumento de 15%")
    precoAumentado = preco * 1.15
    print("")
    print(f"O novo preço do produto será de {precoAumentado: .2f}")
    print("=" * 50)
    print("")

if preco <= 80:
    print("=" * 50)
    print("Classificação:")
    
    print("Está barato!")
    print("=" * 50)

elif preco > 80 and preco > 120:
    print("=" * 50)
    print("Classificação")
    
    print("Preço Normal!")
    print("=" * 50)
    

elif preco > 120 and preco < 200:
    print("=" * 50)
    print("Classificação")
    
    print("Está caro!")
    print("=" * 50)

else:
    print("=" * 50)
    print("Classificação")
    
    print("Está muito caro!")
    print("=" * 50)
