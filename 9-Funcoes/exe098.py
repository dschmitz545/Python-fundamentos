"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através
da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def geralayout(txt: str):
    tam = len(txt)
    print("-=" * (tam // 2 + 1))
    print(f" {txt:^{tam // 2}}")
    print("-=" * (tam // 2 + 1))


def geracontador(ini: int = 10, fin: int = 0, pas: int = -1, tex: str = "contador"):
    geralayout(tex)
    for x in range(ini, fin, pas):
        print(x, end=" ", flush=True)
        sleep(0.075)
    print("FIM")
    print()


geracontador(tex="Contador de 10 até 9 pulando de 1 em 1")
geracontador(ini=10, fin=-2, pas=-2, tex="Contagem de 10 até 0 de 2 em 2")

geralayout("Agora é sua vez de personalizar a contagem!")
texto = str(input("Qual o seu contador? "))
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))


geracontador(inicio, fim, passo, texto)
