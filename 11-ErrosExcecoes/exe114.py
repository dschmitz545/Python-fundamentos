"""
Crie um código em Python que teste se o site
pudim está acessível pelo computador usado.
"""

import urllib
import urllib.request
import urllib.error

try:
    site1 = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento")
else:
    print("Consegui acessar o site Pudim normalmente")

try:
    site2 = urllib.request.urlopen("https://weather.dschmitz.dev")
except urllib.error.URLError:
    print("O site weather-dschmitz não está acessível no momento")
else:
    print("Consegui acessar o site weather.dschmitz normalmente")

try:
    site3 = urllib.request.urlopen("https://a.dschmitz.dev")
except urllib.error.URLError:
    print("O site a.dschmitz não está acessível no momento")
else:
    print("Consegui acessar o site a.dschmitz normalmente")

# Bonus, retornonando o conteudo html da página
print(site1.read())
print(site2.read())
