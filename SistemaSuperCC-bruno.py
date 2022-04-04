# Criação da Classe do Produto
class tProd:
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
# Listar Variaveis do Produto  
def showProd(p):
    print("%-8d %-20s %.2f %7d"%(p.codigo, p.name, p.price, p.stock))
# Buscar Variaveis do Produto Pelo Codigo       
def searchProd(pr,c):
    for i in range(len(pr)):
        if pr[i].codigo==c:
            return i
        return -1
# Atualizar Variaveis do Produto(Somente Preço e Estoque)
def updateProd(l,codigo,prc,stk):
    pos = searchProd(l,codigo)
    if pos != -1:
        l[pos].price=prc
        l[pos].stock=stk
# Registrar Compras
def comprasProd(lproduto, cods, compra):
    for i in range(len(lproduto)):
        if cods in lproduto[i].codigo:
            print(lproduto[i].name)
            compra = int(input("informe a quantidade desejada: "))
            if compra > lproduto[i].stock:
                print(f"Estoque insuficiente, a quantidade disponivel é: ", lproduto[i].stock)
            else:
                c = tProd()
                c.compra_cod = lpd[i].cod
                c.compra_name = lpd[i].name
                c.compra_qtd = compra
                c.compra_price = compra * lpd[i].price
                lpd[i].stock -= compra
                return c    
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
    fn=int(input())
    return fn
# Criação da Lista de Produtos
lpd = []
compras = []
# Começo do Loop
while True:
    fn=menu()
# Sair
    if fn == 0:
        break
# Incluir
    if fn == 1:
        pr=cadProd()
        lpd.append(pr)
# Atualizar
    if fn == 2:
        cd = input("Digite o Código do Produto: ")
        pc = float(input("Novo preço: "))
        sk = int(input("Nova Quantidade: "))
        updateProd(lpd, cd, pc, sk)
# Registrar
    if fn == 3:
        cod = input("Digite o Código do Produto: ")
        comprasProd(lpd, cod, compras)
        
# Consultar
    if fn == 4:
        c=int(input("Digite o Código do Produto: "))
        pos=searchProd(lpd,c)
        if pos == -1:
            print("Produto não encontrado!")
        else:
            print("Código   Nome                 Preço  Estoque")
            print("============================================")
            showProd(lpd[pos])
# Listar todos
    if fn == 5:
        listProd(lpd)