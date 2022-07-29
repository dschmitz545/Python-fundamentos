"""A Confederação Nacional de Natação 
precisa de um programa que leia o ano 
de nascimento de um atleta e mostre 
sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
from datetime import date

anonascimento = input("Informe o ano de nascimento(YYYY): ")

if anonascimento.isnumeric() and len(anonascimento) == 4:
    anonascimento = int(anonascimento)
    anoatual = date.today().year
    idadeatleta = anoatual - anonascimento
    classificacao = ''
    if idadeatleta <= 9:
      classificacao = 'mirim'
    elif 9 > idadeatleta <= 14:
        classificacao = 'infantil'
    elif 14 > idadeatleta <= 19:
        classificacao = 'júnior'
    elif 19 > idadeatleta <= 25:
        classificacao = 'senior'
    elif idadeatleta > 25:
        classificacao = 'master'
    else:
        pass

    print(f"O atleta tem {idadeatleta} ano(s).")
    print(f"classificação: {classificacao.upper()}")

else:
    print("Ano inválido")
