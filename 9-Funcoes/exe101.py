"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de
uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(nasc: int):
    from datetime import date

    idade = date.today().year - nasc
    if idade < 15:
        return f"Com {idade}: Não vota"
    elif idade > 15 and idade <= 65:
        return f"Com {idade}: Voto Obrigatório"
    else:
        return f"Com {idade}: Voto Opcional"


ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
