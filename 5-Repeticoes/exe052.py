"""
Faça um programa que leia um número inteiro 
e diga se ele é ou não um número primo.
"""
num = input("Informe um número: ")

if num.isnumeric():
    num = int(num)
    count = 0

    for x in range(1, num+1):
        if num % x == 0:
            count += 1
            print(f"{x}", end=' - ')

    if count == 2:
        print(f"\nO número {num} é um número primo")
    else:
        print(f"\nO númerno {num} não é primo, ele é divisível {count} vezes")

else:
    print("Não é um número válido")


