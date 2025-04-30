# Importando bibliotecas necessárias
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Função para carregar dados climáticos (exemplo com CSV)
def carregar_dados(caminho_arquivo):
    """
    Carrega dados climáticos a partir de um arquivo CSV.
    :param caminho_arquivo: Caminho do arquivo CSV com os dados climáticos.
    :return: DataFrame com os dados climáticos.
    """
    dados = pd.read_csv(caminho_arquivo, parse_dates=True, index_col='Data')
    return dados

# Função para treinar o modelo ARIMA
def treinar_modelo_arima(dados, ordem=(5, 1, 0)):
    """
    Treina o modelo ARIMA com os dados fornecidos.
    :param dados: Dados históricos (série temporal).
    :param ordem: Parâmetros do modelo ARIMA (p, d, q).
    :return: Modelo ARIMA treinado.
    """
    modelo = ARIMA(dados, order=ordem)
    modelo_ajustado = modelo.fit()
    return modelo_ajustado

# Função para fazer previsões usando o modelo ARIMA
def prever_temperatura(modelo_ajustado, passos_futuro=10):
    """
    Faz previsões de temperatura para os próximos passos de tempo.
    :param modelo_ajustado: Modelo ARIMA treinado.
    :param passos_futuro: Número de passos (dias, meses, etc.) para o qual se deseja prever.
    :return: Previsões para o futuro.
    """
    previsoes = modelo_ajustado.forecast(steps=passos_futuro)
    return previsoes

# Função para visualizar os resultados
def plotar_previsao(dados, previsoes):
    """
    Plota os dados originais e as previsões feitas pelo modelo ARIMA.
    :param dados: Dados climáticos históricos.
    :param previsoes: Previsões futuras geradas pelo modelo.
    """
    plt.figure(figsize=(10,6))
    plt.plot(dados, label='Dados Reais', color='blue')
    plt.plot(range(len(dados), len(dados) + len(previsoes)), previsoes, label='Previsões', color='red')
    plt.title('Previsões Climáticas com ARIMA')
    plt.xlabel('Tempo')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.show()

# Exemplo de uso do ARIMA com dados climáticos (substitua pelo caminho do seu arquivo CSV)
if __name__ == "__main__":
    # Caminho do arquivo de dados climáticos
    caminho_arquivo = 'dados_climaticos.csv'
    
    # Carregar os dados
    dados = carregar_dados(caminho_arquivo)
    
    # Treinar o modelo ARIMA
    modelo_ajustado = treinar_modelo_arima(dados['Temperatura'], ordem=(5, 1, 0))
    
    # Fazer previsões para os próximos 10 dias
    previsoes = prever_temperatura(modelo_ajustado, passos_futuro=10)
    
    # Visualizar as previsões
    plotar_previsao(dados['Temperatura'], previsoes)
