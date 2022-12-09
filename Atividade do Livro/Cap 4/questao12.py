import os 
os.system("clear")

#Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir,
#calcule e mostre o valor a receber.
#Sabe-se que este é composto pelo salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.

#SALÁRIO                         GRATIFICAÇÃO
#Até R$ 350,00                   R$ 100,00
#R$ 350,00 R$ 600,00             R$ 75,00
#R$ 600,00 R$ 900,00             R$ 50,00
#Acima de R$ 900,00              R$ 35,00


#Definição de Variáveis:

salario : float
salAcressimo : float
imposto : float

#Entrada de Dados:

salario = float(input("Insira o seu salário: "))

os.system("clear")

#Processamento:

if salario <= 350:
    #Faz o acressimo calculando o salário e somando mais 100
    salAcressimo = salario + 100
    #o imposto irá receber o salário com um 7% em cima
    imposto = salario * 0.07
    #Subtrai o acressimo pelo imposto
    salAcressimo -= imposto
    print(f"O seu novo salário será de R$ {salAcressimo}")

elif salario > 350 and salario < 600:
    salAcressimo = salario + 75
    imposto = salario * 0.07
    salAcressimo -= imposto
    print(f"O seu novo salário será de R$ {salAcressimo}")

elif salario >= 600 and salario <= 900:
    salAcressimo = salario + 50
    imposto = salario * 0.07
    salAcressimo -= imposto
    print(f"O seu novo salário será de R$ {salAcressimo}")

else:
    salAcressimo = salario + 35
    imposto = salario * 0.07
    salAcressimo -= imposto
    print(f"O seu novo salário será de R$ {salAcressimo}")
