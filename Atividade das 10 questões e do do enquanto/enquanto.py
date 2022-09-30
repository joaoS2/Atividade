#variáveis
soma: int
soma = 0

#processamento
x = int(input("Digite um número (0 - SAIR): "))
while x != 0:
    soma = soma + x
    x = int(input("Digite um número (0 - SAIR): "))

#saída
print("Soma vale ", soma)