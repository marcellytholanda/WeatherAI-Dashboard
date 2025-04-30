-- Criação da Tabela para Dados Climáticos
CREATE TABLE dados_climaticos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_registro DATE NOT NULL,
    temperatura DECIMAL(5,2),
    umidade DECIMAL(5,2),
    pressao DECIMAL(6,2),
    localizacao VARCHAR(100)
);

-- Inserção de Dados de Exemplo
INSERT INTO dados_climaticos (data_registro, temperatura, umidade, pressao, localizacao)
VALUES
('2025-01-01', 29.4, 78.2, 1012.3, 'Rio de Janeiro - RJ'),
('2025-01-02', 30.1, 80.5, 1011.9, 'Rio de Janeiro - RJ'),
('2025-01-03', 28.9, 82.0, 1010.7, 'Rio de Janeiro - RJ');

-- Consulta 1: Temperatura média no mês de janeiro
SELECT 
    AVG(temperatura) AS temperatura_media_janeiro
FROM 
    dados_climaticos
WHERE 
    MONTH(data_registro) = 1;

-- Consulta 2: Tendência de temperatura diária (últimos 7 dias)
SELECT 
    data_registro, 
    temperatura
FROM 
    dados_climaticos
ORDER BY 
    data_registro DESC
LIMIT 7;

-- Consulta 3: Umidade máxima registrada
SELECT 
    MAX(umidade) AS umidade_maxima
FROM 
    dados_climaticos;

-- Consulta 4: Dias com temperatura acima de 30°C
SELECT 
    data_registro, 
    temperatura
FROM 
    dados_climaticos
WHERE 
    temperatura > 30;

-- Consulta 5: Agrupamento de dados por localidade
SELECT 
    localizacao,
    COUNT(*) AS total_registros,
    AVG(temperatura) AS media_temperatura,
    AVG(umidade) AS media_umidade
FROM 
    dados_climaticos
GROUP BY 
    localizacao;
