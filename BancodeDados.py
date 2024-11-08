import sqlite3

# Criando um banco de dado pelo SQL
conexao = sqlite3.connect('dados_vendas.db')

cursor = conexao.cursor()

# Criando uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Inserindo os dados para tabela

cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

conexao.commit()

import pandas as pd

# Carregando os dados do pandas
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Explorando os dados
print(df_vendas.head())
print(df_vendas.describe())
print(df_vendas.info())

# Vendas por categoria
total_vendas_categoria = df_vendas.groupby('categoria')['valor_venda'].sum()
print(total_vendas_categoria)

# Vendas por produtos
media_vendas_produto = df_vendas.groupby('produto')['valor_venda'].mean()
print(media_vendas_produto)

import matplotlib.pyplot as plt

import seaborn as sns

# Criando grafico do total de venda por categoria
plt.figure(figsize=(10,6))
sns.barplot(x=total_vendas_categoria.index, y=total_vendas_categoria.values)
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.show()

# Criando grafico por media de venda dos produtos
plt.figure(figsize=(10,6))
sns.barplot(x=media_vendas_produto.index, y=media_vendas_produto.values)
plt.title('Média de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Média de Vendas')
plt.xticks(rotation=45)
plt.show()
