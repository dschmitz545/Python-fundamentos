"""
Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente.
"""
numerosdigi = []
numerosfilt = []

while True:

    numerosdigi.append(int(input("Digite um valor: ")))
    
    for num in numerosdigi:
        if num not in numerosfilt:
            numerosfilt.append(num)
            print("Número adicionado com sucesso...")
        
    opcao = ' '
    while opcao not in ('sn'):
        opcao = str(input("Quer continuar? [S/N]: ")).lower().strip()
    
    if opcao == 'n':
        break
    
# print(sorted(numerosdigi))
print(f"Você adicionou os valores {sorted(numerosfilt)}")