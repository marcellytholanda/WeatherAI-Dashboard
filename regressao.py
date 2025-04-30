# Importando bibliotecas necessárias
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Função para carregar dados climáticos (exemplo com CSV)
def carregar_dados(caminho_arquivo):
    """
    Carrega dados climáticos a partir de um arquivo CSV.
    :param caminho_arquivo: Caminho do arquivo CSV com os dados climáticos.
    :return: DataFrame com os dados climáticos.
    """
    dados = pd.read_csv(caminho_arquivo, parse_dates=True, index_col='Data')
    return dados

# Função para treinar o modelo de Regressão Linear
def treinar_modelo_regressao(dados, variaveis_entrada, variavel_saida):
    """
    Treina o modelo de Regressão Linear com os dados fornecidos.
    :param dados: DataFrame com os dados climáticos.
    :param variaveis_entrada: Lista de colunas para as variáveis independentes.
    :param variavel_saida: Coluna da variável dependente (temperatura).
    :return: Modelo de regressão treinado.
    """
    X = dados[variaveis_entrada]  # Variáveis independentes
    y = dados[variavel_saida]  # Variável dependente (ex: temperatura)
    
    # Dividindo os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Criando e treinando o modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Fazendo previsões
    y_pred = modelo.predict(X_test)
    
    # Calculando métricas de desempenho
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Erro Quadrático Médio (MSE): {mse}")
    print(f"Coeficiente de Determinação (R²): {r2}")
    
    return modelo, X_test, y_test, y_pred

# Função para visualizar os resultados
def plotar_resultados(y_test, y_pred):
    """
    Plota os valores reais versus as previsões feitas pelo modelo de regressão linear.
    :param y_test: Valores reais da variável dependente.
    :param y_pred: Previsões feitas pelo modelo.
    """
    plt.figure(figsize=(10,6))
    plt.scatter(y_test, y_pred, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
    plt.title('Regressão Linear: Valores Reais vs Previsões')
    plt.xlabel('Valores Reais')
    plt.ylabel('Previsões')
    plt.show()

# Exemplo de uso da Regressão Linear com dados climáticos (substitua pelo caminho do seu arquivo CSV)
if __name__ == "__main__":
    # Caminho do arquivo de dados climáticos
    caminho_arquivo = 'dados_climaticos.csv'
    
    # Carregar os dados
    dados = carregar_dados(caminho_arquivo)
    
    # Definir as variáveis de entrada e saída (exemplo)
    variaveis_entrada = ['Umidade', 'Pressao']  # Exemplo de variáveis independentes
    variavel_saida = 'Temperatura'  # Variável dependente
    
    # Treinar o modelo de regressão
    modelo, X_test, y_test, y_pred = treinar_modelo_regressao(dados, variaveis_entrada, variavel_saida)
    
    # Visualizar os resultados
    plotar_resultados(y_test, y_pred)
