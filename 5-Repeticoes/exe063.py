"""
Escreva um programa que leia um número N 
inteiro qualquer e mostre na tela os N primeiros 
elementos de uma Sequência de Fibonacci. 
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""

# def fibonacci(i):
#     resultado = [0, 1]
#     for _ in range(2, i):
#         resultado.append(sum(resultado[-2:]))
#     return resultado


# if __name__ == "__main__":
#     # Listar os 20 primeiro números da sequência
#     for fib in fibonacci(12):
#         print(fib)

print("--" * 30)
print("Sequência de Fibonacci")
qtd = input("Informe quantos elementos da sequência de fibonacci quer exibir: ")

if qtd.isnumeric():
    qtd = int(qtd)

    count = 3
    seq1 = int(0)
    seq2 = int(1)

    print(f"{seq1} - {seq2} - ",end='')
    while count <= qtd :
        seq3 = seq1 + seq2
        count += 1
        print(f"{seq3} - ", end='')
        seq1 = seq2
        seq2 = seq3
    print("FIM")

else:
    print("Valor digitado é inválido")
