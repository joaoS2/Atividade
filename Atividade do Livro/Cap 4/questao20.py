import os
os.system("Clear")
# Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as regras a seguir.
# Para idade inferior a 5, deverá mostrar mensagem.
 
#CATEgoriA       idAdE
#Infantil        5 a 7
#Juvenil         8 a 10
#Adolescente     11 a 15
#Adulto          16 a 30
#Sênior          Acima de 30

#|DEfinição de variáveis|

idade : int

#|Entrada de Dados|

idade = int(input("Insira a sua idade: "))

#Processamento de Dados:

#Comparar a idade inserida e mostrar a categoria
if idade >= 5 and idade <= 7 :
    print("INFANTIL!")

elif idade >= 8 and idade <= 10:
    print("JUVENIL!")

elif idade >= 11 and idade <= 15:
    print("ADOLESCENTE!")

elif idade >= 16 and idade <= 30:
    print("ADULTO")
else: 
    print("SÊNIOR!")