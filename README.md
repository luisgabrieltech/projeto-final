# 🚧 Sistema de Previsão de Tipos de Acidentes Rodoviários

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0%2B-orange)](https://xgboost.readthedocs.io/)
[![PySpark](https://img.shields.io/badge/PySpark-3.5%2B-yellow)](https://spark.apache.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-red)](https://streamlit.io/)
[![Dash](https://img.shields.io/badge/Dash-3.0%2B-lightblue)](https://dash.plotly.com/)

## 📋 Sobre o Projeto

Este sistema utiliza **Machine Learning** para prever tipos de acidentes rodoviários com base em dados históricos da **Polícia Rodoviária Federal (PRF)**. O objetivo é auxiliar na prevenção de acidentes e no planejamento estratégico de recursos de segurança rodoviária.

### 🎯 Objetivos
- Prever o tipo de acidente (Colisão, Atropelamento, Capotamento, etc.)
- Auxiliar no planejamento preventivo de recursos
- Fornecer insights sobre padrões de acidentes
- Criar dashboards interativos para análise de dados

### 🏆 Principais Características
- **Modelo XGBoost** com 70% de acurácia
- **Pipeline completo** de processamento de dados com PySpark
- **Dashboards interativos** em Dash e Streamlit
- **Testes automatizados** com pytest
- **Análise exploratória** em Jupyter Notebooks

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Machine Learning**: XGBoost, Scikit-learn
- **Processamento de Dados**: PySpark, Pandas
- **Visualização**: Plotly, Dash, Streamlit
- **Testes**: Pytest
- **Análise**: Jupyter Notebooks

## 📂 Estrutura do Projeto

```
projeto-final/
├── data/
│   ├── raw/
│   │   └── acidentes.csv           # Dados brutos da PRF
│   └── processed/
│       └── acidentes_tratado.csv   # Dados processados
├── models/
│   ├── model.pkl                   # Modelo treinado XGBoost
│   ├── label_encoders.pkl          # Encoders para variáveis categóricas
│   ├── target_encoder.pkl          # Encoder para variável target
│   └── classification_report.txt   # Relatório de desempenho
├── src/
│   ├── data_processing.py          # Processamento de dados (PySpark)
│   ├── ml_pipeline.py             # Pipeline de ML
│   ├── predict.py                 # Funções de predição
│   ├── dashboard_dados.py         # Dashboard de análise (Dash)
│   └── dashboard_predict.py       # Dashboard de predição (Streamlit)
├── notebooks/
│   └── eda.ipynb                  # Análise exploratória
├── tests/
│   ├── conftest.py                # Configurações de teste
│   └── test_predict.py            # Testes do modelo
├── reports/
│   └── relatorio.md               # Relatório técnico completo
└── requirements.txt               # Dependências
```

## 🚀 Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone https://github.com/luisgabrieltech/projeto-final.git
cd projeto-final
```

### 2. Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração do Java (para PySpark)
Certifique-se de ter o Java 8+ instalado para usar o PySpark:
```bash
java -version
```

## 📊 Como Usar

### 1. Processamento dos Dados
```bash
# Processa os dados brutos da PRF
python src/data_processing.py
```

### 2. Treinamento do Modelo
```bash
# Treina o modelo XGBoost e salva os artefatos
python src/ml_pipeline.py
```

### 3. Dashboard de Análise de Dados
```bash
# Inicia o dashboard interativo para análise exploratória
python src/dashboard_dados.py
```
Acesse: http://localhost:8050

### 4. Dashboard de Predição
```bash
# Inicia a interface de predição em tempo real
streamlit run src/dashboard_predict.py
```
Acesse: http://localhost:8501

### 5. Predição via API
```python
from src.predict import prever_acidente

# Exemplo de uso
entrada = {
    "hora": 15,
    "uf": "SP", 
    "br": 116,
    "condicao_metereologica": "Céu Claro",
    "causa_acidente": "Reação tardia ou ineficiente do condutor",
    "data": "2025-06-15"
}

resultado = prever_acidente(entrada)
print(f"Tipo de acidente previsto: {resultado}")
```

## 📈 Modelo de Machine Learning

### Algoritmo
- **XGBoost Classifier** otimizado para classificação multiclasse

### Features Utilizadas
- `hora`: Hora do dia (0-23)
- `uf`: Estado onde ocorreu o acidente
- `br`: Número da rodovia federal
- `condicao_metereologica`: Condições climáticas
- `causa_acidente`: Causa principal do acidente
- `periodo_dia`: Período (Madrugada, Manhã, Tarde, Noite)
- `dia_semana`: Dia da semana

### Classes Previstas
1. **Colisão** - Diversos tipos de colisões
2. **Atropelamento** - Atropelamento de pedestres e animais
3. **Capotamento/Tombamento** - Acidentes com capotamento
4. **Outros** - Outros tipos de acidentes

### Desempenho
- **Acurácia Geral**: 70%
- **Melhor Classe**: Colisão (F1-score: 0.82)
- **Maior Desafio**: Capotamento/Tombamento (F1-score: 0.13)

## 🧪 Testes

Execute os testes automatizados:
```bash
# Executa todos os testes
pytest

# Executa testes com cobertura
pytest --cov=src

# Executa testes específicos
pytest tests/test_predict.py -v
```

## 📊 Dashboards

### Dashboard de Análise (Dash)
- Visualizações interativas dos dados históricos
- Gráficos de distribuição por causa, estado, hora e tipo
- Interface responsiva com Bootstrap

### Dashboard de Predição (Streamlit) 
- Interface amigável para fazer predições
- Seleção interativa de parâmetros
- Resultado em tempo real

## 📋 Análise Exploratória

Execute o notebook de análise exploratória:
```bash
jupyter lab notebooks/eda.ipynb
```

O notebook contém:
- Análise estatística dos dados
- Visualizações avançadas
- Correlações entre variáveis
- Insights sobre padrões de acidentes

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📋 Requisitos do Sistema

- **Python**: 3.8+
- **Java**: 8+ (para PySpark)
- **Memória RAM**: 4GB+ recomendado
- **Espaço em Disco**: 1GB+ para dados e modelos

## 🐛 Resolução de Problemas

### Erro com PySpark
```bash
# Configure as variáveis de ambiente
export JAVA_HOME=/path/to/java
export SPARK_HOME=/path/to/spark
```

### Erro de Dependências
```bash
# Reinstale as dependências
pip install --upgrade -r requirements.txt
```

### Modelo não Encontrado
```bash
# Execute o pipeline de ML primeiro
python src/ml_pipeline.py
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- **PRF (Polícia Rodoviária Federal)** pelos dados públicos
- **Comunidade Open Source** pelas ferramentas utilizadas
- **Faculdade** pelo suporte acadêmico

## 📚 Referências

- [Dados Abertos PRF](https://portal.prf.gov.br/dados-abertos)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Dash Documentation](https://dash.plotly.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐