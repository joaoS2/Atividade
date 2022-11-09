import os 

idade: int; idade50: int; alturaentre10e20: int; peso40:int; qtdcad: int
altura: float; peso: float; somaaltura: float

idade50 = 0
altura = 0
somaaltura = 0
alturaentre10e20 = 0
peso40 = 0
qtdcad = 0

os.system('cls')
qtdcad = int(input('Informe a quantidade de cadastros a serem realizados'))


for n in range (1,  qtdcad + 1):
    print(f'Informe os dados para {qtdcad} pessoas')
    print("="* 31)
    print(f"{n}º pessoa")
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    
    if idade > 50:
        idade50 += 1
    if idade >=10 and idade <= 20:
        somaaltura += altura
        alturaentre10e20 += 1
    if peso < 40:
        peso40 += 1

print(f'Existem {idade50} com idade acima de 50 anos')
if alturaentre10e20 <= 0:
    print('Não existem pessoas com média de altura')
else:
    print(f'A média das aluras entre 10 e 20 {somaaltura/alturaentre10e20:.2f}')
print(f'Porcentagem de pessoas que tem o peso inferior de 40kg {peso40/qtdcad*100}%')