"""
Crie um programa que tenha uma tupla com várias
palavras (não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.
"""


palavras = ("uva", "macarao", "feijao", "teclado", "computador", "aluno",
            "estudante", "programador", "paralelepipedo", "programa",
            "tupla", "lista", "exercicio")

vogais = ("a","e","i","o","u")


for palavra in palavras:
    print(f"\nNa palavra {palavra} temos: ", end="")
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=" ")
print("\n")
print("-" * 20)
print("Fim")

    