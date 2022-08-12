"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
largura e comprimento) e mostre a área do terreno
"""


def gerarlayout(tit: str):
    print("-" * 30)
    print(f"{tit:^30}")
    print("-" * 30)


def calculararea(lar: float = 0, alt: float = 0):
    area = lar * alt
    print(f"A área de um terreno {lar:.2f}x{alt:.2f} é de {area:.2f}m².")


gerarlayout("Controle de Terrenos")
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
calculararea(largura, comprimento)
