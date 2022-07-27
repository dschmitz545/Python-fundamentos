"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
Analise: len(), count(), find()
transformações: replace(), upper(), lower(), capitalize(), title(), strip()
junção com join().
"""
nome = input(f"Digite seu nome completo: ")
maiu = nome.strip()
maiu = maiu.upper()
minu = nome.strip()
minu = minu.lower()
qtdletras = nome.strip()
print(qtdletras)
qtdletras = (len(qtdletras) - nome.count(' '))
primnome = nome.strip()
primnome1 = primnome.split()
prime = primnome1[0]
qtdprime = len(primnome1[0])
print(f"Seu nome maiusculo é {maiu}")
print(f"Seu nome minusculo é {minu}")
print(f"Seu nome tem ao todo {qtdletras} letra")
print(f"Seu primeiro nome é {prime} ele tem ao todo {qtdprime}")
