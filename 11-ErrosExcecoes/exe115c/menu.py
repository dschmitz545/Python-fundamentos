from dados import lerPessoa, gravarPessoa
from layout import mensagens, titulo, linha, cor


def opcMenu(txt):

    while True:
        try:
            opc = int(input(txt))
            if opc == 1:
                titulo("PESSOAS CADASTRADAS")
                lerPessoa()
                linha()
                continue

            elif opc == 2:
                titulo("CADASTRAR NOVA PESSOA")
                cadastrarPessoa()
                linha()
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
    print(cor[2], "1", cor[0], " -", cor[3], "Ver pessoas")
    print(cor[2], "2", cor[0], " -", cor[3], "Cadastrar novas Pessoas")
    print(cor[2], "3", cor[0], " -", cor[3], "Sair do Sistema", cor[0])
    linha()

def cadastrarPessoa():
    while True:
        try:
            nome = str(input("Informe um nome: "))
            idade = int(input("Informe uma idade: "))

        except TypeError:
            mensagens("Dados digitado não é válido!", 4)
            continue
        
        except ValueError:
            mensagens("Valor digitado não é válido!", 4)
            continue

        except KeyboardInterrupt:
            mensagens("Usuário cancelou a digitação", 4)
            break
        
        else:
            gravarPessoa(nome, idade)
            break