"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre 
eles (desconsiderando o flag).
"""
entrada = 0
count = 0
parada = 0
numero = 0

while parada != 999:
    entrada = input("Digite um número[999 para parar]: ")
    
    if entrada.isnumeric():
        entrada = int(entrada)

        if entrada != 999:
            numero = numero + entrada
            count += 1
        else:
            parada = entrada

    else:
        print("Valor digitado não é válido")

print(f"Você digitou {count} números e a soma entre eles foi {numero}")
