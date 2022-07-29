"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogada = input("Qual é a sua jogada? ")

if jogada.isnumeric() and jogada == '0' or jogada == '1' or jogada == '2':
    jogada = int(jogada)
    lista = ("Pedra", "Papel", "Tesoura")
    #opcoes = (0,1,2)
    #opcpc = random.choice(opcoes)
    opcpc = randint(0,2)

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    sleep(1)

    if jogada == 0 and opcpc == 0:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("EMPATE")
    elif jogada == 0 and opcpc == 1:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("Computador venceu")
    elif jogada == 0 and opcpc == 2:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("Jogador venceu")
    elif jogada == 1 and opcpc == 0:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("Jogador venceu")
    elif jogada == 1 and opcpc == 1:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("EMPATE")
    elif jogada == 1 and opcpc == 2:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("Computador venceu")
    elif jogada == 2 and opcpc == 0:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("Computador venceu")
    elif jogada == 2 and opcpc == 1:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("Jogador venceu")
    elif jogada == 2 and opcpc == 2:
        print("-=-" * 10)
        print(f"Jogar jogou {lista[jogada]}")
        print(f"Computador jogou {lista[opcpc]}")
        print("-=-" * 10)
        print("EMPATE")

    else:
        print("Opção digitada inválida:")

else:
    print("Opção digitada inválida")
