"""
Desenvolva um programa que pergunte
a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas.
"""

distancia = input("De quantos Km é a viagem? ")

if distancia.isnumeric():
    distancia = int(distancia)

    if distancia <= 200:
        valorcobrado = distancia * 0.50
        
    else:
        valorcobrado = distancia * 0.45
    print(f"O preço da viagem será de R${valorcobrado:.2f}")
else:
    print("Valor digitado não é válido")