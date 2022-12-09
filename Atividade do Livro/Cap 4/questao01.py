#Faça um programa que receba quatro notas de um aluno
#calcule e mostre a média aritmética das notas e a
#mensagem de aprovado ou reprovado, considerando para aprovação média 7.

import os 

os.system("clear")

#definição de Variáveis: 

nota1 : float
nota2 : float
nota3 : float
nota4 : float
media : float

#Entrada de Dados(notas dos alunos):

nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
nota3 = float(input("Insira a terceira nota do aluno: "))
nota4 = float(input("Insira a quarta nota do aluno: "))

#Cálculo da média (somae todas as notas e dividir pela quantidade de notas):
media = (nota1 + nota2 + nota3 + nota4) / 4

#Verificação para saber se ele foi aprovado ou reprovado 

os.system("clear")

if media >= 7:
    print("Parabéns, você foi aprovado!")
else:
    print("Infelizmente você não alcançou a pontuação para ser aprovado")