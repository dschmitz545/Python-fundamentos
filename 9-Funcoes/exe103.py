"""
Faça um programa que tenha uma função chamada
ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""

from curses.ascii import isalpha


def ficha(jog: str = '<desconhecido>', gol: int = 0):
    """
        -> Retorna a ficha do jogador
        :param jog: (Opcional)Nome do jogador.Default=<desconhecido>
        :param gol: (Opcional)Quantidade de gols. Default=0
    """
    return(print(f"O jogador {jog} fez {gol}(s) no campeonato"))


nome = str(input("Nome do Jogador: "))
gols = str(input("Número de Gols: "))


if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

help(ficha)