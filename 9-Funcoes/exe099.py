"""
Faça um programa que tenha uma função chamada maior()
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e
dizer qual deles é o maior.
"""
from random import randint
from time import sleep


def maior(*nums: int):
    print("-=" * 40)
    print("Analisando os valores passados...")
    sleep(0.025)
    qtd = 0
    for x in nums:
        print(f"{x}",end=" ", flush=True)
        sleep(0.1)
        qtd += 1
    print(f"Foram informados {qtd} valores ao todo.")
    sleep(0.5)
    # count = 0
    # if count == 0:
    maior = max(nums)
    # count += 1
    # else:
    #     if maior < nums:
    #         maior = max(nums)
    print(f"maior é informado foi {maior}.")

maior(randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100))
maior(1,2,5,9,10,200,21,365,9887)
maior(25,3,6,987,2,1,-5,-9)
maior(0)
maior(99999,2,36,-6,-7,36,215,2478,25,0,12,32)
