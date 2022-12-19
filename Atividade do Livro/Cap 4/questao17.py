#Faça um programa que verifique a validade de uma senha fornecida pelo usuário. A senha é 4531. O
#programa deve mostrar uma mensagem de permissão de acesso ou não.

#Definição de Variáveis:
senha : int

#Entrada de Dados:
senha = int(input("Insira a senha: "))

#Processamento de dados: 

#Verifica se a senha é a mesma comparando com a senha orginal
if senha == 4531:
    print("Senha correta!")

else:
    print("SENHA INCORRETA!\nTENTE NOVAMENTE!")