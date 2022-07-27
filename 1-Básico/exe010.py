"""
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar
"""

real = input("Quanto dinheiro você tem na carteira? R$")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(real):
    real = float(real)
    dollar = 3.27
    convertido = real / dollar
    print(f"Com R${real:.2f} você pode comprar US${convertido:.2f}")

else:
    print("Não é um valor válido!")
