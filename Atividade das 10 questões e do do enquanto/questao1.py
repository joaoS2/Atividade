nota1: float; nota2: float; nota3: float; media: float; somaP: float; somaN: float
nota1= float(input("Digite sua nota do trabalho do laboratório: "))
nota2= float(input("Digite sua nota da avaliação semestral: "))
nota3= float(input("Digite sua nota do exame final: "))
somaN= nota1*2 + nota2*3 + nota3*5
somaP= 2 + 3 + 5
media= somaN / somaP

if media >= 8:
    print(f"Sua nota é: {media}, o conceito é A")
elif media >= 7 and media<8:
    print(f"Sua nota é: {media}, o conceito é B")
elif media >= 6 and media<7:
    print(f"Sua nota é: {media}, o conceito é C")
elif media >= 5 and media<6:
    print(f"Sua nota é: {media}, o conceito é D")
else:
    print(f"Sua nota é: {media}, o conceito é E")