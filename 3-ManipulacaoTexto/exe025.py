"""
Crie um programa que leia o nome de uma
pessoa e diga se ela tem “SILVA” no nome.
"""

nome = input("Digite um nome: ")
nome = nome.strip()
nome = nome.lower()
nomebuscado = "silva"
print(f"Seu nome tem Silva? {nomebuscado in nome}")
