"""
Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie
duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo
das três listas geradas.
"""

numeros = list()
numpar = list()
numimpar = list()

while True:

    n = int(input("Digite um número: "))
    numeros.append(n)

    for numero in numeros:
        if numero % 2 == 0 and numero not in numpar:
            numpar.append(numero)
        elif numero % 2 == 1 and numero not in numimpar:
            numimpar.append(numero)

    opcao = ' '
    while opcao not in "sn":
        opcao = str(input("Deseja continuar [S/N]: "))
    
    if opcao == 'n':
        break
    
print(f"Os números digitados foram: {numeros}")
print(f"Os números pares digitados foram: {numpar}")
print(f"Os números impares digitados foram: {numimpar}")