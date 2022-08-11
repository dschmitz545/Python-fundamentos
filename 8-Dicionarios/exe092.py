"""
Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-o (com idade) em
um dicionário. Se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com
quantos anos a pessoa vai se aposentar.
"""
from datetime import date, datetime

trabalhador = dict()


trabalhador['Nome'] = str(input("Nome: "))
trabalhador['Idade'] = date.today().year - int(input("Informe o ano de nascimento: "))
trabalhador['ctps'] = int(input("Carteira de trabalho (0 Não tem): " ))

if trabalhador['ctps'] == 0:
    print("-=" * 30)
    for k, v in trabalhador.items():
        print(f"    - {k} tem o valor {v}")

else:
    trabalhador['contratação'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = int(input("Salário: R$"))
    trabalhador['aposentadoria'] = trabalhador['Idade']+ ((trabalhador["contratação"] + 35) - date.today().year)
    print("-=" * 30)
    for k, v in trabalhador.items():
        print(f"    - {k} tem o valor {v}")
