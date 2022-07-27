"""
Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de
dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado
"""


def aluguel(dias, kms):
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    if isfloat(kms) and dias.isnumeric():
        kms = float(kms)
        dias = int(dias)
        kmtotpagar = kms * 0.15
        diastot = dias * 60
        totalpagar = diastot + kmtotpagar
        print(f"O total a pagar é de R${totalpagar:.2f}")
    else:
        print("Os valores informados não são válidos")


if __name__ == '__main__':
    diasAlug = input("Quantos dias alugados? ")
    kmRod = input("Quantos km rodados? ")
    aluguel(diasAlug, kmRod)
