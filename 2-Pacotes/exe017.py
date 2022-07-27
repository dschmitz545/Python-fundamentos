"""
Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente
de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
h = √(co² + ca²)
"""
from math import hypot


def hipotenusa(catopo, catadj):

    def isfloat(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    if isfloat(catopo) and isfloat(catadj):
        catopo = float(catopo)
        catadj = float(catadj)
        hipo = hypot(catopo, catadj)
        print(f"A hipotenusa vai medir {hipo:.2f}")
    else:
        print("Valores informados não são válidos")


if __name__ == '__main__':
    cateto1 = input("Comprimento do cateto oposto: ")
    cateto2 = input("Comprimento do cateto adjacente: ")
    hipotenusa(cateto1, cateto2)
