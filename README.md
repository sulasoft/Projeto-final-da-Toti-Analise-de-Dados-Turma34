<h1 align="center">Conjunto de Dados de Preferências de Compras do Cliente 🛍️</h1>

<p align="justify">
  Este conjunto de dados, parte do projeto final do curso de Análise de Dados ministrado por Toti, oferece uma visão aprofundada do comportamento e padrões de compra dos consumidores. É essencial para as empresas adaptarem produtos, estratégias de marketing e melhorarem a experiência do cliente. Com 3900 registros, abrange informações-chave como idade, gênero, histórico de compras, métodos de pagamento preferidos, frequência de compras e mais. Ideal para iniciantes em Análise de Dados, este conjunto sintético fornece uma base sólida para a tomada de decisões baseada em dados e estratégias centradas no cliente.
</p>

<p align="center">
<img src="https://i.ibb.co/fQRGKG7/powebi-design1.jpg" alt="Power BI Design 1" width = "600">

<img width = "600" src="https://scontent.fcaw6-1.fna.fbcdn.net/v/t39.30808-6/409567995_7197695866960168_8266774480308376513_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeHztXl9KUyuU2Q5EyD8IGCOCGONogHrsKcIY42iAeuwp-Hw1hmMbfW5EYc3_UkZ_-F03CIt0IMe3ox7MOKr8Z3d&_nc_ohc=h0bUP1lzsrkAX-M2lNJ&_nc_ht=scontent.fcaw6-1.fna&oh=00_AfBNMpW1OQJcDKxsAXA-RlFt7VC25XdU-N2qmLzzqpxRXQ&oe=657B3F91">
</p>

<h2>Como Utilizar</h2>
<p>Certifique-se de ter o Python > 3.9 e todas as dependências instaladas antes de executar os scripts. Você pode instalá-las usando:</p>

<pre>
<code>pip install -r requirements.txt</code>
</pre>

<p>O script principal <code>main.py</code> coordena várias tarefas essenciais para o projeto. Abaixo estão detalhados os passos do processo:</p>

<ol>
  <li><strong>Limpeza de Dados:</strong> Execute o script <code>clean_data.py</code> para limpar os dados do CSV original.</li>
  <li><strong>Criação do Banco de Dados:</strong> Utilize o script <code>criar_db.py</code> para criar o banco de dados (<code>moda_estilos.db</code>).</li>
  <li><strong>Inserção de Dados:</strong> O script <code>csv_to_db.py</code> executa a inserção de dados do CSV no banco de dados.</li>
</ol>

<p>Para executar o script principal, utilize o seguinte comando:</p>

<pre>
<code>python main.py</code>
</pre>

<h2>Script clean_data.py</h2>

<p>O script <code>clean_data.py</code> realiza várias operações para limpar e enriquecer o conjunto de dados original:</p>

<ol>
  <li><strong>Ler o CSV Original:</strong> Utiliza o <code>pandas</code> para ler o arquivo CSV original (<code>shopping_trends_updated.csv</code>) e carregar os dados em um DataFrame.</li>

  <li><strong>Criar a Coluna 'Localização':</strong> Adiciona uma nova coluna chamada 'Localização', atribuindo cidades brasileiras aleatórias a cada linha.</li>

  <li><strong>Adição das Colunas 'Item Comprado' e 'Categoria':</strong> Gera aleatoriamente produtos para a coluna 'Item Comprado' e atribui categorias a esses produtos.</li>

  <li><strong>Mapeamento de Categorias:</strong> Define um mapeamento de categorias para atribuir categorias aos itens comprados.</li>

  <li><strong>Função para Atribuir Categorias:</strong> Define uma função que atribui categorias conforme o mapeamento definido.</li>

  <li><strong>Aplicação da Função para Atribuir Categorias:</strong> Aplica a função para atribuir categorias aos itens comprados e cria a coluna 'Categoria'.</li>

  <li><strong>Lista de Métodos de Pagamento e Adição da Coluna 'Método de Pagamento':</strong> Adiciona uma coluna 'Método de Pagamento' com métodos de pagamento brasileiros aleatórios a cada linha.</li>

  <li><strong>Salvamento do DataFrame em um Novo Arquivo CSV:</strong> Salva o DataFrame atualizado em um novo arquivo CSV (<code>shopping_trends_clean.csv</code>).</li>
</ol>

<p>Este script enriquece o conjunto de dados original com informações adicionais, como localização, item comprado, categoria e método de pagamento, antes de salvar em um novo arquivo CSV.</p>

<h2>Script criar_db.py</h2>

<p>O script <code>criar_db.py</code> cria e configura um banco de dados SQLite:</p>

<ol>
  <li><strong>Conectar ao Banco de Dados SQLite:</strong> O script se conecta ao banco de dados SQLite (criará um novo arquivo se não existir).</li>

  <li><strong>Criar Tabela 'clientes':</strong> Cria uma tabela chamada 'clientes' com informações sobre os clientes, como idade, gênero, localização, status da assinatura, compras anteriores, método de pagamento e frequência de compras.</li>

  <li><strong>Criar Tabela 'items':</strong> Cria uma tabela chamada 'items' que armazena informações sobre os itens disponíveis para compra, como nome do item, categoria, valor, tamanho, cor e temporada.</li>

  <li><strong>Criar Tabela 'compras':</strong> Cria uma tabela chamada 'compras' que registra informações sobre cada compra, incluindo valor da compra, avaliação, tipo de envio, desconto aplicado, código promocional usado, e referências às tabelas 'clientes' e 'items'.</li>

  <li><strong>Fechar a Conexão:</strong> Finaliza a conexão com o banco de dados SQLite.</li>
</ol>

<p>Este script é fundamental para a estruturação do banco de dados usado no projeto, definindo as tabelas e suas relações.</p>

<h2>Script csv_to_db.py</h2>

<p>O script <code>csv_to_db.py</code> adiciona dados do arquivo CSV ao banco de dados SQLite:</p>

<ol>
  <li><strong>Conectar ao Banco de Dados SQLite:</strong> O script se conecta ao banco de dados SQLite (<code>moda_estilos.db</code>).</li>

  <li><strong>Ler o CSV:</strong> Utiliza o <code>pandas</code> para ler o arquivo CSV limpo (<code>shopping_trends_clean.csv</code>).</li>

  <li><strong>Adicionar Dados à Tabela 'clientes':</strong> Seleciona as colunas relevantes do DataFrame e adiciona os dados à tabela 'clientes' no banco de dados.</li>

  <li><strong>Adicionar Dados à Tabela 'items' e Eliminar Duplicados:</strong> Seleciona as colunas relevantes do DataFrame e adiciona os dados à tabela 'items', eliminando duplicatas com base no nome do item.</li>

  <li><strong>Verificar Valores Nulos e Inexistentes na Coluna 'Item Comprado':</strong> Verifica se há valores nulos na coluna 'Item Comprado' e se todos os itens existem na tabela 'items'.</li>

  <li><strong>Adicionar Dados à Tabela 'compras':</strong> Seleciona as colunas relevantes do DataFrame e adiciona os dados à tabela 'compras', mapeando os IDs correspondentes dos itens.</li>

  <li><strong>Fechar a Conexão:</strong> Finaliza a conexão com o banco de dados SQLite.</li>
</ol>

<p>Este script é responsável por transferir os dados do arquivo CSV para o banco de dados SQLite, garantindo a integridade e consistência dos dados.</p>

<h2>Importação no Power BI</h2>

<p>Com os dados do CSV já inseridos no banco de dados SQLite, você pode prosseguir com a importação desses dados no Power BI. Aqui estão os passos para realizar a importação utilizando a conexão via SQLite e ODBC:</p>

<h3>Conexão via SQLite:</h3>

<ol>
  <li><strong>Baixe e Instale o Driver SQLite:</strong> Certifique-se de ter o driver SQLite instalado no seu sistema.</li>
  
  <li><strong>Abra o Power BI:</strong> Inicie o Power BI Desktop.</li>
  
  <li><strong>Escolha 'Obter Dados':</strong> Na guia "Página Inicial", escolha a opção "Obter Dados" e selecione "Outros" para ver mais opções.</li>
  
  <li><strong>Escolha 'ODBC':</strong> Selecione "ODBC" e escolha o driver ODBC para SQLite.</li>
  
  <li><strong>Configure a Conexão:</strong> Insira as informações necessárias, como o nome do arquivo do banco de dados SQLite e as credenciais, se aplicável.</li>
  
  <li><strong>Selecione Tabelas:</strong> Selecione as tabelas desejadas (clientes, items, compras) para importar no Power BI.</li>
</ol>

<h3>Conexão via ODBC:</h3>

<ol>
  <li><strong>Configure uma Fonte de Dados ODBC (ProjetoBI):</strong> Certifique-se de ter uma fonte de dados ODBC configurada com o nome "ProjetoBI" para o seu banco de dados SQLite.</li>
  
  <li><strong>Abra o Power BI:</strong> Inicie o Power BI Desktop.</li>
  
  <li><strong>Escolha 'Obter Dados':</strong> Na guia "Página Inicial", escolha a opção "Obter Dados" e selecione "Outros" para ver mais opções.</li>
  
  <li><strong>Escolha 'ODBC':</strong> Selecione "ODBC" e escolha a fonte de dados ODBC configurada. (ProjetoBI)</li>
  
  <li><strong>Selecione Tabelas:</strong> Selecione as tabelas desejadas (clientes, items, compras) para importar no Power BI.</li>
</ol>

<p>Após a configuração da conexão, você poderá explorar e visualizar os dados do seu banco de dados SQLite diretamente no Power BI, permitindo a criação de relatórios e dashboards interativos.</p>


<h2> 🌟 Informações Adicionais</h2>

<p>Os dados utilizados neste projeto foram obtidos do Kaggle. Você pode encontrar o conjunto de dados em <a href="https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset" target="_blank">Customer Shopping Trends Dataset</a>.</p>

<p>Este projeto foi desenvolvido como parte do curso de Análise de Dados ministrado por Toti. 

<h2>Contribuidores ✨</h2>


<a href="https://github.com/sulasoft">
  David Sulbarán
</a>
<br>
<a href="https://github.com/samilmoret">
  Samil Moret
</a>
