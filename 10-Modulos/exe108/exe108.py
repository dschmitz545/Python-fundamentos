"""
Adapte o código do desafio 107,
criando uma função adicional chamada moeda()
que consiga mostrar os números como 
um valor monetário formatado.
"""
from moeda import aumentar, diminuir, dobro, metade, moeda

num = float(input("Digite o preço: R$"))

aum = aumentar(num, 10, "GPB")
print(f"Aumentando 10%, temos {aum}")
dim = diminuir(num, 13)
print(f"Diminuindo 13%, temos {dim}")
dobr = dobro(num)
print(f"O dobro de {moeda(num)} é {dobr}")
met = metade(num, "U$")
print(f"A metade de {moeda(num, 'U$')} é {met}")
