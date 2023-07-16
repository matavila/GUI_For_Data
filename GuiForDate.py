import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def Gerar_Grafico_Cidade():
    # Trazendo os valores por cidade
    Grupo_Cidade = Dataframe.groupby('City')
    Cidades = {}

    for i, x in Grupo_Cidade:
        Total = x['Total'].sum()
        Cidades[i] = Total

    # Criando o gráfico de barra
    plt.bar(Cidades.keys(), Cidades.values())
    plt.ylim(100000, 115000)

    # Configurações adicionais
    plt.title('Distribuição de Vendas por Cidade')

    # Exibindo o gráfico
    plt.show()


def Gerar_Grafico_Produto():

    Total_Linha = {}

    Grupos_Produtos = Dataframe.groupby('Product line')
    for i, valores in Grupos_Produtos:
        Total = valores['Total'].sum()  # Valores atua como um subconjunto do grupo i
        Total_Linha[i] = round(Total, 2)
    print(Total_Linha)

    # Trazendo um gráfico com a participação de cada grupo no total de vendas
    Porcentagem = {}
    Total_vendas = Dataframe['Total'].sum()
    for Linha, tots in Total_Linha.items():
        Valor = (tots / Total_vendas) * 100
        Porcentagem[Linha] = round(Valor, 2)

    # Criando o gráfico de pizza
    plt.pie(Porcentagem.values(), labels=Porcentagem.keys(), autopct='%1.1f%%')

    # Configurações adicionais
    plt.title('Distribuição de vendas por Linha', pad=30)

    plt.axis('equal')

    # Exibindo o gráfico
    plt.show()


def Calcular_Dados_Cidade():

    # Trazendo os valores por cidade
    Grupo_Cidade = Dataframe.groupby('City')
    Cidades = {}

    # Pegando o total de vendas por cidade e adicionado ao dicionário
    for i, x in Grupo_Cidade:
        Total = x['Total'].sum()
        Cidades[i] = Total

    # Adicionar os dados do DataFrame ao Treeview
    for i, valor in Cidades.items():
        tree_Cidades.insert('', 'end', values=(i,round(valor, 2)))

    tree_Cidades['columns'] = ('Cidades', 'Total')

    # Formatar as colunas
    tree_Cidades.column('#0', width=0, stretch=tk.NO)  # Coluna vazia
    tree_Cidades.column('Cidades', width=80)
    tree_Cidades.column('Total', width=80)

    # Definir os cabeçalhos das colunas
    tree_Cidades.heading('#0', text='')
    tree_Cidades.heading('Cidades', text='Cidades')
    tree_Cidades.heading('Total', text='Total')

    # Exibir a tabela
    tree_Cidades.grid(column=1, row=4, padx=(10, 2), pady=(10, 0))


def Calcular_Dados_Genero():

    # Trazendo os valores de arrecadação por Gênero
    Total_Genero = {}
    Grupo_Genero = Dataframe.groupby('Gender')

    for i, valor in Grupo_Genero:
        Total = valor['Total'].sum()
        Total_Genero[i] = Total

    # Adicionar os dados do DataFrame ao Treeview
    for i, valor in Total_Genero.items():
        tree_Genero.insert('', 'end', values=(i,round(valor, 2)))

    tree_Genero['columns'] = ('Gênero', 'Total')

    # Formatar as colunas
    tree_Genero.column('#0', width=0, stretch=tk.NO)  # Coluna vazia
    tree_Genero.column('Gênero', width=80)
    tree_Genero.column('Total', width=80)

    # Definir os cabeçalhos das colunas
    tree_Genero.heading('#0', text='')
    tree_Genero.heading('Gênero', text='Gênero')
    tree_Genero.heading('Total', text='Total')

    # Exibir a tabela
    tree_Genero.grid(column=2, row=4, padx=(10, 2), pady=(10, 0))


def Calcular_Dados_Pagameto():

    # Trazendo os valores de arrecadação por Gênero
    Total_Pagamento = {}
    Grupo_Pagamento = Dataframe.groupby('Payment')

    for i, valor in Grupo_Pagamento:
        Total = valor['Total'].sum()
        Total_Pagamento[i] = Total

    # Adicionar os dados do DataFrame ao Treeview
    for i, valor in Total_Pagamento.items():
        tree_Pagamento.insert('', 'end', values=(i, round(valor, 2)))

    tree_Pagamento['columns'] = ('Pagamento', 'Total')

    # Formatar as colunas
    tree_Pagamento.column('#0', width=0, stretch=tk.NO)  # Coluna vazia
    tree_Pagamento.column('Pagamento', width=80)
    tree_Pagamento.column('Total', width=80)

    # Definir os cabeçalhos das colunas
    tree_Pagamento.heading('#0', text='')
    tree_Pagamento.heading('Pagamento', text='Pagamento')
    tree_Pagamento.heading('Total', text='Total')

    # Exibir a tabela
    tree_Pagamento.grid(column=3, row=4, padx=(10, 2), pady=(10, 0))


def Calcular_Dados_Produto():

    # Trazendo os valores de arrecadação por Gênero
    Total_Pagamento = {}
    Grupos_Produtos = Dataframe.groupby('Product line')

    for i, valores in Grupos_Produtos:
        Total = valores['Total'].sum()      # Valores atua como um subconjunto do grupo i
        Total_Pagamento[i] = round(Total, 2)

    # Adicionar os dados do DataFrame ao Treeview
    for i, valor in Total_Pagamento.items():
        tree_Produto.insert('', 'end', values=(i, round(valor, 2)))

    tree_Produto['columns'] = ('Produto', 'Total')

    # Formatar as colunas
    tree_Produto.column('#0', width=0, stretch=tk.NO)  # Coluna vazia
    tree_Produto.column('Produto', width=140)
    tree_Produto.column('Total', width=80)

    # Definir os cabeçalhos das colunas
    tree_Produto.heading('#0', text='')
    tree_Produto.heading('Produto', text='Produto')
    tree_Produto.heading('Total', text='Total')

    # Exibir a tabela
    tree_Produto.grid(column=4, row=4, padx=(26, 2), pady=(10, 0), columnspan=2, sticky="W")


def Gera_Colunas(Df):
    # Obter as colunas do DataFrame
    colunas = Df.columns.tolist()

    # Removendo a primeira coluna do Tkinter
    tree.column('#0', width=0, stretch=tk.NO)

    # Definir as colunas no Treeview
    tree['columns'] = colunas

    # Configurar as colunas no Treeview
    for coluna in colunas:
        tree.column(coluna, width=95)
        tree.heading(coluna, text=coluna)

    # Exibir a tabela
    tree.grid(column=1, row=2, columnspan=6, padx=(25, 40), pady=(10, 0))


def carregar_dados():

    # Definindo o DataFrame como variável global
    global Dataframe

    # Abrir a janela de diálogo para seleção de arquivo
    arquivo = filedialog.askopenfilename()

    # Limpar a tabela existente
    limpar_tabela()

    # Trazendo o banco de dados utilizando a bibliotecas
    Dataframe = pd.read_csv(arquivo)

    # Limpando os dados indesejados
    Dados_Indesejados = ['Invoice ID', 'Branch', 'Time', 'cogs', 'Rating', 'gross income', 'gross margin percentage']
    for i in Dados_Indesejados:
        Dataframe = Dataframe.drop(i, axis=1)

    Gera_Colunas(Dataframe)

    # Adicionar os dados do DataFrame ao Treeview
    for i, linha in Dataframe.iterrows():
        tree.insert('', 'end', values=linha.tolist())

    # Adicionando um label antes da Tabela
    Texto_Entada = Label(root, text="Tabela de Dados:")
    Texto_Entada.grid(column=1, row=1, columnspan=6, padx=(0, 870), pady=(10, 0))

    # Exibir a tabela
    tree.grid(column=1, row=2, columnspan=6, padx=(25, 40), pady=(10, 0))

    botao_upload = tkinter.Button(root, text="Vendas por Cidade", command=Calcular_Dados_Cidade)
    botao_upload.grid(column=1, row=3, padx=(20,0), pady=10, sticky="W")

    botao_upload = tkinter.Button(root, text="Vendas por Gênero", command=Calcular_Dados_Genero)
    botao_upload.grid(column=2, row=3, pady=10,)

    botao_upload = tkinter.Button(root, text="Vendas por Pagamento", command=Calcular_Dados_Pagameto)
    botao_upload.grid(column=3, row=3, pady=10,)

    botao_upload = tkinter.Button(root, text="Vendas por Produto", command=Calcular_Dados_Produto)
    botao_upload.grid(column=4, row=3, pady=10, )


def limpar_tabela():
    # Remover todas as linhas da tabela
    for item in tree.get_children():
        tree.delete(item)

    # Removendo todas as colunas do Treeview
    for coluna in tree['columns']:
        tree.heading(coluna, text="")
        tree.column(coluna, width=0)
    tree['columns'] = []


# Configuração inicial da janela principal
root = tk.Tk()

# Definindo o tamanho da tela
root.geometry('1000x500')

# Criar um objeto Menu
menu = tk.Menu(root)

# Criar o Treeview (tabela de dados)
tree = ttk.Treeview(root)
tree_Cidades = ttk.Treeview(root)
tree_Genero = ttk.Treeview(root)
tree_Pagamento = ttk.Treeview(root)
tree_Produto = ttk.Treeview(root)

# Configurar largura e altura da Treeview
tree_Cidades.configure(height=5)
tree_Genero.configure(height=5)
tree_Pagamento.configure(height=5)
tree_Produto.configure(height=5)

# Criar um submenu
submenu = tk.Menu(menu, tearoff=0)
submenu_grafico = tk.Menu(menu, tearoff=0)

submenu.add_command(label="Carregar Dados", command=carregar_dados)
submenu_grafico.add_command(label="Participação de Produtos", command=Gerar_Grafico_Produto)
submenu_grafico.add_command(label="Vendas por Cidade", command=Gerar_Grafico_Cidade)

# Adicionar o submenu ao menu principal
menu.add_cascade(label="Arquivo", menu=submenu)
menu.add_cascade(label="Análise Gráfica", menu=submenu_grafico)

# Configurar o menu como o menu da janela principal
root.config(menu=menu)


# Definir o número de colunas e o tamanho de cada uma
root.grid_columnconfigure(1, weight=1, minsize=200)
root.grid_columnconfigure(2, weight=1, minsize=200)
root.grid_columnconfigure(3, weight=1, minsize=200)
root.grid_columnconfigure(4, weight=1, minsize=200)
root.grid_columnconfigure(5, weight=1, minsize=200)


# Execução da interface gráfica
root.mainloop()





