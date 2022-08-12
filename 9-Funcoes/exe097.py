"""
Faça um programa que tenha uma função
chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
"""


def escreva(txt: str):
    tam = len(txt)
    print("~" * (tam + 2))
    print(f" {txt:^{tam}}")
    print("~" * (tam + 2))


texto = str(input("Digite alguma coisa: "))
escreva(texto)
