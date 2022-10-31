import os
c: str
compra: float; cv: float; cp: float; ct:float
compra = 0
cv = 0
cp = 0

c = ""

for n in range(1,16):
    print(f'Dados da {n}ª venda')

    while(c != "V" and c != "P" ):
        c = input('Digite o código da compra (V - à vista ou P - à prazo): ').upper()    
        if c =="V" :
            compra = float(input('Digite um valor da compra: R$'))
            cv = cv + compra
        elif c == "P" :
            compra = float(input('Digite o valor da compra: R$'))
            cp + cp + compra
    c = ""       
    os.system('cls')

print(f'O valor total à vista: R$ {cv:.2f}')
print(f'O valor total à prazo: R$ {cp:.2f}')
print(f'O valor total das compras: R$ {cp + cv:.2f}')
print(f'O valor da primeira prestação das compras a prazo juntas: R$ {cp/3:.2f}')