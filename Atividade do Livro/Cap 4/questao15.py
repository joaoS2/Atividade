import os 
os.system("clear") 
 
 #Uma agência bancária possui dois tipos de investimentos, conforme o quadro a seguir.
#Faça um programa que receba o tipo de investimento e seu valor,
#calcule e mostre o valor corrigido após um mês de investimento, de acordo com o tipo de investimento.
 
#TIPO        DESCRIÇÃO               RENDIMENTO MENsAL
#1           Poupança                3%
#2           Fundos de renda fixa    4%

#Definiçã de Variáveis:

tipoInvestimento : int
valorInvestimento : float
valorCorrigido : float

tipoInvestimento = 0

print("TIPOS   |    DESCRIÇÃO            |   RENDIMENTO MENsAL")
print("─────────────────────────────────────────────────────────")
print("1       |    Poupança             |        3%")
print("─────────────────────────────────────────────────────────")
print("2       |    Fundos de renda fixa |        4% ")
print("─────────────────────────────────────────────────────────")

#Entrada de dados:

valorInvestimento = float(input("Insira o valor investido: "))
tipoInvestimento = int(input("Insira o tipo de investimento de acordo com a tabela acima (1─2): "))

#Processamento: 
if tipoInvestimento == 1:
    valorCorrigido = valorInvestimento * 1.03
    os.system("clear")
    print(f"O seu rendimento mensal será de R$ {valorCorrigido: .2f}")

elif tipoInvestimento == 2:
    valorCorrigido = valorInvestimento * 1.04
    os.system("clear")
    print(valorCorrigido)


