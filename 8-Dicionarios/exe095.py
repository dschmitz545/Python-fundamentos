"""
Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
Aprimore o desafio 93 para que ele funcione com
vários jogadores,incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
"""
jogadores = []
jogador = dict()
partidas = 0
golsqtd = list()

while True:

    jogador["nome"] = str(input("Nome do Jogador: "))

    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for x in range(0, partidas):
        n = int(input(f"Quantos gols na partida {x+1}? "))
        golsqtd.append(n)

    jogador["gols"] = golsqtd.copy()
    jogador["total"] = sum(golsqtd)

    jogadores.append(jogador.copy())
    golsqtd.clear()
    jogador.clear()

    opc = " "
    while opc not in "sn":
        opc = str(input("Quer continuar: [S/N]: ")[0].lower().strip())

    if opc == "n":
        break


print("-=" * 40)
print(jogadores)
print("-=" * 40)

print(f"{'Codº':<5}{'Nome':<10}{'Gols':<12}{'Total':>18}")
print("-=" * 40)
for k, joga in enumerate(jogadores):
    # print(joga)
    print(f"{k:<5}", end="")
    print(f"{joga['nome']:<10}", end="")
    print(f"{joga['gols']}", end="")
    print(f"{joga['total']:>18}")

while True:

    detalhar = int(input("Mostrar dados de qual jogador? [999 interrompe]: "))

    try:
        if detalhar == 999:
            break
        else:

            if detalhar <= len(jogadores):
                print(
                    f"-- LEVANTAMENTO DO JOGADOR {jogadores[detalhar]['nome'].upper()}:"
                )
                for i, g in enumerate(jogadores[detalhar]["gols"]):
                    print(f"    - No jogo {i+1} fez {g} gols")
            else:
                print(f"Erro. Não existe jogador com código {detalhar}!")
    except IndexError as err:
        print("Código inválido")

print("Até Mais")
