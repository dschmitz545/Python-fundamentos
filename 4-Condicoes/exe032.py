"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date

ano = input("Digite um ano para saber se ele foi ou será bissexto, ou zero para ano atual: ")

if ano.isnumeric():
    ano = int(ano)
    if ano == 0:
        ano = date.today().year

    else:
        ano = ano

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano de {ano} é bissexto")
            
    else:
        print(f"O ano de {ano} não é bissexto")

else:
    print("Valor informado não é válido")
