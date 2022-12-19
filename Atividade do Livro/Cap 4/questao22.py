# Este programa solicita ao usuarío suda idade e seu peso e mostra a categoria que ele se encaixa de acordo com uma tabela. */


#|Dfinição de Variávies|

idade : float
peso : float


#|Entrada de Dados|

idade = float(input("Insira a sua idade: "))
peso = float(input("Insira a sua idade: "))

#|Processamento|

#Tabela dos 20 anos
if idade < 20:
    if peso < 60:
        print("Sua categoria é 9")
    
    elif peso >= 60 and idade <= 90:
        print("Sua categoria é 8")
    
    else:
        print("Sua categoria é 7")
#Parte dos 20 anos acabou

#Começo dos 20 aos 50:
elif idade >= 20 and idade <= 50:

    if peso >= 60 and idade <= 90: 
        print("Sua categoria é 6")

    elif peso >= 60 and idade <= 90:
        print("Sua categoria é 5")

    else:
        print("Sua categoria é 4")

#Encerramento dos 20 aos 50.

else:
    if peso >= 60 and idade <= 90: 
        print("Sua categoria é 3")

    elif peso >= 60 and idade <= 90:
        print("Sua categoria é 2")

    else:
        print("Sua categoria é 1")


