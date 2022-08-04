"""
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação
novamente até ter um valor correto.
"""

sexo = str(input("Informe seu sexo: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = input(str("Dados inválidos. Por favor informe seu sexo: "))

print("Sexo {} registrado com sucesso".format(sexo))