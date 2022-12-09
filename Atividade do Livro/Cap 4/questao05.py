import os 

os.system("clear")

#Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolhado usuário.

#1 Média entre os números digitados
#2 Diferença do maior pelo menor
#3 Produto entre os números digitados
#4 Divisão do primeiro pelo segundo
#Se a opção digitada for inválida, mostre uma mensagem de erro e termine a execução do programa.
#Lembre-se de que, na operação 4, o segundo número deve ser diferente de zero.

#Definição de variáveis:
num1 : float
num2 : float
escolha : int
media : float
diferença : float
produto : float
divisao : float

#Entrda de Dados (números):
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

os.system("clear")

#Tabela de escolhas:
print("Escolha do usuário!")
print("=" * 38)
print("1 Média entre os números digitados")
print("-" * 38)
print("2 Diferença do maior pelo menor")
print("-" * 38)
print("3 Produto entre os números digitados")
print("-" * 38)
print("4 Divisão do primeiro pelo segundo")
print("=" * 38)

#Escolha do usuário:
escolha = int(input("Insira o número correspondente a sua escolha:  "))

#Executando e verificando se o número digitado corresponde as opções:
if escolha >= 1 and escolha <= 4: 

#Caso ele escolha a opção 1:
    if escolha == 1: 
        media = (num1 + num2) / 2
        os.system("clear")
        print(f"A média dos dois produtos é de {media}")
#Caso ele escolha a opção 2:
    if escolha == 2:
        #Descobrir qual dos dois é o maior para poder fazer a diferença:
        if num1 > num2:
            diferença = num1 - num2
            os.system("clear")
            print(f"A diferença entre os dois números é {diferença}")
        if num2 > num1:
            #Fazend a diferença:
            diferença = num2 - num1
            os.system("clear")
            print(f"A diferença entre os dois números é {diferença}")
#Caso ele escolha a opção 2:
    if escolha == 3:
        os.system("clear")
        produto = num1 * num2 
        print(f"O produto dos números digitads é {produto}")
#Caso ele escolha a opção 2:
    if escolha == 4:
        #Verifica se o número é diferente de 0;
        if num2 != 0 :
            divisao = num1 / num2
            print(f"O resultado da divisão dos dois números é {divisao}")
        else:
            os.system("clear")
            print("ERRO! O número tem que ser diferente de 0!")
#Caso não exista o código, mostrar a mensagem.
else: 
    os.system("clear")
    print("Número inválido!")