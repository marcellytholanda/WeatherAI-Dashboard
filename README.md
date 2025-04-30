# WeatherAI-Dashboard

Este repositório apresenta o projeto **WeatherAI-Dashboard**, um dashboard interativo desenvolvido para visualização de dados climáticos em tempo real e geração de previsões com base em modelos de Inteligência Artificial.

## 🎯 Objetivo

Fornecer uma ferramenta visual e educativa para análise de dados climáticos, com foco na conscientização ambiental e na aplicação de técnicas de Ciência de Dados no contexto do Ensino Médio.

## 🧠 Tecnologias e Métodos Utilizados

- Power BI para visualização e integração de dados
- Python com modelos de IA para previsão:
  - ARIMA (séries temporais)
  - Regressão Linear
- SQL para manipulação e consultas de dados
- API OpenWeatherMap para coleta de dados climáticos reais

---

## 📊 Apresentação do Dashboard

Este repositório contém:

- Imagens de cenários climáticos
- Vídeo demonstrativo do dashboard em funcionamento
- Scripts utilizados como base no projeto (em Python e SQL)

> O dashboard foi aplicado no Colégio São João de Deus (RJ), como ferramenta educativa interativa para alunos do Ensino Médio, em alinhamento com o ODS 13: Ação Contra a Mudança Global do Clima.

---

## 📦 Scripts Utilizados no Projeto

> Os códigos abaixo são modelos usados para gerar os dados analisados no dashboard. Eles são demonstrativos e não precisam ser executados neste repositório.

### `api_coleta.py`
Modelo de script em Python para coleta de dados da API OpenWeatherMap, simulando a obtenção de temperatura, umidade, pressão etc.

### `modelo_arima.py`
Modelo de previsão utilizando ARIMA (AutoRegressive Integrated Moving Average) aplicado a séries temporais climáticas.

### `regressao.py`
Script de exemplo com aplicação de Regressão Linear para prever temperaturas futuras com base em dados históricos.

### `consultas.sql`
Script com:
- Estrutura de tabela `dados_climaticos`
- Inserções simuladas
- Consultas SQL para análise no Power BI (temperatura média, dias mais quentes, agrupamentos por cidade, etc.)

---

## 🌍 Projeções de Mudança Climática

De acordo com o IPCC:

- Até 2050: aumento médio de aproximadamente 1.5°C
- Até 2100: aumento entre 2°C e 4°C

O dashboard simula essas projeções com base em diferentes cenários de emissão (baixo, médio e alto).

---

## 🧪 Resultados Esperados/Obtidos

- Visualização de dados climáticos em tempo real
- Geração de previsões com base em modelos de IA
- Interface acessível e interativa para professores e estudantes
- Conscientização ambiental e aprendizado prático em sala de aula

---

## 📁 Estrutura do Repositório

├── api_coleta.py # Coleta de dados climáticos (modelo)
├── modelo_arima.py # Previsão climática com ARIMA
├── regressao.py # Previsão com Regressão Linear
├── consultas.sql # Estrutura e consultas SQL
├── README.md # Documentação do projeto
├── WeatherAI-Dashboard.mp4 # Vídeo demonstrativo
└── imagens/ # Gráficos e cenários simulados

---

## 👩‍🏫 Aplicação Educacional

- **Instituição:** Colégio São João de Deus – Rio de Janeiro/RJ  
- **Público-alvo:** Estudantes e professores do Ensino Médio  
- **ODS Atendido:** 13 – Ação Contra a Mudança Global do Clima

---

## 📽️ Demonstração

🔗 Repositório com imagens, vídeo e códigos-modelo:  
[https://github.com/marcellytholanda/WeatherAI-Dashboard](https://github.com/marcellytholanda/WeatherAI-Dashboard)

---

## ✅ Considerações Finais

Este projeto proporcionou aprendizado prático em:

- Integração de APIs climáticas
- Desenvolvimento de modelos preditivos com Python
- Visualização de dados com Power BI
- Aplicação real da Ciência de Dados no contexto educacional
