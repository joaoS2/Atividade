n1 = float(input( ' Digite sua nota: '))
n2 = float(input( ' Digite sua outra nota: '))
n3 = float(input( ' Digite sua ultima nota: '))
p1 = float(input( ' Digite o peso da nota 1: '))
p2 = float(input( ' Digite o peso da nota 2: '))
p3 = float(input( ' Digite o peso da nota 3: '))

s1 = n1+n2+n3+p1+p2+p3
s2 = p1+p2+p3
m = s1/s2

print(f" Sua media ponderada e:   {m}")
