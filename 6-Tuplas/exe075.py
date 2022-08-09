"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

numeros = (int(input("Digite o primeiro valor: ")),
           int(input("Digite o segundo valor: ")),
           int(input("Digite o terceiro valor: ")),
           int(input("Digite o quarto valor: ")))

print(numeros)

if numeros.count(9) > 0:
    qtdnove = numeros.count(9)
    print(f"A quantidade de números 9 digitados foi de {qtdnove}")
else:
    print("Não foi digitado nenhum número 9")

if 3 in numeros:
    positres = numeros.index(3)
    print(f"O número 3 foi digitado na posição {positres}")
else:
    print("Não foi digitado nenhum número 3")

print("Os valores pares digitados foram ",end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
