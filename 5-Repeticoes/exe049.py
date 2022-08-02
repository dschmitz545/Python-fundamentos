"""Refaça o DESAFIO 9, mostrando a tabuada
de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

numero = input("Informe um número para ver sua tabuada: ")

if numero.isnumeric():
    numero = int(numero)
    for x in range(1,11):
        saida = x * numero
        print(f"{numero} X {x} = {saida}")
else:
    print("Número digitado não é válido")
