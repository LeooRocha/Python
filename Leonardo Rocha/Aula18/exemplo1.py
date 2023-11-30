#Importar a biblioteca BS4 

from bs4 import BeautifulSoup
import requests

#URL da página web a ser raspada

url =  'https://www.mercadolivre.com.br/'

#Enviar uma solicitação GET para nossa página
response =  requests.get(url)

#Verificar se a solicitação foi bem sucedida
if response.status_code == 200:
    #Criar um objeto BeautifulSoup para analisar o nosso conteúdo

    soup= BeautifulSoup(response.text, 'html.parser')

# Procura o primeiro elemento h1
    h1 = soup.find('h1')

# Exibir o texto dentro da tag h1
    print (f"Título da página: {h1.text}")

# Exibir todos os elementos HTML correspondentes a uma tag específica

# Tag 'a' procura por todos os links na página
    todos_links = soup.find_all('a')

# Exibir os URLs de todos os links na página
    for link in todos_links:
        print(link.get('href'))

# Acessar atributos de um elemento HTML
    img_src = soup.find('img')['src']

    print (img_src)

    # Navegar pela árvore DOM, navegar pelo HTML para encontrar elementos alinhados
    conteudo_div = soup.find('div', class_='ui-pdp-header__title-container')
    conteudo_spam = soup.find('spam', 'class_:')

    # Exibir o texto desnto da tag < div class= 'conteudo' >
    print ('Conteúdo da Div: ')
    print (conteudo_div.text.strip())
    print ('Preço do Produto: ')
    print (conteudo_spam.text.strip())

    # Encontrar todos os elementos de uma classe específica 

    todos_elementos_classe_x = soup.find_all (class_= '')

    print(todos_elementos_classe_x.text.strip())


    # Encontrar o próximo elemento irmão
    elemento_filho = title_tags.find_next_sibling()

    # Encontrar elementos pelo seletor CSS
    elemento_css = soup.select(' .minha-classe_css')
    
else:
    print (f'A solicitação falhou com o código')