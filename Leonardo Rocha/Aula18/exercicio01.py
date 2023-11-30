import requests
from bs4 import BeautifulSoup

def pesquisar_produto():
    produto_pesquisa = input("Qual produto você está procurando: ")
    produto_pesquisa = produto_pesquisa.replace(' ', '+')

    url = f'https://www.amazon.com.br/{produto_pesquisa}'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        resultados = soup.find_all('li', class_= 'nav-search-field')

        for resultado in 