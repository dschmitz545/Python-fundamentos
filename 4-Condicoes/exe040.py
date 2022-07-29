"""
Crie um programa que leia duas notas de
um aluno e calcule sua média, mostrando uma mensagem 
no final, de acordo com a média atingida
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

nota1 = input("Informe a primeira nota: ")
nota2 = input("Informe a segunda nota: ")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(nota1) and isfloat(nota2):
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = ((nota1 + nota2) / 2)

    if media < 5:
        print(f"{media:.2f} REPROVADO")
    elif media >= 5 and media <= 6.9:
        print(f"{media:.2f} RECUPERAÇÃO")
    elif media > 7 and media <=10:
        print(f"{media:.2f} APROVADO")
    else:
        print("Você digitou valores inválidos")

else:
    print("Valores digitados não são válidos")
