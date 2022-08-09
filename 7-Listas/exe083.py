"""
Crie um programa onde o usuário digite
uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados
na ordem correta.
"""

# # Primeira versão
# expressao = str(input("Digite a expressão: "))

# qtd1 = expressao.count("(")
# qtd2 = expressao.count(")")


# if qtd1 == qtd2:
#     print("Sua expressão está correta:")
# else:
#     print("Sua expressão está incorreta")

pilha =[]
aa = 0
bb = 0

expressao = str(input("Digite a expressão: "))

for x in expressao:
    if x == "(":
       pilha.append("(")

    elif x == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão está correta:")
else:
    print("Sua expressão está incorreta")