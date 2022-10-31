#Definição de Variáveis:

import os

os.system("cls")


valorCarro: float;
precoAVista : float;
valorParelas: float;
qtdParcelas: int;
taxaJuros : float;

taxaJuros = 0.03
valorCarro = 0.0
preçoAVista = 0.0


#Entrada de Dados:

valorCarro = float(input("Insira o valor do carro: "))

#Processamento e Saída de Dados:

precoAVista = valorCarro - (valorCarro * 0.20)

print("QUANTIDADE DE PARÇELAS - PERCENTUAL DE JUROS")
print("")
for n in range (6 , 60 , 6) :
    print("=" * 6)
    print(f"{n}x")
    print(f"{valorCarro + valorCarro * taxaJuros}")
    taxaJuros = taxaJuros + 0.03