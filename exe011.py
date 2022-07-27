"""
Faça um programa que leia a largura e a altura
de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la,
sabendo que cada 1litro de tinta pinta
uma área de 2 metros quadrados.
"""
larg = input("largura da parede: ")
alt = input("altura da parede:")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(larg) and isfloat(alt):
    larg = float(larg)
    alt = float(alt)
    area = larg * alt
    cober = area / 2
    print(f"Sua parede tem a dimensão de {alt:.2f}x{larg:.2f} e sua área é de {area:.4f}m².")
    print(f"Para pintar essa parede, você precisará de {cober:.4f}l de tinta")

else:
    print("Valores não são números")
