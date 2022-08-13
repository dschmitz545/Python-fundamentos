def aumentar(n=0, taxa=0, moe="R$"):
    aum = (n * taxa) / 100
    val = n + aum
    ret = moeda(val, moe)
    return ret


def diminuir(n=0, taxa=0, moe="R$"):
    dim = (n * taxa) / 100
    val = n - dim
    ret = moeda(val, moe)
    return ret


def dobro(n=0, moe="R$"):
    dbr = n * 2
    ret = moeda(dbr, moe)
    return ret


def metade(n=0, moe="R$"):
    met = n / 2
    ret = moeda(met, moe)
    return ret


def moeda(val: float, moeda="R$"):
    numf = f"{moeda}{val:.2f}".replace(".", ",")
    return numf
