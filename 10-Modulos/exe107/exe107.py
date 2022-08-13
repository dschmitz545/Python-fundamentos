"""
Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use
algumas dessas funções.
"""
from moeda import aumentar, diminuir, dobro, metade

num = float(input("Digite o preço: R$"))

aum = aumentar(num, 10)
print(f"Aumentando 10%, temos R${aum:.2f}")
dim = diminuir(num, 13)
print(f"Diminuindo 13%, temos R${dim:.2f}")
dobr = dobro(num)
print(f"O dobro de R${num:.2f} é R${dobr:.2f}")
met = metade(num)
print(f"A metade de R${num:.2f} é R${met:.2f}")
