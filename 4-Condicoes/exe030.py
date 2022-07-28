"""
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = input("\033[1;36mMe diga um número qualquer: \033[0;0m")

if numero.isnumeric():
    numero = int(numero)
    validacao = numero % 2
    if validacao == 0:
        print(f"O número {numero} é \033[1;34mPAR\033[0;0m")
    else:
        print(f"O número {numero} é \033[1;90m\033[1;102mIMPAR\033[0;0m")
else:
    print("Número digitado não é um número válido\033[0;0m")
