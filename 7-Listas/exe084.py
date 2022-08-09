"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves
"""

nomes = list()
temp = list()
nmaior = []
nmenor = []
maior = menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))

    if len(nomes) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]

        elif temp[1] < menor:
            menor = temp[1]
    
    nomes.append(temp[:])
    temp.clear()

    opcao = " "
    while opcao not in "sn":
        opcao = str(input("Quer continuar [S/N]: ")).lower().strip()

    if opcao == "n":
        break

for n in nomes:
    if n[1] == maior:
        nmaior.append(n[0])
    elif n[1] == menor:
        nmenor.append(n[0])

print(f"foram cadastradas {len(nomes)} pessoas")
print(f"As pessoas mais pessadas tem {maior}Kg e foram {nmaior}")
print(f"As pessoas mais leves tem {menor}Kg e foram {nmenor}")
