"""
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função
input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)
"""

def leiaInt(msg):
    """
        -> verifica se o valor digitado é um número inteiro
        :param msg: Mensagem que irá aparecer solicitando um número para o usuário
        :return n: Retorna o número inteiro
    """
    isvalid = False
    while isvalid == False:
        n = str(input(msg))

        if n.isnumeric():
            n = int(n)
            isvalid = True
            return n
        else:
            print("\033[1;31mErro! digite um número inteiro válido\033[m")


num = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {num}")

# help(leiaInt)
