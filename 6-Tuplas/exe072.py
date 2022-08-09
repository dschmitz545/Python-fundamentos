"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
"""

sequencia = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
             "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
             "Doze", "Treze", "Quatorze", "Quinze", "Dezeseis",
             "Dezesete", "Dezoito", "Dezenove", "Vinte")

while True:
    numero = int(input("Digite um número entre 0 e 20: "))

    while numero not in range(0, 21):
        numero = int(input("Tente novamente. Digite um número entre 0 e 20: "))

    print(sequencia[numero])

    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input("Deseja continuar? [S/N]")).strip().lower()[0]

    if resposta == 'n':
        break

print("Até logo")



