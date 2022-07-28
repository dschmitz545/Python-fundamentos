"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")
num3 = input("Informe o terceiro número: ")

if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    menor = num1
    maior = num1
    if num2 < num1 and num2 < num3:
        menor = num2
    if num3 < num1 and num3 < num2:
        menor = num3
    
    if num2 > num1 and num2 > num3:
        maior = num2
    if num3 > num1 and num3 > num2:
        maior = num3

    print(f"Menor número é {menor}")
    print(f"Maior número é {maior}")
else:
    print("Não são números válidos")
