"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.
"""

valcasa = input("Qual o valor da casa? ")
salcomprador = input("Qual o salário do comprador? ")
anos = input("Quantos anos para pagar? ")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if isfloat(valcasa) and isfloat(salcomprador) and anos.isnumeric():
    valcasa = float(valcasa)
    salcomprador = float(salcomprador)
    anos = int(anos)

    meses = anos * 12
    valprestacao = valcasa / meses
    pisomaximo = (salcomprador * 30) / 100
   
    if pisomaximo < valprestacao:
        situcaoempresimo = "negado"
        cor = "\033[0;37;41m"
    else:
        situcaoempresimo = "concedido"
        cor = "\033[0;37;42m"

    print(f"Para pagar uma casa de R${valcasa:.2f} em {anos} anos a prestação será de R${valprestacao:.2f}")
    print(f"Status do emprestimo: {cor}{situcaoempresimo.upper()}")
else:
    print("Valor informado não é válido")
