from dados import verPessoa, cadastrarPessoa
from layout import mensagens, titulo, linha, cor


def opcMenu(txt):

    while True:
        try:
            opc = int(input(txt))
            if opc == 1:
                verPessoa()
                titulo("Opção 1")
                continue
            elif opc == 2:
                cadastrarPessoa()
                titulo("Opção 2")
                continue
            elif opc == 3:
                titulo("Saindo do Sistema... Até logo!")
                break
            else:
                mensagens("Opção inválida", 4)
                continue
        except TypeError:
            mensagens("Erro! Digite um número inteiro válido", 4)
        except ValueError:
            mensagens("Erro! Digite uma opção válida", 4)
        except KeyboardInterrupt:
            mensagens("Usuário resolveu cancelar a digitação", 4)
            break
        # else:
        #     return opc

def menutxt():
    print(cor[2],"1",cor[0]," -",cor[3],"Ver pessoas")
    print(cor[2],"2",cor[0]," -",cor[3],"Cadastrar novas Pessoas")
    print(cor[2],"3",cor[0]," -",cor[3],"Sair do Sistema",cor[0])
    linha()