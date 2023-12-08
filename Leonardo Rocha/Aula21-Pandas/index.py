import pandas as pd
import matplotlib.pyplot as plt

# Criacação de um Dataframe

#  Passo 1: Dados Fictícios
dados_alunos = {
    'Nome': ['João','Maria', 'Carlos', 'Ana'],
    'Idade' : [18,20,19,22], 
    'Nota_Matemática': [78,80,75,85],
    'Nota_Portugues': [88,70,65,95]
}

# Passo 2: Criar o Dataframe
df_alunos = pd.DataFrame(dados_alunos)

# Passo 3: Exibir o Dataframe
print(df_alunos)

# Análise de Dados:

# Média das notas de Matemática
media_matematica = df_alunos['Nota_Matemática'].mean()

# Média das notas de Português
media_portugues = df_alunos['Nota_Portugues'].mean()

# Imprimir a média
print(f'Média em Matemática: {media_matematica}')
print(f'Média de Português: {media_portugues}')

######################

# Visualização de Dados:

# Gráfico de Barra das notas de Matemática

df_alunos.plot(x = 'Nome', y =['Nota_Matemática', 'Nota_Portugues'], kind='line')

plt.title("Notas dos Alunos em Matemática e Português")

plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.show()