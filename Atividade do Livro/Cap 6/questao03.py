import os 
#Faça um programa para controlar o estoque de mercadorias de uma empresa.
#Inicialmente, o programa deverá preencher dois vetores com dez posições cada,
#Onde o primeiro corresponde ao código do produto e o segundo, ao total desse produto em estoque.
#Logo após, o programa deverá ler um conjunto indeterminado de dados contendo o código de um cliente e
#o código do produto que ele deseja comprar, juntamente com a quantidade. 
#Código do cliente igual a zero indica fim do programa. O programa deverá verificar:

# se o código do produto solicitado existe. Se existir, tentar atender ao pedido; caso contrário, exibir
#cada pedido feito por um cliente só pode ser atendido integralmente. Caso isso não seja possível,
#escrever a mensagem Não temos estoque suficiente dessa mercadoria. Se puder atendê-lo, escrever
#a mensagem Pedido atendido. Obrigado e volte sempre;
# efetuar a atualização do estoque somente se o pedido for atendido integralmente;
# no final do programa, escrever os códigos dos produtos com seus respectivos estoques já atualizados.
os.system("clear")


codigoProduto = []
produtoEstoque = []
codigoProdutCliente : str
codigoCliente : str 
quantidade : int
quantidadeTotal : int
codigoCliente = 1

#Entrada de Dados:
for n in range (0,10):
    os.system("clear")
    
    #Encerir o código do produto e a quantidade do estoque
    codigoProduto.append(input("Insira o código do produto: "))
    produtoEstoque.append(int(input("insira a quantidade no estoque: ")))

codigoCliente = input("Insira o código do cliente: ")


while codigoCliente != 0:
    #Entrada de dados do cliente:
    codigoCliente = input("Insira o código do cliente: ")
    codigoProdutCliente = input("Insira o código do produto que deseja comprar: ")
    quantidade = int(input("insira a quantidade que deseja comprar: "))
    
    os.system("clear")
    for n in range(0,10):
        
        #Verificar se o código digitado pelo cliente existe
        if codigoProdutCliente == codigoProduto[n]: 
            print("Vamos atender ao seu pedido!")
            
            #verificar se há estoque o soficiente para enviar o pedido
            if produtoEstoque[n] > 0:
                print("Pedido atendido. Obrigado e volte sempre!")
                produtoEstoque[n] -= quantidade  
            else:
                print("Não temos estoque suficiente dessa mercadoria!")
        else:
            print("Código inexistente!")

        os.system("clear")
        #Escolher se deseja encerrar o programa

    codigoCliente = input("Se quiser encerrar o código digite »0«, caso contrario digite outro número: ")

print(produtoEstoque)



    


