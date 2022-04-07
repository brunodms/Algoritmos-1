# Criação da Classe do Produto
class tProd:
    compras_cod = 0
    compras_name = None
    compras_qtd = 0.00
    compras_price = 0
# Criação da Classe de Compras
class tCompras:
    codigo = 0
    name = None
    price = 0.00
    stock = 0
# Definição da Classe do Produto
def cadProd():
    tcod = int(input("Código: "))
    for i in range(len(lpd)):
        if tcod == lpd[i].codigo:
            return -1
    prod = tProd()
    prod.codigo = tcod
    prod.name = input("Nome: ")
    prod.price = float(input("Preço: "))
    prod.stock = int(input("Estoque: "))
    return prod
# Listar Variaveis
def showProd(p):
    print("{:>8} {:<16} {:>12} {:>10}".format(p.codigo, p.name, p.price, p.stock))
def showCompras(c):
    print("{:>8} {:<16} {:>12} {:>10}".format(c.compras_cod, c.compras_name, c.compras_qtd, c.compras_price))
# Buscar Variaveis do Produto Pelo Codigo
def searchProd(pr, c):
    for i in range(len(pr)):
        if pr[i].codigo == c:
            return i
    return -1
# Atualizar Variaveis do Produto(Somente Preço e Estoque)
def updateProd(l, codigo):
    pos = searchProd(l, codigo)
    if pos != -1:
        prc = float(input("Novo preço: "))
        stk = int(input("Nova Quantidade: "))
        l[pos].price = prc
        l[pos].stock = stk
    else:
        print("Produto não encontrado!")
        return -1
# Registrar Compras
def comprasProd(lproduto, cods):
        produto = searchProd(lproduto,cods)
        if produto != -1:
            print(lproduto[produto].name)
            buy = int(input("informe a quantidade desejada: "))
            if buy > lproduto[produto].stock:
                print(f"Estoque insuficiente, a quantidade disponivel é: ", lproduto[produto].stock)
                return -1
            else:
                c = tCompras()
                c.compras_cod = lproduto[produto].codigo
                c.compras_name = lproduto[produto].name
                c.compras_price = float(buy * lproduto[produto].price)
                c.compras_qtd = buy
                lproduto[produto].stock -= buy
                return c
        else:
            print("Produto não encontrado!")
            return -1
# Carrinho de Compras
def listCompras(cprs):
    print("{:>8} {:<16} {:>12} {:>10}".format("Código", "Nome", "Quantidade", "Preço"))
    print("=================================================")
    for i in range(len(cprs)):
        showCompras(cprs[i])
# Listar Todas as Variaveis do produto Organizadamente
def listProd(lprod):
    print("{:>8} {:<16} {:>12} {:>10}".format("Código", "Nome", "Preço", "Estoque"))
    print("=================================================")
    for i in range(len(lprod)):
        showProd(lprod[i])
# Valor total da compra
def vTotal(cprs):
    vT = 0.00
    for i in range(len(cprs)):
        vT += cprs[i].compras_price
    print("{:>38}".format("Total"), "{:>10}".format(vT))
# Menu
def menu():
    print("1- Incluir")
    print("2- Atualizar Produto")
    print("3- Registrar Compra")
    print("4- Cosultar Produto")
    print("5- Relatorio de Produtos")
    print('0- Sair')
    mn = int(input())
    return mn
# Criação da Lista de Produtos
lpd = []
compras = []
# Começo do Loop
while True:
    mn = menu()
    # Sair
    if mn == 0:
        break
    # Incluir
    if mn == 1:
        pr = cadProd()
        if pr == -1:
            print("Código do produto já cadastrado!")
        else:
            lpd.append(pr)
    # Atualizar
    if mn == 2:
        cd = int(input("Digite o Código do Produto: "))
        updateProd(lpd, cd)
    # Registrar
    if mn == 3:
        cd = int(input("Digite o Código do Produto: "))
        cpr = comprasProd(lpd, cd)
        if cpr != -1:
            compras.append(cpr)
            listCompras(compras)
            vTotal(compras)
    # Consultar
    if mn == 4:
        cd = int(input("Digite o Código do Produto: "))
        pos = searchProd(lpd, cd)
        if pos == -1:
            print("Produto não encontrado!")
        else:
            print("{:>8} {:<16} {:>10} {:>10}".format("Código", "Nome", "Preço", "Estoque"))
            print("=================================================")
            showProd(lpd[pos])
    # Listar todos
    if mn == 5:
        listProd(lpd)