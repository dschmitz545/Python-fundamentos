"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
from email.iterators import typed_subpart_iterator


people = dict()
datapeople = list()
sumagepeople = countpeople = 0
womans = list()

while True:
    people['name'] = str(input("Name: "))
    
    people['sex'] = ' '
    while people['sex'] not in "mf":
        people['sex'] = str(input("Sex: [M/F]: "))[0].lower().strip()

        if people['sex'] not in "mf":
            print("Error! Please, enter only the values Male or Female")


    people['age'] = int(input("Age: "))

    opc = ' '
    while opc not in 'yn':
        opc = str(input("Do you want to continue: [YES/NO]: "))[0].lower().strip()

        if opc not in 'yn':
            print("Error, Anwser only Yes or No")


    # people['name'] = name
    # people['sex'] = sex
    # people['age'] = age

    datapeople.append(people.copy())
    people.clear()

    if opc == 'n':
        break

countpeople = len(datapeople)

for ages in datapeople:
    sumagepeople += ages['age']
mediapeople = sumagepeople / countpeople

# for woman in datapeople:
#     typesex = woman['sex']
#     if typesex == 'f':
#         womans.append(woman['name'])



print("-=" * 40)
print(f"A) We have all {countpeople} people registered")
print(f"B) The average age is {mediapeople:.2f} years")

print(f"c) The womans registered were:",end=" ")
for woman in datapeople:
    typesex = woman['sex']
    if typesex == 'f':
        print(woman['name'],end=" ")
print()

print(f"D) The list of people's above average:")
for listpeople in datapeople:
    if listpeople['age'] > mediapeople:
        print(f"    name = {listpeople['name']}; sex = {listpeople['sex']}; age= {listpeople['age']}")

print()
print("<< Conclude >>")
