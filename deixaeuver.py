# raspagem de dados
from bs4 import BeautifulSoup

# Caminho para o arquivo local
caminho_arquivo = "C:/Users/Usuário/Desktop/PROGRAMAS/index.html"

# Abrir o arquivo e ler o conteúdo
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo_html = arquivo.read()

# Analisar o conteúdo com BeautifulSoup
site = BeautifulSoup(conteudo_html, "html.parser")

# Exemplo: imprimir o HTML analisado
print(site.prettify())
