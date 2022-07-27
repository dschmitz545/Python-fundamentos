"""
Faça um programa que leia
um número Inteiro qualquer
e mostre na tela a sua tabuada.
"""

num = input("Digite um número para ver a sua tabuada: ")


if num.isnumeric():
    num = int(num)
    for x in range(11):
        num1 = num * x
        print(f"{num} x {x} = {num1}")
else:
    print("Não é um número válido")
