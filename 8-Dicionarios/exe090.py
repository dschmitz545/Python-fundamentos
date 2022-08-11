"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()

aluno['Nome'] = str(input("Nome: "))
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

print("-=" * 40)

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 7 and aluno['Média'] >= 5:
    aluno['Situção'] = 'Recuperação'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f"{k} é igual a {v}")


# print(f"- Nome é igual a {aluno['nome']}")
# print(f"- Média é igual a {aluno['media']}")
# print(f"- Situação é igual a {aluno['situacao']}")
