"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""
from random import randint

lista = []
escolhidos = []
tot = 1

print("-=" * 20)
print(f"{'GERADOR DE NÚMEROS MEGA SENA':^40}")
print("-=" * 20)
qtd = int(input("Quantos jogos quer gerar?: "))


while tot <= qtd:
    count = 0
    while True:
        num = randint(1, 60)
        
        if num not in lista:
            lista.append(num)
            lista.sort()
            count += 1
        
        if count >= 6:
            break
    
    escolhidos.append(lista[:])
    lista.clear()
    tot += 1

print("-=" * 20)
for x in range(0, qtd):
    print(f"Jogo{x+1:<2}: {escolhidos[x]}")
