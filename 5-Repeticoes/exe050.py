"""
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0

for x in range(1, 7):
    num = int(input(f"Informe o {x}º número: "))
    if num % 2 == 0:
        soma = soma + num
    else:
        pass
print(f"A soma de todos os números pares é: {soma}")
    