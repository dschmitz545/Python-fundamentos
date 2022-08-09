dados = list()
pessoas = list()

lista2 = [[[],[]],[[],[]]]
dados.append("Pedro")
dados.append(25)

dados.append("Maria")
dados.append(30)
print(dados)

pessoas.append(dados[:])
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[0][2])
print(pessoas[0][3])

count = 0
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            for l in range(0, 2):
                for m in range(0, 2):
                    for n in range(0, 2):
                        for o in range(0, 2):
                            for p in range(0, 2):
                                lista2[p].append(int(input(f"digite um numero {i} {j} {k} {l} {m} {n} {o} {p}: ")))
                                count += 1

print(lista2)
print(count)
