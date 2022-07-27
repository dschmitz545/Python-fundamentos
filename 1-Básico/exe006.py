"""
Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.
"""
import math


def dobrotriploquadrado():
    num = input("Informe um número: ")

    if num.isnumeric():
        num = int(num)
        print(f"O dobro de {num} é {num * 2}")
        print(f"O triplo de {num} é {num * 3}")
        print(f"A raiz quadrada de {num} é {round(math.sqrt(num),2)}")
    else:
        print("Não é um número válido")

if __name__ == '__main__':
    dobrotriploquadrado()

