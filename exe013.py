"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento
"""


def aumento():

    salario = input("Qual é o salário do Funcionário? R$")

    def isfloat(num):
        try:
            float(num)
            return True
        except TypeError:
            return False

    if isfloat(salario):
        salario = float(salario)
        peraum = 15
        aument = salario * (peraum / 100)
        novosalario = salario + aument
        print(f"Um funcionário que ganhava R${salario:.2f}, com {peraum}% de aumento,\
passa a receber R${novosalario:.2f}")
    else:
        print("Valor informando é inválido")


if __name__ == '__main__':
    aumento()
