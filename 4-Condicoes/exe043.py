"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
Peso ÷ (Altura × Altura)
"""
peso = input("Informe seu peso: ")
altura = input("Infome sua altura: ")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if isfloat(peso) and isfloat(altura):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura * altura)
    print(imc)

    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso ideal")
    elif 25 <= imc < 30:
        print("sobrepeso")
    elif 30 <= imc < 40:
        print("obesidade")
    elif imc >= 40:
        print("Obesidade morbida")
    else:
        pass

else:
    print("Valores digitados não são válidos")
