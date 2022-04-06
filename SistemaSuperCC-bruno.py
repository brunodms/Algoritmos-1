# Criação da Classe do Produto
class tProd:
    compras_cod = 0
    compras_name = None
    compras_qtd = 0.0
    compras_price = 0
# Criação da Classe de Compras
class tCompras:
    codigo = 0
    name = None
    price = 0.0
    stock = 0
# Definição da Classe do Produto
def cadProd():
    prod = tProd()
    prod.codigo = int(input("Código: "))
    prod.name = input("Nome: ")
    prod.price = float(input("Preço: "))
    prod.stock = int(input("Estoque: "))
    return prod
# Listar Variaveis
def showProd(p):
    print("%-8d %-20s %.2f %7d" % (p.codigo, p.name, p.price, p.stock))
def showCompras(c):
    print("%-8d %-20s %.2f %7d" % (c.compras_cod, c.compras_name, c.compras_price, c.compras_qtd))
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
# Registrar Compras
def comprasProd(lproduto, cods):
        produto = searchProd(lproduto,cods)
        if produto != -1:
            print(lproduto[produto].name)
            buy = int(input("informe a quantidade desejada: "))
            if buy > lproduto[produto].stock:
                print(f"Estoque insuficiente, a quantidade disponivel é: ", lproduto[produto].stock)
            else:
                c = tCompras()
                c.compra_cod = lproduto[produto].codigo
                c.compra_name = lproduto[produto].name
                c.compra_price = buy * lproduto[produto].price
                c.compra_qtd = buy
                lproduto[produto].stock -= buy
                return c
# Carrinho de Compras
def listCompras(cprs):
    print("Código   Nome                 Preço  Estoque")
    print("============================================")
    for i in range(len(cprs)):
        showProd(cprs[i])
# Listar Todas as Variaveis do produto Organizadamente
def listProd(lprod):
    print("Código   Nome                 Preço  Estoque")
    print("============================================")
    for i in range(len(lprod)):
        showProd(lprod[i])
# Menu
def menu():
    print("1- Incluir")
    print("2- Atualizar Produto")
    print("3- Registrar Compra")
    print("4- Cosultar Produto")
    print("5- Relatorio de Produtos")
    print('0- Sair')
    fn = int(input())
    return fn


# Criação da Lista de Produtos
lpd = []
compras = []
# Começo do Loop
while True:
    fn = menu()
    # Sair
    if fn == 0:
        break
    # Incluir
    if fn == 1:
        pr = cadProd()
        lpd.append(pr)
    # Atualizar
    if fn == 2:
        cd = int(input("Digite o Código do Produto: "))
        updateProd(lpd, cd)
    # Registrar
    if fn == 3:
        cod = int(input("Digite o Código do Produto: "))
        cpr = comprasProd(lpd, cod)
        compras.append(cpr)
        listCompras(compras)
    # Consultar
    if fn == 4:
        c = int(input("Digite o Código do Produto: "))
        pos = searchProd(lpd, c)
        if pos == -1:
            print("Produto não encontrado!")
        else:
            print("Código   Nome                 Preço  Estoque")
            print("============================================")
            showProd(lpd[pos])
    # Listar todos
    if fn == 5:
        listProd(lpd)