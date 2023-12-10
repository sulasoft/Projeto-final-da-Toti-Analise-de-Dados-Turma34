import pandas as pd
import random

def main():
    # Ler o CSV
    df = pd.read_csv('shopping_trends_updated.csv')

    # Criar lista com cidades do Brasil
    cidades_brasil = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília', 'Fortaleza', 'Recife', 'Manaus', 'Curitiba', 'Porto Alegre', 'Belém', 'Goiânia', 'Cuiabá', 'Florianópolis', 'Natal', 'Teresina', 'Campo Grande', 'João Pessoa', 'Aracaju', 'Palmas']

    df['Localização'] = [random.choice(cidades_brasil) for _ in range(len(df))]

    # Adicionar itens comprados e categorias
    produtos = [
        "Blusa", "Suéter", "Sandálias", "Tênis", "Camisa", "Shorts", 
        "Casaco", "Bolsa", "Sapatos", "Vestido", "Saia", "Óculos de Sol", 
        "Calças", "Jaqueta", "Moletom", "Joias", "Cachecol", "Chapéu", 
        "Meias", "Mochila", "Cinto", "Luvas", "Botas"
    ]

    # Adicionar as colunas "Item Comprado" e "Categoria" ao DataFrame existente
    df['Item Comprado'] = [random.choice(produtos) for _ in range(len(df))]

    # Mapeo de categorias
    mapeo_categorias = {
        "Roupas": ["Blusa", "Suéter", "Calças", "Jeans", "Camisa", "Jaqueta", "Shorts", "Casaco", "Vestido", "Saia", "Camiseta", "Moletom", "Luvas"],
        "Calçados": ["Sandálias", "Tênis", "Sapatos", "Botas"],
        "Agasalhos": ["Casaco", "Moletom"],
        "Acessórios": ["Bolsa", "Óculos de Sol", "Joias", "Cachecol", "Chapéu", "Meias", "Cinto", "Mochila"]
    }

    def asignar_categoria(item_comprado):
        posibles_categorias = [key for key, value in mapeo_categorias.items() if item_comprado in value]
        return posibles_categorias[0] if posibles_categorias else None

    df['Categoria'] = df['Item Comprado'].apply(asignar_categoria)


    # Lista de métodos de pagamento no Brasil
    metodos_pagamento_brasil = [
        "Pix",
        "Boleto Bancário",
        "Transferência Bancária",
        "Cartão de Crédito",
        "Cartão de Débito",
        "Dinheiro"
    ]

    # Criar uma lista de métodos de pagamento para a coluna "Pagamento"
    lista_pagamento = [random.choice(metodos_pagamento_brasil) for _ in range(len(df))]

    # Atribuir a nova lista à coluna "Pagamento" no seu DataFrame
    df['Método de Pagamento'] = lista_pagamento


    # Salvar o DataFrame atualizado em um novo arquivo CSV
    df.to_csv('shopping_trends_clean.csv', index=False)