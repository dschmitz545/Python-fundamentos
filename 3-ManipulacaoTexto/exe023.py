"""
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
"""

numero = input("Digite um número de 0000 a 9999: ")

if numero.isnumeric() and len(numero) < 4:
    uni = numero[-1]
    deze = numero[-2]
    cent = numero[-3]
    milh = numero[-4]

    print(f"analisando o numero {numero}")
    print(f"Unidade: {uni}")
    print(f"Dezena: {deze}")
    print(f"Centena: {cent}")
    print(f"Milhar: {milh}")
else:
    print("não digitou um numero válido")
