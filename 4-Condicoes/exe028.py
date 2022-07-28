"""
Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na
tela se o usuário venceu ou perdeu.
"""
import random
import time

print("\033[1;93m-=-\033[0;0m" * 20)
print("\033[1;96m Vou pensar em um número de 0 a 5. Tente adivinhar... \033[0;0m")
print("\033[1;93m-=-\033[0;0m" * 20)
numero = input("\033[1;32m Em qual número eu pensei? \033[0;0m ")
print("\033[1;95m PROCESSANDO... \033[0;0m")
time.sleep(2)

if numero.isnumeric():
    numero = int(numero)
    numsort = random.randint(0, 5)
    if numero == numsort:
        print("\033[1;32m Parabéns!! Você acertou \033[0;0m")
    else:
        print(f"\033[1;31m \033[1;101m Numero errado. Eu tinha pensando no {numsort} \033[0;0m")
else:
    print("\033[1;31m Não é um número válido \033[0;0m")
