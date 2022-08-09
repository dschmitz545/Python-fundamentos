"""
Crie um programa que declare uma matriz de dimensão 3×3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta.
"""
matriz = [[],[],[]]

for i in range (0, 3):
    for j in range (0, 3):
        matriz[i].append(int(input(f"Digite o número da posição [{i},{j}]: ")))


for x in matriz[0]:
    print(f"[ {x} ]",end="")
print()

for y in matriz[1]:
    print(f"[ {y} ]",end="")
print()

for z in matriz[2]:
    print(f"[ {z} ]",end="")
print()
