"""
O mesmo professor do desafio 19
quer sortear a ordem de apresentação
de trabalhos dos alunos.
Faça um programa que leia o nome dos
quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

# n1 = input("Primeiro Aluno: ")
# n2 = input("Segundo Aluno: ")
# n3 = input("Terceiro Aluno: ")
# n4 = input("Quarto Aluno: ")
# lista = [n1, n2, n3, n4]
# random.shuffle(lista)
# print(lista)

lista = []
for x in range(4):
    aluno = input(f"Aluno {x}: ")
    lista.append(aluno)
shuffle(lista)
print(f"A ordem de apresentação será {lista}")
