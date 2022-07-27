"""
Crie um programa que leia um número Real
qualquer pelo teclado e mostre na tela a 
sua porção Inteira
"""
import math

numerodigi = input("Informe um número: ")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(numerodigi):
    numeroint = float(numerodigi)
    numeroint = math.trunc(numeroint)
    print(f"O valor digitado foi {numerodigi} e sua porção inteira é {numeroint}")
else:
    print("Valor digitado não é um número")

