"""
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade
"""


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print("\033[1;31mErro! digite um número real válido\033[m")
            continue
        else:
            return n


def leiaInt(msg):
    """
    -> verifica se o valor digitado é um número inteiro
    :param msg: Mensagem que irá aparecer solicitando um número para o usuário
    :return n: Retorna o número inteiro
    """
    while True:
        try:
            n = int(input(msg))

        except TypeError:
            print("\033[1;31mErro! Favor digitar um número inteiro válido\033[m")
            continue

        except ValueError:
            print("\033[1;31mErro! Favor digitar um número inteiro válido\033[m")
            continue

        else:
            return n


numint = leiaInt("Digite um número inteiro: ")
numfloat = leiaFloat("Digite um número real: ")
print(f"Você acabou de digitar o número {numint}")
print(f"Você acabou de digitar o número {numfloat}")
