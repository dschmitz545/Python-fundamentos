"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = input("Informe seu nome completo: ")
nome = nome.strip().split()
print("Muito Prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu ultimo nome é {nome[-1]}")
