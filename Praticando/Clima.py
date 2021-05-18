import requests
from bs4 import BeautifulSoup

cidade = str(input("Cidade "))
url = "https://www.google.com/search?&q=weather=weather=clima-em-" + cidade

requisicao = requests.get(url)
soup = BautifulSoup(requisicao.text, "html.parser")

resultado = soup.find("div", class_="BNeawe"). text
print(resultando)
