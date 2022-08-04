"""
Faça um programa que leia um número qualquer
e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""

num = input("Digite um número para saber seu fatorial: ")

if num.isnumeric():
    num = int(num)

    count = num
    fatorial = 1

    while count > 0:
        print(f"{count}",end='')
        print(" x " if count > 1 else ' = ',end='')
        fatorial = fatorial * count
        count -= 1
        
    print(fatorial)
else:
    print("Número digitado é inválido")