"Entrada para usuario digitar o site, Entrada para palavra de pesquisa"

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from operator import itemgetter

def entrar_navegador():
    lista_produtos = []
    navegador = webdriver.Chrome()
    navegador.get("https://www.mercadolivre.com.br/")

    sleep(2)

# Pesquisa o determinado produto
    pesquisa = captura_usuario
    pesquisa_tv = navegador.find_element(By.ID, "cb1-edit")

    pesquisa_tv.send_keys(pesquisa)
    pesquisa_tv.submit()
    sleep(2)

# Puxar as informações
    conteudo_pag = navegador.page_source
    site = BeautifulSoup(conteudo_pag, 'html.parser')

    flag_pagina_seguinte = True

    while flag_pagina_seguinte == True:

        produtos = site.findAll ('div', attrs={'class': 'ui-search-result'})

        for produto in produtos:
            h_ref = produto.find('a')
            preco = produto.find('span', attrs = {'aria-roledescription': 'Preço'}).contents[1].text
            preco = preco.replace('.', '')
            preco = preco.replace(',', '.') #Trata os dados
            preco = float(preco)

            lista_produtos.append([h_ref['title'], "{:2f}".format(preco), h_ref['href'], preco])

        try:
            btn_seguinte = navegador.find_element(By.XPATH, value= "//a@title=Seguinte']")
            navegador.execute_script("arguments[0].click();", btn_seguinte)
            sleep(5)

        except:
            flag_pagina_seguinte = False
            pass
    
    '''lista_ordenada = sorted(lista_produtos, key = itemgetter(3)) #Variavel que organiza os dados

    for item in lista_ordenada:
        del item[3]

    arq_produtos = pd.DataFrame(lista_ordenada, columns=['Título', 'Preço', 'Link'])
    arq_produtos.to_excel(f'{pesquisa}.xlsx', index = False)

    print (lista_ordenada)
'''

#Cria uma janela
janela = tk.Tk()


#Cria um Label - Produto
label = tk.Label(janela, text = "produto")
label.pack()

#Criar uma area para inserir texto
entrada_txt = tk.Entry(janela, width= 50)
entrada_txt.pack()
captura_usuario = entrada_txt.get()

#Função para armazenar a entrada


#Button: Botão:
botao = tk.Button(janela, text ="executar", command= entrar_navegador)
botao.pack()


janela.mainloop()