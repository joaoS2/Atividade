#-Faça um programa que receba duas notas,
#-calcule e mostre a média aritmética e
#-a mensagem que se encontra na tabela a seguir: 

#Definição de Variáveis:

nota1 : float
nota2 : float
mediaAritmedica : float

#Entrda de Dados (notas do aluno)
nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))

#Cálculo da média do aluno (somar as notas e dividir pela quantidade delas): 

mediaAritmedica = (nota1 + nota2) / 2

if mediaAritmedica >= 0 and mediaAritmedica < 3:
    print("Reprovado")

if mediaAritmedica >= 3 and mediaAritmedica < 7:
    print("Exame")

if mediaAritmedica >= 7 and mediaAritmedica == 10:
    print("aprovado")