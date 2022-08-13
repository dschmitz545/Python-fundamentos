"""
Agora, Vamos ver como fazer acesso
a arquivos usando o Python
"""

from dados import existearquivo, criarArquivo
from layout import titulo, mensagens
from menu import opcMenu, menutxt
from time import sleep

arq = "dadospessoa.txt"
mensagens("Procurando base de dados", 3)
sleep(0.5)

if existearquivo(arq):
    mensagens("Base de dados encontrada", 6)
    sleep(0.5)
else:
    mensagens("Base de dados não encontrada", 4)
    sleep(0.5)
    mensagens("Criando base dados", 2, e=" ")
    criarArquivo(arq)


while True:
    titulo('MENU PRINCIPAL')
    menutxt()
    n = opcMenu("Sua Opção: ", arq) 
    break