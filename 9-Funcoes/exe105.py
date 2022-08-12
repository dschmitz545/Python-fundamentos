"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""


def notas(*nots, sit: bool = False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param nots: umas ou mais notas dos alunos(aceita vários)
    :param sit: (Opcional), indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    # Outra forma de solucionar
    r = dict()
    r["total"] = len(nots)
    r["mario"] = max(nots)
    r["menor"] = min(nots)
    r["media"] = sum(nots) / len(nots)

    boletin = {}
    maior = menor = media = 0

    boletin["total"] = len(nots)
    for n in range(0, len(nots)):
        if n == 0:
            maior = nots[n]
            menor = nots[n]

        else:
            if maior < nots[n]:
                maior = nots[n]
            elif menor < nots[n]:
                menor = nots[n]

    boletin["maior"] = maior
    boletin["menor"] = menor

    media = sum(nots) / len(nots)

    boletin["media"] = media
    if sit == True:
        if media < 6:
            boletin["situacao"] = "Ruim"
            r["situacao"] = "Ruim"
        elif media <= 6.5:
            boletin["situacao"] = "Razoável"
            r["situacao"] = "Razoável"
        elif media > 6 and media < 7.5:
            boletin["situacao"] = "Regular"
            r["situacao"] = "Regular"
        elif media >= 7 and media < 9:
            boletin["situacao"] = "Boa"
            r["situacao"] = "Boa"
        else:
            boletin["situacao"] = "Excelente"
            r["situacao"] = "Excelente"

    return print(boletin)


notas(0, 1, 10, 2, 8.5, 3)
# help(notas)
