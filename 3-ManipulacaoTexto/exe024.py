"""
Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome “SANTO”.
"""

nome = input("digite o nome da cidade: ")

nomebuscado = nome.strip()
nomebuscado = nomebuscado.upper()
print(nomebuscado[:5] == 'SANTO')
