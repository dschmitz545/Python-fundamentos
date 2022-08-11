"""
Crie um programa onde 4 jogadores joguem um dado e tenham 
resultados aleatórios. Guarde esses resultados em um dicionário
em Python. No final, coloque esse dicionário em ordem, sabendo que
o vencedor tirou o maior número no dado.
"""

from operator import itemgetter
from random import randint
from time import sleep


jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}

print("Valores Sorteados:")

for k, v in jogo.items():
    sleep(0.5)
    print(f"{k} tirou {v} no dado")

print("-=" * 40)
print("RANKING DOS JOGADORES")
sleep(1)

for item in sorted(jogo, key=jogo.get, reverse=True):
    print(f"O {item} tirou {jogo[item]} nos dados")
    sleep(0.5)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f" {i+1}º lugar: {v[0]} tirou {[v[1]]} nos dados")
