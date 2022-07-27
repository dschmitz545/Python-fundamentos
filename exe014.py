"""
Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta para graus Fahrenheit.
F = {(9 x C) / 5} + 32
"""


def fahrenheit(temp):

    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    if isfloat(temp):
        temp = float(temp)
        fare = ((9 * temp) / 5) + 32
        print(f"A temperatura convertida de {temp:.1f}ºC é {fare:.1f}ºF")
    else:
        print("O valor informado não é valido")


if __name__ == '__main__':
    temperatura = input("Informe a temperatura em ºC: ")
    fahrenheit(temperatura)
