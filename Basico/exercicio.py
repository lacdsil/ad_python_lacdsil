import sys
def compra(preco,quantidade,saldo):
    saldo = saldo -(preco*quantidade)
    return saldo
preco_produto = sys.argv[0]
meusaldo = sys.argv[1]
quantidade_produto = sys.argv[2]
saldofinal = compra(preco_produto,quantidade_produto,meusaldo)
print(saldofinal)