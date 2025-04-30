import requests
import json
import pandas as pd
from datetime import datetime

# Função para coletar dados de uma API climática (exemplo com OpenWeatherMap)
def coletar_dados_climaticos(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
    resposta = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Extraindo informações relevantes do JSON
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        pressao = dados['main']['pressure']
        descricao = dados['weather'][0]['description']
        data_hora = datetime.now()
        
        # Organizando os dados em um dicionário
        dados_climaticos = {
            "cidade": cidade,
            "temperatura": temperatura,
            "umidade": umidade,
            "pressao": pressao,
            "descricao": descricao,
            "data_hora": data_hora
        }
        
        return dados_climaticos
    else:
        print("Erro na coleta de dados:", resposta.status_code)
        return None

# Função para salvar os dados em um arquivo CSV
def salvar_dados_csv(dados_climaticos):
    if dados_climaticos:
        # Convertendo os dados para DataFrame
        df = pd.DataFrame([dados_climaticos])
        
        # Salvando os dados no CSV (simulando a coleta)
        df.to_csv("dados_climaticos_coletados.csv", index=False)
        print("Dados climáticos salvos com sucesso!")
    else:
        print("Nenhum dado para salvar.")

# Exemplo de coleta e salvamento de dados
cidade = "Rio de Janeiro"
chave_api = "sua_chave_api_aqui"  # Substitua pela chave da API do OpenWeatherMap

dados = coletar_dados_climaticos(cidade, chave_api)
salvar_dados_csv(dados)
