#modificado


nota1: float; nota2: float; nota3: float; media: float; notaNes: float; mediaRec: float; escolha: int; notaExa: float
nota1= float(input("Digite sua primeira nota: "))
nota2= float(input("Digite sua segunda nota: "))
nota3= float(input("Digite sua terceira nota: "))
media= (nota1 + nota2 + nota3)/3

if media>=0 and media<3:
    print("Reprovado!")
elif media>=3 and media<7:
    notaNes = 12 - media
    print(f"Recuperação, você deve tirar: {notaNes} para passar.")
    print("=============================================")
    print("Escolha uma opção:")
    print("1. Vou fazer o exame")
    print("2. Já fiz o exame")
    escolha = int(input("Digite a sua escolha (1 ou 2): "))
    print("=============================================")
    if escolha == 1:
        print("Boas Sorte!")
    else:
        notaExa = float(input("Digite a sua nota do exame de recuperação: "))
        mediaRec = (notaExa + media)/2
        if mediaRec >= 6:
            print("Aprovado!")
        else:
            print("Reprovado!")
else:
    print("Aprovado!")