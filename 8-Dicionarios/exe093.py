"""
Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
"""
jogador = dict()
partidas = 0
golsqtd = list()

jogador['Nome'] = str(input("Nome do Jogador: "))

partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))

for x in range(0, partidas):
    n = int(input(f"Quantos gols na partida {x+1}? "))
    golsqtd.append(n)

jogador['gols'] = golsqtd
jogador['total'] = sum(golsqtd)

print("-=" * 40)
print(jogador)
print("-=" * 40)

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor} ")
print("-=" * 40)

print(f"O jogador {jogador['Nome']} jogou {len(jogador['gols'])} partidas.")
for cha, val in enumerate(jogador['gols']):
    print(f"    => Na partida {cha+1}, fez {val} gols")
print(f"Foi um total de {jogador['total']} gols")
