from email.errors import InvalidBase64CharactersDefect
from stringprep import in_table_d2


faixetaria1 : int
faixetaria2 : int
faixetaria3 : int
faixetaria4 : int
faixetaria5 : int
idade : int

faixetaria1 = 0
faixetaria2 = 0
faixetaria3 = 0
faixetaria4 = 0
faixetaria5 = 0

for n in range(1,9):
    idade =int(input('Insira sua idade: '))

    if idade <= 15 :
        faixetaria1 = faixetaria1 + 1
    elif idade > 15 and idade <= 30:
        faixetaria2 = faixetaria2 + 1
    elif idade > 30 and idade <= 45:
        faixetaria3 = faixetaria3 + 1
    elif idade > 45 and idade <= 60:
        faixetaria4 = faixetaria4 + 1
else:
    faixetaria5 = faixetaria5 + 1

print(f'|faxetaria 1 (até 15 anos): {faixetaria1}')
print("=" * 30)
print(f'|faxetaria 2 (até 30 anos): {faixetaria2}')
print("=" * 30)
print(f'|faxetaria 3 (até 45 anos): {faixetaria3}')
print("=" * 30)
print(f'|faxetaria 4 (até 60 anos): {faixetaria4}')
print("=" * 30)
print(f'|faxetaria 5 (acima de 60 anos): {faixetaria5}')
print("=" * 30)
print(f'|A porcentagem de pessoas {faixetaria1/8*100}%')
print("=" * 30)
print(f'|A porcentagem de pessoas {faixetaria5/8*100}%')
print("=" * 30)