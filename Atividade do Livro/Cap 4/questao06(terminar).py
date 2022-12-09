import os
import math

#Faça um programa que receba dois números e
#execute uma das operações listadas a seguir, de acordo com a escolha do usuário.
#Se for digitada uma opção inválida, mostre mensagem de erro e termine a execução do programa. 
#As opções são:
#a) O primeiro número elevado ao segundo número.
#b) Raiz quadrada de cada um dos números.
#c) Raiz cúbica de cada um dos números. 

#Definição de Variáveis: 
num1 : float
num2 : float
opcaoA : float
raizQuadrada1 : float
raizQuadrada2 : float
escolhaUsuario: str
raizCubica1 : float
raizCubica2 : float


os.system("clear")

#Entrda de Dados (números):
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

os.system("clear")

#Tabela das escolhas:
print("=" * 50)
print("a)",  end="")
print(" O primeiro número elevado ao segundo número.")
print("-" * 50)
print("b)",  end="")
print(" Raiz quadrada de cada um dos números.")
print("-" * 50)
print("c)",  end="")
print(" Raiz cúbica de cada um dos números.")
print("=" * 50)

#Escolha do usuário:
escolhaUsuario = input("Insira a sua escolha (a-b-c): ").upper

#Verifica se o código inserido existe

if escolhaUsuario == "A":
    #Fazendo a exponenciação 
    opcaoA = num1 ** num2
    os.system("clear")
    print(f"O resultado da exponenciação do primeiro pelo segundo é {opcaoA}")

elif escolhaUsuario == "B":
    raizQuadrada1 = math.pow(num1, 1/2)
    raizQuadrada2 = math.pow(num2 , 1/2)
    print(f"A raíz quadrada de {num1} é {raizQuadrada1}")
    print("")
    print(f"A raíz quadrada de {num2} é {raizQuadrada2}")

elif escolhaUsuario == "C":
    raizCubica1 = math.pow(num1, 1/3)
    raizCubica2 = math.pow(num2 , 1/3)
    print(f"A raíz quadrada de {num1} é {raizCubica1}")
    print("")
    print(f"A raíz quadrada de {num2} é {raizCubica2}")
    
else:
    os.system("clear")
    print("ERRO! A opção escolhida não existe.")


