#definição de Variáveis: 

altura: float;
peso: float;
mediaIdade: float;
idade: int;
idadeSuperior: int;
qtdPessoasPeso: int;
somaIdade: int;

#Entrada de Dados:
qtdPessoasPeso = 0
idadeSuperior = 0
mediaIdae = 0
somaIdade = 0

for n in range (1, 11):
    print(f"Insira os dados da {n}ª pessoa")
    idade = int(input("Insira a sua idade: "))
    altura = float(input("Insira a altura: "))
    peso = float(input("Insiar o peso: "))

    somaIdade = somaIdade + idade

    if idade > 90 and altura < 1.50:
        qtdPessoasPeso += 1
    if idade >= 10 and idade <= 30 and altura > 1.90:
        idadeSuperior += 1

mediaIdade = somaIdade / 10

print("=" * 78)
print(f"A média das pessoas é de: {mediaIdade:.2f}.")
print("-" * 78)
print(f"A quantidade de pessoas com o peso superior a 90 kg e altura inferior a 1,50m é: {qtdPessoasPeso} pessoas.")
print("-" * 78)
print(f"A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90m é: {idadeSuperior/10*100:.1f}%. ")
print("=" * 78)