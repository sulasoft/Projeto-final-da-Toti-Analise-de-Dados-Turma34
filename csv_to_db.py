import sqlite3
import pandas as pd

def main():

	# Conectar ao banco de dados SQLite
    conn = sqlite3.connect('moda_estilos.db')
    cursor = conn.cursor()

    # Ler o CSV
    df = pd.read_csv('shopping_trends_clean.csv', delimiter=',')

    # Adicionar dados à tabela clientes
    df_clientes = df[['Idade', 'Gênero', 'Localização', 'Status de Assinatura', 'Compras Anteriores', 'Método de Pagamento', 'Frequência de Compras']]
    df_clientes.columns = ['idade', 'genero', 'localizacao', 'status_da_assinatura', 'compras_anteriores', 'metodo_de_pagamento', 'frequencia_de_compras']
    df_clientes.to_sql('clientes', conn, if_exists='append', index=False)

    # Adicionar dados à tabela items e eliminar duplicados
    df_items = df[['Item Comprado', 'Categoria', 'Valor da Compra (R$)', 'Tamanho', 'Cor', 'Estação']]
    df_items.columns = ['item', 'categoria', 'valor', 'tamanho', 'cor', 'temporada']
    df_items.drop_duplicates(subset=['item'], inplace=True)

    # Verificar se há valores nulos na coluna 'Item Comprado'
    if df['Item Comprado'].isnull().any():
        raise ValueError("A coluna 'Item Comprado' não pode conter valores nulos.")

    # Verificar se há valores em 'Item Comprado' que não existem em df_items depois de eliminar duplicados
    nao_df_items = set(df['Item Comprado']) - set(df_items['item'])
    if nao_df_items:
        raise ValueError(f"Os seguintes elementos não existem na tabela 'items': {nao_df_items}")

    df_items.to_sql('items', conn, if_exists='append', index=False)

    df_items['id_item'] = range(1, len(df_items) + 1)

    # Adicionar dados à tabela compras
    df_compras = df[['Valor da Compra (R$)', 'Avaliação', 'Tipo de Envio', 'Desconto Aplicado', 'Código Promocional Utilizado', 'ID do Cliente']]
    df_compras.columns = ['valor_da_compra', 'avaliacao', 'tipo_de_envio', 'desconto_aplicado', 'codigo_promocional_usado', 'id_clientes']

    # Mapear os IDs de items correspondentes a cada linha em df_compras
    df_compras['id_items'] = df['Item Comprado'].map(df_items.set_index('item')['id_item'])

    # Adicionar dados à tabela compras no banco de dados
    df_compras.to_sql('compras', conn, if_exists='append', index=False)

    # Fechar a conexão
    conn.close()