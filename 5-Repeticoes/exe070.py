"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
"""
totalprodutos = 0
totpro1000 = 0
prodbarato = ' '
prebarato = 0
qtd = 0

while True:
    print("--" * 20)
    print("LOJÂO BARATÂO")
    print("--" * 20)
    qtd += 1

    produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço: R$"))

    totalprodutos = totalprodutos + preco

    if preco > 1000:
        totpro1000 += 1

    if qtd == 1 or preco < prebarato:
        prodbarato = produto
        prebarato = preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if continuar == 'N':
        break
print("{:-^40}".format("Fim do Programa"))

print(f"O total da compra foi R${totalprodutos:.2f}")
print(f"Temos {totpro1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {prodbarato} que custa R${prebarato:.2f}")
