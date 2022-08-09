"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
time = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", 
        "Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo",
        "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife",
        "EC Vitória", " Coritiba", "Avaí", "Ponte Preta", "Atlético-GO"
       )

print(f"Os cinco primeiros times são {time[0:5]}")
print(f"Os ultimos quatro colocados são {time[-4:]}")
print(f"Times em ordem alfabética: {sorted(time)}")
print(f"Posição da chapecoense: {time.index('Chapecoense')}")
