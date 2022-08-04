"""
Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor 
valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
"""
opcao = ''
count = 0
media = 0
maior = 0
menor = 0
soma = 0

while opcao != 0:
    entrada = input("Informe um número, ou 0[zero] para encerar: ")

    if entrada.isnumeric():
        entrada = int(entrada)
        opcao = int(entrada)

        if entrada != 0:
            count  += 1
            soma = soma + entrada

            if count == 1:
                maior = entrada
                menor = entrada
            else:
                if entrada > maior:
                    maior = entrada
                elif entrada < menor:
                    menor = entrada

        else:
           opcao = entrada

        media = soma / count
    else:
        print("Valor digitado não é válido")

print(f"A média de todos os números digitados foi {media}")
print(f"O maior números digitados foi {maior}")
print(f"O menor números digitados foi {menor}")