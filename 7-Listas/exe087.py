"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = soma = maior = 0

for i in range (0, 3):
    for j in range (0, 3):
        matriz[i][j] = int(input(f"Digite o número da posição [{i},{j}]: "))

for nums in matriz:
    for num in nums:
        if num % 2 == 0:
            pares += num

soma = (matriz[0][2] + matriz[1][2] + matriz[2][2])

for m in matriz[1]:
    
    if m == 0:
        maior = m
    else:
        if m > maior:
            maior = m

for x in matriz[0]:
    print(f"[ {x} ]",end="")
print()

for y in matriz[1]:
    print(f"[ {y} ]",end="")
print()

for z in matriz[2]:
    print(f"[ {z} ]",end="")
print()

print(f"A soma de todos os pares digitados foi {pares}")
print(f"A soma de todos os valores da terceira coluna {soma}")
print(f"O maior valor da segunda linha é {maior}")
