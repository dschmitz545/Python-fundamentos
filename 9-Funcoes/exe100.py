"""
Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai
colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares
sorteados pela função anterior.
"""
from random import randint
from time import sleep

numeros = list()
numpares = []

def sorteia():
    for _ in range(0, 5):
        n = randint(0,100)
        numeros.append(n)
    print(f"Sorteando 5 valores da lista {numeros}, PRONTO!")
    sleep(0.4)
    return numeros


def somaPar(lstnums):
    somapares = 0
    for x in lstnums:
        if x % 2 == 0:
            somapares += x
            numpares.append(x)
        else:
            pass
    sleep(0.65)
    print(f"Somando os valores {lstnums}, temos {somapares}")
    

s = sorteia()
somaPar(s)
