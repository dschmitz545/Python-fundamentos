"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior 
valor que estão na tupla.
"""

from random import randint

numeros = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f"Os números sorteados foram: {numeros}")
print(f"OS números sorteados em ordem crescente {sorted(numeros)}")
print(f"Os números sorteados em ordem decrescente {sorted(numeros,reverse= True)}")

for x in range(0, len(numeros)):

    if x == 0:
        maior = numeros[x]
        menor = numeros[x]
    else:
        if maior < numeros[x]:
            maior = numeros[x]
        
        elif menor > numeros[x]:
            menor = numeros[x]

print(f"O maior número gerado foi {maior}")
print(f"O menor número gerado foi {menor}")
