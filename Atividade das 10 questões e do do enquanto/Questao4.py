a: float; b: float; c: float
a = int(input('Escreva um número: '))
b = int(input('Escreva um segundo número: '))
c = int(input('Escreva um terceiro número: '))

if a>b>c:
    print(f"A ordem crescente é: {c}, {b} e {a}")
elif a>c>b:
    print(f"A ordem crescente é: {b}, {c} e {a}")
elif b>a>c:
    print(f"A ordem crescente é: {c}, {a} e {b}")
elif b>c>a:
    print(f"A ordem crescente é: {a}, {c} e {b}")
elif c>a>b:
    print(f"A ordem crescente é: {b}, {a} e {c}")
else:
    print(f"A ordem crescente é: {a}, {b} e {c}")