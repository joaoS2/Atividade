#Faça um programa que receba:

#o código do produto comprado;° e
#a quantidade comprada do produto.°

#Calcule e mostre:
#o preço unitário do produto comprado, seguindo a Tabela I°;
#o preço total da nota°;
#o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota°; e
# o preço final da nota depois do desconto°. 

#OBS: Tabelas presentws na pagina 93.


#|Definição de Variávies|

codigoProduto : int
quantidadeCompraProduto : int

nota: float
desconto : float
precofinal : float


#|Entrada de Dados|

codigoProduto = int(input("Insira o código do produto: "))
quantidadeCompraProduto = int(input("Insira o código do produto: "))

#|Processamento|

#Preço unitário segundo a tabela 1:

if codigoProduto >= 1 and codigoProduto <= 10:
    print("O preço unitário do produto comprado é de R$10,00")
    nota = quantidadeCompraProduto * 10
    print(f"O valor final da nota é R${nota}")

elif codigoProduto >= 11 and codigoProduto <= 20:
    print("O preço unitário do produto comprado é de R$15,00")
    nota = quantidadeCompraProduto * 15
    print(f"O valor final da nota é R${nota}")

elif codigoProduto >= 21 and codigoProduto <= 30:
    print("O preço unitário do produto comprado é de R$20,00")
    nota = quantidadeCompraProduto * 20
    print(f"O valor final da nota é R${nota}")

elif codigoProduto >= 31 and codigoProduto <= 40:
    print("O preço unitário do produto comprado é de R$30,00")
    nota = quantidadeCompraProduto * 30
    print(f"O valor final da nota é R${nota}")

#Fim do calculo da nota e o preço unitário

#Desconto

if nota < 250:
    print("Você tem 5% de desconto!")
    desconto = nota * 0.5
    #Mostrando o desconto
    print(f"O desconto será de %{desconto: .2f}")
    #Calculo do valor final do preço 
    precofinal = nota - desconto
    #Mostrando o preço final (nota - desconto).
    print(f"Com o desconto, o preço final será R${precofinal: .2f}")

elif nota >= 250 and nota < 500:
    print("Você tem 10% de desconto!")
    #Calculo do desconto
    desconto = nota * 0.10
    #Mostrando o desconto
    print(f"O desconto será de %{desconto: .2f}")
    #Calculo do valor final do preço 
    precofinal = nota - desconto
    #Mostrando o preço final (nota - desconto).
    print(f"Com o desconto, o preço final será R${precofinal: .2f}")

else:
    print("Você tem 15% de desconto!")
    #Calculo do desconto
    desconto = nota * 0.15
    #Mostrando o desconto
    print(f"O desconto será de %{desconto: .2f}")
    #Calculo do valor final do preço 
    precofinal = nota - desconto
    #Mostrando o preço final (nota - desconto).
    print(f"Com o desconto, o preço final será R${precofinal: .2f}")




