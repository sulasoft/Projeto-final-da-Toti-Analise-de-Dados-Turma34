import pandas as pd
import matplotlib.pyplot as plt
from criar_db import main as criarDB
from csv_to_db import main as csvSql
from clean_data import main as cleanData
from time import sleep

try:

	print('Iniciando...')

	# Para limpar dados do csv original
	cleanData()
	
	# Para criar o banco de dados
	criarDB()

	print('Banco de dados criado.')

	# Esperamos 1 segundo para continuar
	sleep(1)

	# Do documento CSV, inserimos os dados no Banco de Dados SQL
	csvSql()
	print('Dados do CSV inseridos no Banco de Dados: moda_estilos.db')

	print('Fim.')

except Exception as e:
	print('Erro: ', str(e))