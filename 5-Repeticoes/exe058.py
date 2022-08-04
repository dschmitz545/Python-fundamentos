"""
Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na
tela se o usuário venceu ou perdeu.
Melhore o jogo do DESAFIO 28 onde o computador 
vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar 
até acertar, mostrando no final quantos 
palpites foram necessários para vencer
"""
import random
import time

print("\033[1;93m-=-\033[0;0m" * 20)
print("\033[1;96m Vou pensar em um número de 0 a 10. Tente adivinhar... \033[0;0m")
print("\033[1;93m-=-\033[0;0m" * 20)
numero = input("\033[1;32m Em qual número eu pensei? \033[0;0m ")
print("\033[1;95m PROCESSANDO... \033[0;0m")
time.sleep(2)

if numero.isnumeric():
    numero = int(numero)
    numsort = random.randint(0, 10)
    palpites = 0

    while numero != numsort:
        if numero > numsort:
            condicao = 'Menos'
        else:
            condicao = 'Mais'
        print(f"\033[1;31m \033[1;101m {condicao}... Tente mais uma vez\033[0;0m")
        numero = input(f"\033[1;32m Em qual número eu pensei?\033[0;0m ")
        if numero.isnumeric():
            numero = int(numero)
            palpites += 1
        else:
            print("\033[1;31m Não é um número válido \033[0;0m")
    print(f"\033[1;32m Parabéns!! Você acertou, com {palpites} tentativas\033[0;0m")
else:
    print("\033[1;31m Não é um número válido \033[0;0m")
