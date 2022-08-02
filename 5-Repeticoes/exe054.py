"""
Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas 
já são maiores.
"""
from datetime import datetime


maior = 0
menor = 0

for x in range(7):
    ano = int(input(f"Em que ano nasceu a {x+1}ª pessoa? "))
    idade = datetime.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"A todo tivemos {menor} pessoas menor de idade")
print(f"E também tivemos {maior} pessoas maior de idade")
