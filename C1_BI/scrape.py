import pandas as pd

# faz a requisição GET no site e armazena o conteúdo HTML
import requests
from bs4 import BeautifulSoup


# URL do site
url = 'https://coronavirus.es.gov.br/painel-covid-19-es'

# Fazer a requisição para o site
response = requests.get(url)

# Criar objeto BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar o link para o arquivo CSV
link = soup.find('a', href='https://bi.s3.es.gov.br/covid19/MICRODADOS.csv')

# Baixar o arquivo CSV
file_url = link['href']
response = requests.get(file_url)
with open('MICRODADOS.csv', 'wb') as f:
    f.write(response.content)