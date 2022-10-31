a:int
b:int
c:int
d:int

n:int
m1:int
m2:int
m3:int
m4:int

m1 = 0
m2 = 0
m3 = 0
m4 = 0

for n in range(1,6):
    print(f'Digite valores para grupo {n}: ')
    a = int(input('Digite um valor para A: '))
    b = int(input('Digite um valor para B: '))
    c = int(input('Digite um valor para C: '))
    d = int(input('Digite um valor para D: '))



    if a > b and a > c and a > d:
        m1 = a
        if b > c and b > d:
            m2 = b
            if c > d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        elif c > d and c > d:
            m2 = c
            if b > d:
                m3 = b
                m4 = d
            else:
                m3 = d
                m4 = b
        elif d > c and d > b:
            m2 = d
            if c > b:
                m3 = c
                m4 = d
        else:
            m3 = d
            m4 = c
    if b > a and b > c and b > d:
        m1 = b
        if a > c and a > d:
            m2 = a
            if c > d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        elif c > a and c > d:
            m2 = c 
            if a > d:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
        elif d > a and d > c:
            m2 = d
            if a > c:
                m3 = a
                m4 = c
        else:
            m3 = c
            m4 = a
    if c > a and c > b and c > d:
        m1 = c
        if a > b and a > d:
            m2 = a
            if b > d:
                m3 = b
                m4 = d
            else:
                m3 = d
                m4 = b
        if b > a and b > d:
            m2 = b
            if a > d:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
        if d > a and d > b:
            m2 = d
            if a > b:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
    else:
        m1 = d
        if a > b and a > c:
            m2 = a
            if c > d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        if b > a and b > c:
            m2 = b
            if a > c:
                m3 = a
                m4 = c
            else:
                m3 = c 
                m4 = a
        if c > a and c > b:
            m2 = c
            if a > b:
                m3 = a
                m4 = b
            else:
                m3 = b
                m4 = a
    print(f"A ordem recebida foi {a , b , c , d} ")
    print(f'A ordem decrescente é {m1 , m2 , m3 , m4}')
    print(f'A ordem crescente é {m4 , m3 , m2 , m1}')