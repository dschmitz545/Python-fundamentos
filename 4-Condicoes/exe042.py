"""
Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar 
que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""

print("-=-" * 10)
print("Analisador de triângulo")
print("-=-" * 10)

r1  = input("Primeiro segmento: ")
r2  = input("Segundo segmento: ")
r3  = input("Terceiro segmento: ")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if isfloat(r1) and isfloat(r2) and isfloat(r3):
    r1 = float(r1)
    r2 = float(r2)
    r3 = float(r3)

    if r1 < (r3 + r2) and r2 < (r1 + r3) and r3 < (r1 + r2):
        if r1 == r2 == r3:
            print("Os segmentos acima podem formar EQUILATERO")
        elif r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2:
            print("Os segmentos acima pode formar ISÓSCELES")
        elif r1 != r2 != r3 != r1:
            print("Os segmentos acima podem formar ESCALENO")
    else:
        print("Não é possível formar um triângulo")

else:
    print("Valores informados não são válidos")