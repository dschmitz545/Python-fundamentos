"""
Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão.
Refaça o DESAFIO 51, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
Melhore o DESAFIO 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele
disser que quer mostrar 0 termos. 
"""

termo = input("Informe o primeiro termo: ")
razao = input("Informe a razão: ")
qtd = input("Quantos termos você quer exibir? ")

if termo.isnumeric() and razao.isnumeric() and qtd.isnumeric():
    termo = int(termo)
    razao = int(razao)
    qtd = int(qtd)
    count = 1
    opcao = 5
    primeiraexecucao = 1
    # qtd = termo + ((10 -1 ) * razao)
    # for x in range(termo, razao + qtd, razao):
    #     print(x)


    while opcao != 0:

        if primeiraexecucao == 1:

            while  count <= qtd:
                print(termo)
                termo = termo + razao
                count = count + 1
            print("Fim")
            primeiraexecucao == 2
            
        print("Deseja informar outro termo?")
        print("[1] para novo termo")
        print("[0] para sair")
        opcao = input("").strip()
        

        if opcao.isnumeric():
            opcao = int(opcao)
            

            if opcao == 1:
                termo = input("Informe o primeiro termo: ")
                razao = input("Informe a razão: ")
                qtd2 = input("Quantos termos você quer exibir? ")

                if termo.isnumeric() and razao.isnumeric() and qtd2.isnumeric():
                    termo = int(termo)
                    razao = int(razao)
                    qtd2 = int(qtd2)
                    count = 1

                    while  count <= qtd2:
                        print(termo)
                        termo = termo + razao
                        count = count + 1
                else:
                    print("Valor digitado não é válido")
            else:
                print("Até logo")

        else:
            print("Valor digitado não é válido")

else:
    print("Valores digitados não são válidos")
