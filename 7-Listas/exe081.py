"""
Crie um programa que vai ler vários números e colocar
em uma lista.Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista
"""

numeros = list()

while True:

    n = int(input("Digite um número: "))

    numeros.append(n)

    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input("Deseja continuar? [S/N]")).lower().strip()

    if opcao == 'n':
        break

print("=-=" * 20)
print(f"Você digitou {len(numeros)} elementos")
print(f"Os valores em ordem decresence são {sorted(numeros, reverse=True)}")
if 5 in numeros:
    print("Sim o 5 faz parte da lista")
else:
    print("Não, o 5 não faz parte da lista")

