"""
Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada 
aluno individualmente.
"""
historico = []
temp = []


while True:

    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2

    temp.append(nome)
    temp.append(n1)
    temp.append(n2)
    temp.append(media)

    historico.append(temp[:])
    temp.clear()

    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input("Quer continuar [S/N]")).lower().strip()

    if opcao == 'n':
        break


print("-=" * 20)
print(f"{'Nº':<3}{'Nome':^15}{'Media':>21}")
print("-" * 40)
for i, c in enumerate(historico):
    print(f"{i:<3}",end="")
    print(f"{historico[i][0]:^15}",end="")
    print(f"{historico[i][3]:>21}",end="")
    print()


while True:

    aluno = int(input("Mostrar nota de qual aluno? [999 interrompe]: "))          

    try:            
        if aluno == 999:
            break
        
        else:
            if aluno <= len(historico):
                print("-" * 40)
                print(f"As notas de {historico[aluno][0]} foram {historico[aluno][1]} e {historico[aluno][2]}")
                print("-" * 40)
    except IndexError as err:
        print("Código inválido")


print("Até Mais")