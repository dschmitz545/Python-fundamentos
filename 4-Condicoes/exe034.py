"""
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1250,00,
calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%
"""

salario = input("Informe o valor do sálario: ")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(salario):
    salario = float(salario)
    if salario > 1250:
        aumento = (salario * 10) / 100
        novosalario = salario + aumento
        print(
            f"Seu aumento será de R${aumento:.2f}, resultando em um novo salário de R${novosalario:.2f}")

    else:
        aumento = (salario * 15) / 100
        novosalario = salario + aumento
        print(
            f"Seu aumento será de R${aumento:.2f}, resultando em um novo salário de R${novosalario:.2f}")

else:
    print("Valor informado não é válido!")
