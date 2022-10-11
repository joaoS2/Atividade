

grupo1 = 1
 
for grupo1 in range(0, grupo1):
   a = float(input("Insira um valor para a: "))
   b = float(input("Insira um valor para b: "))
   c = float(input("Insira um valor para c: "))
   d = float(input("Insira um valor para d: "))

   if a > b and a > c and a > d: 
        maior1 = a
        if b > c and b > d:
            maior2 = b
        elif c > d : 
            maior3 = c
            maior4 = d
        else: 
            maior4 = d 
            maior3 = c
print(a,b,c,d)
print(maior1,maior2,maior3,maior4)
print(maior4,maior3,maior2,maior1)