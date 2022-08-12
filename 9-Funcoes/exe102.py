"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será
um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
"""
from time import sleep


def fatorial(num, show: bool = False):
    """
        -> Calcula o fatorial de um número
        :param num: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta
        :return: O valor do Fatorial de um número num

    """
    print("-" * 40)
    sleep(0.25)
    fat = 1
    count = num
    while count > 0:
        fat = fat * count
        if show == True:
            if count > 1:
                sleep(0.25)
                print(f"{count} X ", end="", flush=True)
            else:
                sleep(0.25)
                print(f"{count} = ", end="", flush=True)
        count -= 1
    return fat


numero = int(input("Digite um número para saber seu fatorial: "))

procs = " "
while True:
    procs = str(input("Mostrar processo? [S/N]: "))[0].lower().strip()

    if procs in "sn":
        break

if procs == "n":
    show = False
else:
    show = True


fat = fatorial(numero, show)
print(fat)
help(fatorial)
