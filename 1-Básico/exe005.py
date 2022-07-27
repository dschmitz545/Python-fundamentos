"""
Faça um programa que leia um número Inteiro e
mostre na tela o seu sucessor e seu antecessor.
"""


def antecessorSucessor():
    num = input("Digite um numero: ")

    if num.isnumeric():
        num = int(num)
        print(f"Analisando o valor {num}, seu antecessor é {num - 1} e o sucessor é {num + 1}")
    else:
        print("Não é um número")


if __name__ == '__main__':
    antecessorSucessor()

