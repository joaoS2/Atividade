#declaração de variáveis
salCarlos: float
salJoao: float
mes: int
mes = 0

#entrada de dados
salCarlos = float(input("Digite o salário do funcionário Carlos: "))

#processamento de dados
salJoao = salCarlos / 3
while salJoao <= salCarlos:
    mes += 1
    salCarlos *= 1.02
    salJoao *= 1.05

#saída de dados
print(f"A qunatidade de meses é: {mes}, o salário de Carlos virou: {round(salCarlos,2)} e o salário de João virou: {round(salJoao,2)}")