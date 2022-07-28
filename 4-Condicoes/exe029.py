"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = input("Qual a velocidade atual do carro? ")

if velocidade.isnumeric():
    velocidade = int(velocidade)
    if velocidade <= 80:
        pass
    else:
        execedente = velocidade - 80
        multa = execedente * 7
        print(f"\033[1;91mMULTADO! Você excedeu o limite permitido que é de 80Km/h")
        print(f"Você deve pagar uma multa de \033[1;93m R${multa:.2f}!")

    print("\033[1;92mTenha um bom dia! dirija com segurança \033[0;0m")
else:
    print("Valor digitado não é valido")
