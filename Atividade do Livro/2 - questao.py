from msvcrt import open_osfhandle


precoingresso = float
despesas: float
lucro: float
quantingressos: int

precoingresso = 5.00
quantiingressos = 120
despesas = 200

while precoingresso >= 1.00:
    lucro = quantiingressos * precoingresso - despesas
    print(f"|Preço: \t\t|R$ {precoingresso:.2f}") 
    print(f'|Lucro: \t\t|R${lucro:.2f}')
    print(f'|Ingressos vendido: \t|{quantiingressos}')
    print('_' * 34)
    quantiingressos = quantiingressos + 26
    precoingresso = precoingresso - 0.50