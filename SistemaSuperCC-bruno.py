cod = int
class Prod:
    prod_cod = None
    prod_name = None
    prod_price = None
    prod_stock = None
produto = []
compras = []

fn = int(input("Digite 1 para Cadastro de novos produtos, 2 para Atualizaçoes, 3 para Vendas, 4 para Consultas e 5 para Relatorio"))
if fn == 1:
    while True:
        p = Prod()
        p.prod_cod = int(input("\nCódigo(0 encerra o codigo): "))
        if p.prod_cod == 0:
            break
        elif p.prod_cod in produto.prod_cod:
            print("Codigo já cadastrado")
            continue
        p.prod_name = input("Nome: ")
        p.prod_price = float(input("Preço: "))
        p.prod_stock = int(input("Estoque: "))
        produto.append(p)
        
if fn == 2:
    cod = input("Digite o Código do Produto: ")
    for i in range(len(produto)):
        if cod in produto[i].prod_cod:
            att = int(input("Digite 1 para atualzar o preço, 2 para atualizar o estoque ou 3 para atualizar ambos"))
            if att == 1:
                produto[i].prod_price = input("Novo Preço: ")
            elif att == 2:
                produto[i].prod_stock = input("Novo Estoque: ")
            elif att == 3:
                produto[i].prod_price = input("Novo Preço: ")
                produto[i].prod_stock = input("Novo Estoque: ")
            else:
                print("O Valor informado é Invalido!")
        else:
            print("Código invalido")
elif fn == 3:
    cod = input("Digite o Código do Produto: ")
    for i in range(len(produto)):
        if cod in produto[i].prod_cod:
            print(produto[i].prod_name)
            compra = int(input("Informe a quantidade desejada: "))
            if compra >= produto[i].prod_stock:
                print("Estoque insuficiente, a quantidade disponivel é: ", produto[i].prod_stock)
            else:
                c = Prod()
                c.compra_cod = produto[i].prod_cod
                c.compra_name = produto[i].prod_name
                c.compra_qtd = compra
                c.compra_price = compra * produto[i].prod_price
                compras.append(c)
                produto[i].prod_stock -= compra
        else:
            print("Código invalido")
            
elif fn == 4:
    cod = input("Digite o Código do Produto: ")
    for i in range(len(produto)):
        if cod in produto[i].prod_cod:
            print(" Código: ", produto[i].prod_cod, " Nome: ", produto[i].prod_name, " Preço: ", produto[i].prod_price, " Estoque: ", produto[i].prod_stock)
        else:
            print("Código invalido")
elif fn == 5:
    for i in range(len(produto)):
        print(" Código: ", produto[i].prod_cod, " Nome: ", produto[i].prod_name, " Preço: ", produto[i].prod_price, " Estoque: ", produto[i].prod_stock)
else:
    print("Função invalida")