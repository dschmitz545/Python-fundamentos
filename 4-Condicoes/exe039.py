"""
Faça um programa que leia o ano de nascimento de
um jovem e informe, de acordo com a sua idade, se ele
ainda vai se alistar ao serviço militar, se é a hora
exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import datetime

nascimento = input("Informe o ano de nascimento(YYYY): ")

if nascimento.isnumeric() and len(nascimento) == 4:
    nascimento = int(nascimento)
    anoatual = datetime.today().year
    print(anoatual)
    idade = anoatual - nascimento

    if idade <= 18:
        faltante = 18 - idade
        alistamento = anoatual + faltante
        print(f"Quem nasceu em {nascimento} tem {idade * (-1)} em {anoatual}")
        print(f"Ainda faltam {faltante} ano(s) para o alistamento")
        print(f"Seu alistamento será em {alistamento}")
    elif idade >= 18:
        passou = idade - 18
        alistamento = anoatual - passou
        print(f"Quem nasceu em {nascimento} tem {idade} em {anoatual}")
        print(f"Você deveria ter se alistado há {passou} ano(s)")
        print(f"Seu alistamento foi em {alistamento}")
    elif idade == 18:
        print(f"Quem nasceu em {nascimento} tem 18 anos em {anoatual}")
        print("Você tem que se alistar IMEDIATAMENTE")

    else:
        pass

else:
    print("Valor informado é inválido")
