#declaração de variáveis
anoInicial: int
percentual: float
novosalario: float
ano: int
salarioBase: int

#processameno de dados
import datetime
dataAtual = datetime.datetime.now()
anoAtutal = dataAtual.year
salarioBase = 1000.00
anoInicial = 2005
percentual = 0.5
ano = 2005
novosalario = 0

while ano < 2007:
    ano += 1
    novosalario = salarioBase +(salarioBase*percentual)

while ano <= 2007 and ano <= anoAtutal:
    ano += 1
    percentual *= 2
    novosalario += novosalario * percentual

#saída de dados
print(f"O salário atual é de: R${novosalario}")  