"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues.
OBS: considere que o caixa possui cédulas de
R$50, R$20, R$10 e R$1.
"""
cedulas = (50, 20, 10, 1)
x = 0
totalsacado = 0

print("==" * 20)
print("Banco")
print("==" * 20)

valor = int(input("Qual valor você quer sacar? R$"))
montante = valor

while True:
   
    if montante >= cedulas[x]:
        montante -= cedulas[x]
        totalsacado += 1
    else:
        print(f"Foi sacado {totalsacado} notas de R${cedulas[x]}")
        if cedulas[x] == 50:
            x = 1
            totalsacado = 0
        elif cedulas[x] == 20:
            x = 2
            totalsacado = 0
        elif cedulas[x] == 10:
            x = 3
            totalsacado = 0

        if montante == 0:
            break

print("Volte Sempre")
