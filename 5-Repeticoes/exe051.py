"""
Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão.
"""
termo = input("Informe o primeiro termo: ")
razao = input("Informe a razão: ")

if termo.isnumeric() and razao.isnumeric():
    termo = int(termo)
    razao = int(razao)
    qtd = termo + ((10 -1 ) * razao)
    for x in range(termo, razao + qtd, razao):
        print(x)
