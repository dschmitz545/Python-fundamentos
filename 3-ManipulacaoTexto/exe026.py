"""
Faça um programa que leia uma frase pelo
teclado e mostre quantas vezes aparece a
letra “A”, em que posição ela aparece na
primeira vez e em que posição ela aparece
na última vez.
"""
frase = input("digite uma frase: ")

frase = frase.strip()
frase = frase.lower()
a1 = frase.count("a")
pos1 = frase.find("a")+1
pos2 = frase.rfind("a")+1
print(f"A letra A apareçeu {a1} vezes na frase")
print(f"A primeira letra A apareceu na posição {pos1}")
print(f"A ultima letra A apareceu na posição {pos2}")
