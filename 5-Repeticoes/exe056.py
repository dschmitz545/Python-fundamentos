"""
Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, qual é o nome 
do homem mais velho e quantas mulheres
têm menos de 20 anos.
"""
mulheres = 0
maisvelho = ""
idadevelho = 0
mediaidade = 0

for x in range(4):
    nome = str(input(f"Informe o {x+1}º nome: ")).strip().upper()
    idade = int(input(f"Informe a {x+1}ª idade: "))
    sexo = str(input(f"Informe o {x+1}º sexo M/F: ").strip().upper())

    mediaidade += idade

    if sexo == "F" and idade < 20:
        mulheres += 1

    if sexo == "M":
        if x == 0:
            maisvelho = nome
            idadevelho = idade

        if idadevelho < idade:
            maisvelho = nome
            idadevelho = idade
        else:
            maisvelho = maisvelho
            idadevelho = idadevelho

mediaidade = mediaidade / 4
    
print(f"Quantidade de mulheres com menos de 20 anos é de {mulheres}")
print(f"O nome do homem mais velho é {maisvelho} e ele tem {idadevelho} anos")
print(f"A média de idade do grupo é {mediaidade}")