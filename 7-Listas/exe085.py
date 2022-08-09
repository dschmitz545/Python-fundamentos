"""
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.
"""
nums = []
numpar = []
numimpar = []
listafinal = []

for x in range(7):

    nums.append(int(input("Digite um número: ")))

for y in nums:
    if y % 2 == 0:
        numpar.append(y)
    else:
        numimpar.append(y)

listafinal.append(sorted(numpar))
listafinal.append(sorted(numimpar))

# print(f"A lista de numeros pares e impares digitados é {listafinal}")
print(f"A lista de números pares digitada: {listafinal[0]}")
print(f"A lista de números impares digitadas: {listafinal[1]}")