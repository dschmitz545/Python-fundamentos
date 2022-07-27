"""
Faça um programa que leia algo do teclado
e mostre na tela o seu tipo primitivo e todas
as informações possiveis sobre ela.
"""

entrada = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(entrada)}")
print(f"Só tem espaços? ", entrada.isspace())
print(f"Está minusculo?", entrada.islower())
print(f"Está maiúsculo? ", entrada.isupper())
print(f"É um número? ", entrada.isnumeric())
print(f"É alfabético ", entrada.isalpha())
print(f"É alfanumérico ", entrada.isalnum())
print(f"Está capitalizado? ", entrada.istitle())
