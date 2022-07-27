"""
Um professor quer sortear um dos seus quatro
alunos para apagar o quadro.
Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.
"""
import random

# aluno1 = input("Primeiro Aluno: ")
# aluno2 = input("Segundo Aluno: ")
# aluno3 = input("Terceiro Aluno: ")
# aluno4 = input("Quarto Aluno: ")
# alunoescolhido = random.choice([aluno1, aluno2, aluno3, aluno4])
# print(f"O aluno escolhido foi {alunoescolhido}")

lista = []
for x in range(4):
    aluno = input(f"Aluno {x}: ")
    lista.append(aluno)
alunoescolhido = random.choice(lista)
print(f"O aluno escolhido foi {alunoescolhido}")
