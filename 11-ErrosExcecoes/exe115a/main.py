"""
Vamos criar um menu em Python, usando modularização
"""

from layout import titulo
from menu import opcMenu, menutxt

while True:
    titulo('MENU PRINCIPAL')
    menutxt()
    n = opcMenu("Sua Opção: ") 
    break