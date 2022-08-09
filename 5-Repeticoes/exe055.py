"""
Faça um programa que leia o peso
de cinco pessoas. No final, mostre qual 
foi o maior e o menor peso lidos.
"""

maior = 0
menor = 0

for x in range(1, 6):
    peso = float(input(f"Informe o peso da {x}º pessoa: "))

    if x == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso

print(f"O maior peso digitado foi {maior:.2f} kg")
print(f"O menor peso digitado foi {menor:.2f} kg")