"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular.
"""

produtos = ("Lápis", 1.75,
            "Borracha", 0.75,
            "Caderno", 15.90,
            "Estojo", 25.40,
            "Transferidor", 4.20,
            "Compasso", 4.40,
            "Mochila", 120.35,
            "Canetas", 5.55,
            "Livro", 25.90)
print("-" * 40)
print(f"{'Listagem de preços':^40}")
print("-" * 40)
for produto in produtos:
    if produtos.index(produto) % 2 == 0:
        print(f"{produto:.<30}",end='')
    else:
        print(f"R$ {produto:>7.2f}")
print("-" * 40)