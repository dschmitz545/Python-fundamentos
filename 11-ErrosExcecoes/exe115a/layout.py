def linha(tam : int = 40):
    print("-" * tam)

def titulo(txt : str = ''):
    linha()
    print(f"{txt:^40}")
    linha()

def mensagens(txt, colors=0):
    print(cor[colors],txt,cor[0])


cor = ("\033[m",          # 0 sem cor
     "\033[0;30;41m",   # 1 fundo vermelho
     "\033[1;93m",      # 2 amarelo
     "\033[1;94m",      # 3 azul claro
     "\033[1;31m"       # 4 vermelho
     )


