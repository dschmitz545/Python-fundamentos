"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
"""

comprabruta = input("Preço das compras: ")
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão \n")

opcaomenu = input("qual é a opção: ")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if isfloat(comprabruta) and opcaomenu.isnumeric():
    comprabruta = float(comprabruta)
    opcaomenu = int(opcaomenu)
    comprabruta = 0
    compraliquida = 0

    if opcaomenu == 1:
        desconto = comprabruta * 10 / 100
        compraliquida = comprabruta - desconto

    elif opcaomenu == 2:
        desconto = comprabruta * 5 / 100
        compraliquida = comprabruta - desconto

    elif opcaomenu == 3:
        compraliquida = comprabruta

    elif opcaomenu == 4:
        qtdparcela = input("Quantas parcelas? ")

        if qtdparcela.isnumeric():
            qtdparcela = int(qtdparcela)
            acrescimobruto = comprabruta * 20 / 100
            acrescimentoliquido = (comprabruta + acrescimobruto) / qtdparcela
            compraliquida = comprabruta + acrescimobruto
            print(
                f"Sua compra será parcelada em {qtdparcela}x de R${acrescimentoliquido:.2f} COM JUROS")

        else:
            pass

    else:
        print("Opção digitada foi inválida")

    print(
        f"Sua compra de R${comprabruta:.2f} vai custar R${compraliquida:.2f} no final")

else:
    print("Opção digita inválida")
