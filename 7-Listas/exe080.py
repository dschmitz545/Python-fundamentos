"""
Crie um programa onde o usuário possa digitar 
cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção
(sem usar o sort()). 
No final, mostre a lista ordenada na tela.
"""
lista = list()


for c in range(5):
    n = input("Informe um número: ")

    if n.isnumeric():
        n = int(n)

    # inserindo primeiro elemento
    if len(lista) == 0:
        lista.append(n)
        print("add primeiro elemento")
    
    # Se o numero digitado for maior que o ultimo elemento que já existe
    elif n > lista[- 1]:
        lista.append(n)

    else:
        count2 = 0
        # enquando o contador é menor que o tamanho da lista
        while count2 < len(lista):
            # se o numero digitado é menor que a lista no indice do contador
            if n <= lista[count2]:
                # insere o numero na posição do contador
                lista.insert(count2, n)
                break
            count2 += 1

print(lista)

         




    
#     # se já não fo o primeiro elemento
#     else:
#         print("Já é o segundo")
#         print(len(lista))
#         input()

#         # Busca cada numero ja contido na lista
#         for pos, x in enumerate(lista):

#             # se o num digi é menor que os já contidos?
#             print("entrando no for")
#             print("print lista")
#             print(lista)
#             print("tamanho")
#             print(len(lista))
#             print("x")
#             print(x)
#             print("pos")
#             print(pos)
#             input()
#             if n < x[pos]:
#                 print("entrando no if")
#                 input()
#                 # busca o indice dele:
#                 # print("buscando o indice")
#                 # a = lista.index(x)
#                 # print(a)
#                 # insere antes dele
#                 print("inserindo o próximo")
#                 lista.insert(pos-1, n)
#                 input()
#                 break

#                 # insere por ultimo mesmo
#             else:
#                 print("Inserindo por ultimo mesmo")
#                 input()
#                 lista.append(n)
#                 input()
#         # # if n > lista[len(lista)- 1]: # out of range
#         # if n < lista.find(n):
#         #     a = lista.index()
#         #     print(a)
#         #     # lista.insert(lista.index(-1), n)
#         # else:
#         #     lista.append(n)


# print(lista)