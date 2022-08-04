"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
"""

countidade = 0
counthomem = 0
countmulher = 0


while True:
    print("--" * 20)
    print("CADASTRE UMA PESSOA")
    print("--" * 20)

    idade = int(input("Idade: "))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("[M/F]: ")).strip().upper()[0]

    if idade > 18:
        countidade += 1
    
    if sexo == 'M':
        counthomem += 1
    
    if idade < 20 and sexo == 'F':
        countmulher += 1

    continuar =  ' '
    while continuar not in 'SN':
        continuar = input("quer continuar? [S/N]").strip().upper()[0]

    if continuar == 'N':
        break

print(f"Total de pessoas com mais de 18 anos: {countidade}")
print(f"Ao todo temos {counthomem} homens cadastrados")
print(f"E temos {countmulher} mulher com menos de 20 anos")
