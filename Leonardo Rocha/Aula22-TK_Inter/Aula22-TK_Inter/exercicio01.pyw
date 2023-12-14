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
import openpyxl
import matplotlib.pyplot as plt
import pyautogui

# Função entrar navegador
def entrar_navegador():
    lista_produtos = []
    navegador = webdriver.Chrome()
    navegador.get("https://www.mercadolivre.com.br/")

    sleep(2)

# Pesquisa o determinado produto
    pesquisa = entrada_txt.get() #Termo para armazenar o valor do Entry
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
            btn_seguinte = navegador.find_element(By.XPATH, value="//a[@title='Seguinte']") 
            navegador.execute_script("arguments[0].click();", btn_seguinte)
            sleep(5)

        except:
            flag_pagina_seguinte = False
            pass
    
    lista_ordenada = sorted(lista_produtos, key = itemgetter(3)) #Variavel que organiza os dados

    for item in lista_ordenada:
        del item[3]

    arq_produtos = pd.DataFrame(lista_ordenada, columns=['Título', 'Preço', 'Link'])
    arq_produtos.to_excel(f'{pesquisa}.xlsx', index = False)

    print (lista_ordenada)

# Função que mostra a tabela/Gera o gráfico
def caminho_arquivo():
    grafico = (f'{entrada_txt.get()}.xlsx')
    df_grafico = pd.read_excel(grafico)

    df_grafico.plot(x = 'Título', y =['Preço'], kind='bar')

    plt.xlabel("Título")
    plt.ylabel("Preço")
    plt.show()

#Cria uma janela
janela = tk.Tk()


#Cria um Label - Produto
label = tk.Label(janela, text = "produto")
label.pack()

#Criar uma area para inserir texto
entrada_txt = tk.Entry(janela, width= 50)
entrada_txt.pack()

#Button: Botão:
botao = tk.Button(janela, text ="Pesquisa", command= entrar_navegador)
botao.pack()
# Função para o botão "Enter" executar o programa
def on_enter_press(event):
    if event.keysym == "Return":
        entrar_navegador()
janela.bind("<KeyPress>", on_enter_press)

#Button: Botão:
botao = tk.Button(janela, text ="Gráfico", command= caminho_arquivo)
botao.pack()


janela.mainloop()