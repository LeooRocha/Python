import pandas as pd
import matplotlib.pyplot as plt

# Lita de vendedores

ranking_vendas = {
    "Vendedor": ["João", "Marcelo", "Paula", "Paula", "Thais"],
    "Valor_Vendido":[10000.00,5000.00,7800.00,5800.00,6000.00],
    "Conversao_Vendas":[2000,4000,7000,9000,1000]
}

# Criar seu Dataframe
df = pd.DataFrame(ranking_vendas)

print (df)

media_vendas = df['Valor_Vendido'].mean()
media_conversao = df['Conversao_Vendas'].mean()
maximo_vendas = df['Valor_Vendido'].max()
minimo_vendas = df['Valor_Vendido'].min()

print(f"Média de vendas: {media_vendas}")
print(f"Média da conversão: {media_conversao}")
print(f"Maior valor vendido: {maximo_vendas}")
print(f"Menor valor vendido: {minimo_vendas}")

df.plot(x = 'Vendedor', y =['Valor_Vendido', 'Conversao_Vendas'], kind='bar')

plt.title("Ranking de Vendas")

plt.xlabel("Vendedores")
plt.ylabel("Venda")
plt.show()

