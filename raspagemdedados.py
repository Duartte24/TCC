#raspagem de dados
from bs4 import BeautifulSoup
import requests

link_site = "file:///C:/Users/Usu%C3%A1rio/Desktop/PROGRAMAS/index.html"

acessar_site = requests.get(link_site)

print(acessar_site.text)

site = BeautifulSoup(acessar_site.text , "html.parser")

