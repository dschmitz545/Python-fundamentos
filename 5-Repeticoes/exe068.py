"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo. 
"""

from random import randint

count = 0

while True:
    print("-=-" * 20)
    print("Vamos jogar par ou impar")
    print("-=-" * 20)

    jogador = input("Diga um número: ")

    if jogador.isnumeric():
        jogador = int(jogador)
        computador = randint(0, 10)

        resultado = computador + jogador
        mao = ' '
        while mao not in 'pi':

            mao = input("Par ou Ímpar? [P/I] ").lower().strip()[0]

        print(f"Você jogou {jogador} e o computador {computador}. Total de {resultado}")
        print(f"Deu par" if resultado % 2 == 0 else 'Deu impar')

        if mao == 'p':
            if resultado % 2 == 0:
                print("Você venceu")
                count += 1
            else:
                print("Você perdeu")
                break
        elif mao == 'i':
            if resultado % 2 == 1:
                print("Você venceu")
                count += 1
            else:
                print("Você perdeu")
                break
        print("Vamos jogar novamente...")

    else:
        print("Valor digitado não é válido")

print(f"Game Over, você ganhou {count} vezes")
