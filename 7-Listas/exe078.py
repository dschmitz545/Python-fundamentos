"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista.
"""
numeros = []


for x in range(5):

    numeros.append(int(input(f"Digite um número para a posição {x}: ")))

    if x == 0:
        maior = numeros[x]
        menor = numeros[x]
    else:
        if maior < numeros[x]:
            maior = numeros[x]

        elif menor > numeros[x]:
            menor = numeros[x]

print(f"Você digitou os numeros {numeros}")

print(f"O maior valor digitado foi {maior} na posição ",end='')
for pos, y in enumerate(numeros):
    if y == maior:
        print(f"{pos}...",end='')
print()
print(f"O menor número digitado foi {menor} na posição ",end="")
for pos, y in enumerate(numeros):
    if y == menor:
        print(f"{pos}...",end='')
print()