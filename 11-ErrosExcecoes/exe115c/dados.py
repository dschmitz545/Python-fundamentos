arq = "dadospessoa.txt"

def criarArquivo():
    try:
        a = open(arq, "wt+", encoding="UTF-8")
        a.close()
    except:
        print("Houve erro na criação do arquivo")
    else:
        print(f"Arquivo {arq} criado com sucesso")


def existearquivo():
    try:
        a = open(arq, "rt", encoding="UTF-8")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def lerPessoa():
    try:
        a = open(arq, "rt", encoding="UTF-8")
    except:
        print("Erro ao ler aquivo")
    else:
        for l in a:
            dado = l.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def gravarPessoa(nome, idade):
    try:
        a = open(arq, "at", encoding="UTF-8")
    except:
        print("Não consegui abrir o arquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever no arquivo")
        else:
            print(f"Novo registro adicionado {nome} {idade}")
    finally:
        a.close()

