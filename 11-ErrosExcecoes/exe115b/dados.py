def criarArquivo(nome):
    try:
        a = open(nome, "wt+", encoding="UTF-8")
        a.close()
    except:
        print("Houve erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")


def existearquivo(nome):
    try:
        a = open(nome, "rt", encoding="UTF-8")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def verPessoa(nome):
    try:
        a = open(nome, "rt", encoding="UTF-8")
    except:
        print("Erro ao ler aquivo")
    else:
        return a.read()


def cadastrarPessoa():
    pass
