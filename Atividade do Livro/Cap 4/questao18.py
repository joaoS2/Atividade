# Faça um programa que receba a idade de uma pessoa e mostre a mensagem de maioridade ou não.

#SOLUÇÃO: Receber uma idade e usar  if para comparar se a idade recebida é maior ou menor que 18 anos

#|DEfinição de variáveis|

idade : int

#|Entrada de Dados|

idade = int(input("Insira a sua idade: "))

#Processamento de Dados:

#Comparar se a idade inserida é maior que 18 anos
if idade >= 18:
    print("Maior de idade!")

else:
    print("Menor de idade!")