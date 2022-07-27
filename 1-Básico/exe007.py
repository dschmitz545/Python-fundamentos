"""
Desenvolva um programa que
leia as duas notas de um aluno,
calcule e mostre a sua média com 1 casa decimal
"""

nota1 = input("Informe a primeira nota: ")
nota2 = input("Informe a segunda nota: ")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(nota1) and isfloat(nota2):
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2
    print(f"A média entre {nota1:.2f} e {nota2:.2f} é igual a {round(media,1)}")
else:
    print("Não é um número válido")
