#Declaração de variáveis
import math
conjunto1: float
conjunto2: float
quadrado1: float
quadrado1: float
cubo1: float
cubo2: float
raiz1: float
raiz2: float

#Entrada de dados
print("="*15)
print("Programa Tabela")
print("="*15)
print("Quando você digitar um numero menor ou igual a zero o programa não se repetirà.")
conjunto1 = float(input("Digie algum valor para a tabela 1: "))
conjunto2 = float(input("Digite ouro valor para a ttabela 2: "))

#Processamento de dados
quadrado1 = conjunto1 ** 2
cubo1 =  conjunto1 ** 3
raiz1 = math.sqrt(conjunto1)
quadrado2 = conjunto2 ** 2
cubo2 =  conjunto2 ** 3
raiz2 = math.sqrt(conjunto2)
print("="*120)

#Saída de dados
while conjunto1 >0 and conjunto2 >0:
    print(f"Valor inicial 1: {conjunto1} | Valor elevado ao quadrado: {quadrado1} | Valor elevado ao cubo: {cubo1} | Raiz quadrada do valor: {round(raiz1,2)}")
    print("_"*120)
    print(f"Valor inicial 2: {conjunto2} | Valor elevado ao quadrado: {quadrado2} | Valor elevado ao cubo: {cubo2} | Raiz quadrada do valor: {round(raiz2,2)}")
    print("="*120)
    conjunto1 = float(input("Digie algum valor para a tabela 1: "))
    conjunto2 = float(input("Digite ouro valor para a tabela 2: "))
    print("="*120)