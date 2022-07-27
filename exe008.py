"""
Escreva um programa que leia um valor em metros
e o exiba convertido em kilometros, hectometros,
decametros, decimetros, centímetros e milímetros.
"""

metros = input("Uma distância em metros: ")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(metros):
    metros = float(metros)
    km = metros / 1000
    hm = metros / 100
    dam = metros / 10
    dm = metros * 10
    cm = metros * 100
    mm = metros * 1000
    print(f"A medida de {metros:.2f}m corresponde a: \n{km}km \n{hm}hm \
          \n{dam:.2f}dam \n{dm:.2f}dm \n{cm:.2f}cm \n{mm:.2f}mm"
         )
else:
    print("Não é um número válido")
