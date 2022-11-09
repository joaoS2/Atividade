
#Definição de Variáveis:

idade: int; 
peso: float;

mediaPesosFaixa1a10: float
mediaPesosFaixa11a20: float
mediaPesosFaixa21a30: float
mediaPesosFaixa31Acima: float

somaPesosFaixa1a10: float
somaPesosFaixa11a20: float
somaPesosFaixa21a30: float
somaPesosFaixa31Acima: float

qtdPesosFaixa1a10: float
qtdPesosFaixa11a20: float
qtdPesosFaixa21a30: float
qtdPesosFaixa31Acima: float

mediaPesosFaixa1a10 = 0
mediaPesosFaixa11a20 = 0
mediaPesosFaixa21a30 = 0
mediaPesosFaixa31Acima = 0

somaPesosFaixa1a10 = 0
somaPesosFaixa11a20 = 0
somaPesosFaixa21a30 = 0
somaPesosFaixa31Acima = 0

qtdPesosFaixa1a10 = 0
qtdPesosFaixa11a20 = 0
qtdPesosFaixa21a30 = 0
qtdPesosFaixa31Acima = 0

#Entrada de Dados:

for n in range (1,15 + 1):
    print(f"Dados da {n}ª pessoa!")
    idade = int(input("Insira a sua idade: "))
    peso = float(input("Insira o seu peso: "))

if idade >= 1 and idade <= 10:
    qtdPesosFaixa1a10 += 1
    somaPesosFaixa1a10 += 1

if idade >= 11 and idade <= 20:
    qtdPesosFaixa11a20 += 1
    somaPesosFaixa11a20 += 1

if idade >= 21 and idade <= 31:
    qtdPesosFaixa21a30 += 1
    somaPesosFaixa21a30 += 1

if idade > 31:
    qtdPesosFaixa31Acima += 1
    somaPesosFaixa31Acima += 1

#Processamento e Saída:
if qtdPesosFaixa1a10 > 0:
    mediaPesosFaixa1a10 = qtdPesosFaixa1a10 / somaPesosFaixa11a20
    print(f"A média de pessoas com faixa de 1 a 10 anos é: {mediaPesosFaixa1a10}")
else:
    print("Não ouve ninguém com a faxetária de 1 a 10 anos!")

if qtdPesosFaixa11a20 > 0:
    mediaPesosFaixa11a20 = qtdPesosFaixa11a20 / somaPesosFaixa11a20
    print (f"A média de pessoas com faixa de 11 a 20 anos é: {mediaPesosFaixa11a20}")
else: 
    print("Não ouve ninguém com a faxetária de 11 a 20 anos!")

if qtdPesosFaixa21a30 > 0:
    mediaPesosFaixa21a30 = qtdPesosFaixa21a30 / somaPesosFaixa21a30
    print (f"A média de pessoas com faixa de 21 a 30 anos é: {mediaPesosFaixa21a30}")
else:
    print("Não ouve ninguém com a faxetária de 21 a 30 anos!")

if qtdPesosFaixa31Acima > 0:
    mediaPesosFaixa31Acima = qtdPesosFaixa31Acima / somaPesosFaixa31Acima
    print(f"A média de pessoas com faixa de 21 a 30 anos é: {mediaPesosFaixa31Acima}")
else:
    print("Não ouve ninguém acima de 31 anos de idade!")