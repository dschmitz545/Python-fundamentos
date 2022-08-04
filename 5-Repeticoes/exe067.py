"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
"""

while True:
    print("-=-" * 20)
    numero = input("Digite o número para ver sua tabuada: ")
    print("-=-" * 20)

    numero = int(numero)

    if numero < 0:
        break
    
    for x in range(1, 11):
        print(f"{numero} x {x} = {numero*x}")

print("Programa de Tabuada Encerrado, Volte Sempre")