"""
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
"""
qtd = 0
soma = 0
while True:
    numero = input("Digite um valor [999 para parar]: ")

    if numero.isnumeric():
        numero = int(numero)

        if numero == 999:
            break

        soma += numero
        qtd += 1

    else:
        print("Valor digitado não é válido")

print(f"A soma de todos os números digitados foi: {soma}")
print(f"Ao todo você digitou {qtd} números")