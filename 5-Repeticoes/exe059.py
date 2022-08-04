"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. 
"""

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
print("-=-" * 10)
print("O que você quer fazer agora?")
print("[1] somar")
print("[2] multiplicar")
print("[3] maior")
print("[4] novos números")
print("[5] sair do programa")
opcao = input("Digite sua opção: ")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if isfloat(num1) and isfloat(num2) and opcao.isnumeric():
    num1 = float(num1)
    num2 = float(num2)
    opcao = int(opcao)


    while opcao != 5:
        if opcao == 1:
            resultado = num1 + num2
            print(f"resultado de {num1:.2f} + {num2:.2f} = {resultado:.2f}")
            opcao = input("Digite sua opção: ")
            print("-=-" * 10)
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                print("Opacao digitada é inválida")

        elif opcao == 2:
            resultado = num1 * num2
            print(f"O resultado de {num1:.2f} x {num2:.2f} = {resultado:.2f}")
            opcao = input("Digite sua opção: ")
            print("-=-" * 10)
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                print("Opacao digitada é inválida")

        elif opcao == 3:
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            print(f"O maior número digitado foi {maior:.2f}")
            opcao = input("Digite sua opção: ")
            print("-=-" * 10)
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                print("Opacao digitada é inválida")

        elif opcao == 4:
            num1 = input("Digite o primeiro número: ")
            num2 = input("Digite o segundo número: ")
            opcao = input("Digite sua opção: ")
            print("-=-" * 10)
            if isfloat(num1) and isfloat(num2) and opcao.isnumeric():
                num1 = float(num1)
                num2 = float(num2)
                opcao = int(opcao)
            else:
                print("Opacao digitada é inválida")

        else:
            opcao = input("Opção inválida, Digite sua opção: ")
            print("-=-" * 10)
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                print("Opacao digitada é inválida")

    print("Ate Mais")
else:
    print("Numero digitado não é válido")