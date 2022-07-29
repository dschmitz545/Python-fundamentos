"""
Escreva um programa em Python que leia um número inteiro 
qualquer e peça para o usuário escolher qual será a base 
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
num = input("Digite um numero: ")
num = num.strip()

if num.isnumeric():
    num = int(num)
    print("Escolha uma das bases de conversão")
    print("[ 1 ] para BINÁRIO")
    print("[ 2 ] para OCTAL")
    print("[ 3 ] para HEXADECIMAL")

    opcao = input("Sua opcao: ")
    saida = 0
    
    if opcao.isnumeric():
        opcao = int(opcao)
        if opcao == 1:
            descri = "binário"
            saida = bin(num)[2:]

            print(f"{num} convertido para base {descri.upper()} é igual a {saida}")

        elif opcao == 2:
            descri = "octal"
            saida = oct(num)[2:]

            print(f"{num} convertido para base {descri.upper()} é igual a {saida}")

        elif opcao == 3:
            descri = "hexadecimal"
            saida = hex(num)[2:]
            print(saida)
        
            print(f"{num} convertido para base {descri.upper()} é igual a {saida}")

        else:
            print("Opção escolhida inválida")


    else:
        print("Valor digitado inválido")

else:
    print("Valor digitado é inválido")
