import os 
os.system("clear")

#O preço ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
#e dos impostos, ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a
#seguir. Faça um programa que receba o custo de fábrica de um carro e mostre o preço ao consumidor.

#Custo de Fábrica                     % do distrbuidor        % dos impostos
#Até R$ 12.000,00                               5                    isento
#Entre R$ 12.000,00 e R$ 25.000,00              10                    15
#Acima de R$ 25.000,00                          15                    20

#Definição de Variáveis:

valTotalVeiculo : float
custoFabrica : float
precoConsumidor : float

precoConsumidor = 0



#Entrada de Dados:

valTotalVeiculo = float(input("Insira o valor total do carro: "))
custoFabrica = float(input("Insira o valor de fábrica do carro: "))

#Saída

if custoFabrica <= 12000:
    precoConsumidor = valTotalVeiculo * 1.05
    print(F"Você foi isentado de impostos! Então, o preço fianal do veículo é R${precoConsumidor: .2F}")

if custoFabrica >= 12000 and precoConsumidor < 25000:
    precoConsumidor = valTotalVeiculo * (0.10  + 0.15)
    print("ooi")
    print(F"O preço fianal do veículo é R${precoConsumidor: .2F}.")

if custoFabrica > 25000:
    precoConsumidor = valTotalVeiculo * (0.15 + 0.20)
    print(F"O preço fianal do veículo é R${precoConsumidor: .2F}.")
    



