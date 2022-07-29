"""
Escreva um programa que leia dois números inteiros
e compare-os. mostrando na tela uma mensagem
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

num1 = input("Escreva o primeiro número: ")
num2 = input("Escreva o segundo número: ")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)

    if num2 > num1:
        print("O segundo valor é maior")
    elif num1 > num2:
        print("O primero valor é maior")
    elif num2 == num1:
        print("Não exite número maior, os dois são iguais")
    else:
        pass

else:
    print("valor digitado não é válido")