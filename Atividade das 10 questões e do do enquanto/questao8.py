import math


print("1.Somar dois números")
print("2.Raíz quadrada de um número")
a= int(input("Digite a opção desejada; "))
if a == 1:
    numbSom1= float(input("Digite o primeiro número: "))
    numbSom2= float(input("Digite o segundo número: "))
    soma = numbSom1 + numbSom2
    print(f"A soma dos números é: {soma}")
else:
    numR = float(input("Digite um número: "))
    raiz = math.sqrt(numR)
    print (f"A raiz quadrada é: {round(raiz,2)}")