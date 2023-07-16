# Importando as bibliotecas que usaremos
import pandas as pd
import matplotlib.pyplot as plt

print("======================= Trazendo os títulos das colunas====================================")
# Trazendo o banco de dados utilizando a bibliotecas
Dataframe = pd.read_csv('supermarket_sales - Sheet1.csv')

# Adicionando os títulos das colunas à uma lista
Titulos = [x for x in Dataframe.columns]
print(Titulos)

print("_______________________________________________________________________________________")
print("======================= Valor por Linha de Produto ====================================")
# Limpando os dados indesejados
Dados_Indesejados=['Invoice ID','Branch','Time','cogs']
for i in Dados_Indesejados:
    Dataframe= Dataframe.drop(i,axis=1)

# Transformando a data em Mês e Ano
#  (1) Convertendo a coluna de Data para datetime
Dataframe['Date'] =pd.to_datetime(Dataframe["Date"])

#  (2) Extraindo o mês e o ano a partir da coluna transformada
Dataframe['Mes'] = Dataframe['Date'].dt.month
Dataframe['Ano'] = Dataframe['Date'].dt.year

# Pegando as linhas de produtos
Linhas_Produtos = []
for linha in Dataframe['Product line'].unique():
    Linhas_Produtos.append(linha)
print(Linhas_Produtos)

print("_______________________________________________________________________________________")
print("======================= Valor por Linha de Produto ====================================")
# Trazendo os valores de arrecadação por linha de produto

"""
-> Conseguimos trazer de uma forma mais direta
Total = Dataframe.groupby('Product line')['Total'].sum()
print(Total)
"""

Total_Linha = {}

Grupos_Produtos = Dataframe.groupby('Product line')
for i, valores in Grupos_Produtos:
    Total = valores['Total'].sum()                      #Valores atua como um subconjunto do grupo i
    Total_Linha[i] = round(Total,2)
print(Total_Linha)

# Trazendo um gráfico com a participação de cada grupo no total de vendas
Porcentagem = {}
Total_vendas = Dataframe['Total'].sum()
for Linha, tots in Total_Linha.items():
    Valor = (tots/Total_vendas)*100
    Porcentagem[Linha] = round(Valor,2)

# Criando o gráfico de pizza
plt.pie(Porcentagem.values(), labels=Porcentagem.keys(), autopct='%1.1f%%')

# Configurações adicionais
plt.title('Distribuição de vendas por Linha')
plt.axis('equal')

# Exibindo o gráfico
plt.show()

print("__________________________________________________________________________________________")
print("================================= Valor por Genero =======================================")

# Trazendo os valores de arrecadação por Gênero
Total_Genero ={}
Grupo_Genero = Dataframe.groupby('Gender')

for i, valor in Grupo_Genero:
    Total = valor['Total'].sum()
    Total_Genero[i] = Total
print(Total_Genero)

# Trazendo o valor em porcetagem
Porcentagem_Genero = {}
for Genero, total in Total_Genero.items():
    Valor = (total/Total_vendas)*100
    Porcentagem_Genero[Genero] = round(Valor, 2)

print(Porcentagem_Genero)
# Criando o gráfico de pizza
plt.pie(Porcentagem_Genero.values(), labels=Porcentagem_Genero.keys(), autopct='%1.1f%%')

# Configurações adicionais
plt.title('Distribuição de Vendas por Genero')

# Exibindo o gráfico
plt.show()

print("__________________________________________________________________________________________")
print("================================= Valor por Cidade =======================================")

# Trazendo os valores por cidade
Grupo_Cidade = Dataframe.groupby('City')
Cidades = {}

for i,x in Grupo_Cidade:
    Total = x['Total'].sum()
    Cidades[i] = Total

# Criando o gráfico de barra
plt.bar(Cidades.keys(),Cidades.values())
plt.ylim(100000, 115000)

# Configurações adicionais
plt.title('Distribuição de Vendas por Cidade')

# Exibindo o gráfico
plt.show()

