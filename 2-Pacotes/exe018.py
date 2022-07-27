"""
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do
seno, cosseno e tangente desse ângulo
"""
import math

angulo = input("Informe um ângulo: ")


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


if isfloat(angulo):
    angulo = float(angulo)
    angulorad = math.radians(angulo)
    seno = math.sin(angulorad)
    cosseno = math.cos(angulorad)
    tangente = math.tan(angulorad)
    print(f"O angulo de {angulo:.1f} tem o SENO de {seno:.2f}")
    print(f"O angulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}")
    print(f"O angulo de {angulo:.1f} tem a tangente de {tangente:.2f}")
else:
    print("O valor digitado é inválido")
