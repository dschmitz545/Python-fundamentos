"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""

preco = input("Qual é o preço do produto? R$")


def isfloat(num):
    try:
        float(num)
        return True
    except TypeError:
        return  False


if isfloat(preco):
    preco = float(preco)
    perdes = 5
    desconto = (preco * perdes) / 100
    novopreco = preco - desconto
    print(f"O produto que custava R${preco:.2f}, na promoção com desconto de {perdes}% \
vai custar R${novopreco:.2f}"
          )
else:
    print("Não é um valor válido")
