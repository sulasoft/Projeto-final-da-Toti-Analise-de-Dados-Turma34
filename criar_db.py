import sqlite3

def main():
  # Conectar ao banco de dados SQLite (irá criar um novo arquivo se não existir)
  conn = sqlite3.connect('moda_estilos.db')
  cursor = conn.cursor()

  # Criar tabela clientes
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idade INTEGER NOT NULL,
    genero TEXT NOT NULL,
    localizacao TEXT NOT NULL,
    status_da_assinatura TEXT NOT NULL,
    compras_anteriores INTEGER NOT NULL,
    metodo_de_pagamento TEXT NOT NULL,
    frequencia_de_compras TEXT NOT NULL);
  ''')

  # Criar tabela items
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    categoria TEXT NOT NULL,
    valor REAL NOT NULL,
    tamanho TEXT NOT NULL,
    cor TEXT NOT NULL,
    temporada TEXT NOT NULL);
  ''')

  # Criar tabela compras
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_da_compra REAL NOT NULL,
    avaliacao REAL NOT NULL,
    tipo_de_envio TEXT NOT NULL,
    desconto_aplicado TEXT NOT NULL,
    codigo_promocional_usado TEXT NOT NULL,
    id_items INTEGER NOT NULL,
    id_clientes INTEGER NOT NULL,
    FOREIGN KEY (id_clientes) REFERENCES clientes (id),
    FOREIGN KEY (id_items) REFERENCES items (id));
  ''')

  # Fechar a conexão
  conn.close()