# Relatório Técnico: Sistema de Previsão de Tipos de Acidentes Rodoviários

## 1. Objetivo do Projeto

O projeto tem como objetivo desenvolver um sistema de machine learning capaz de prever o tipo de acidente rodoviário com base em características como hora, localização, condições meteorológicas e causa do acidente. Esta ferramenta visa auxiliar na prevenção e no planejamento de recursos de atendimento a acidentes nas rodovias federais brasileiras.

## 2. Dados Utilizados

### Fonte dos Dados
- **PRF (Polícia Rodoviária Federal)**: Dados históricos de acidentes em rodovias federais, incluindo informações sobre localização, horário, condições meteorológicas e causas dos acidentes.

### Estrutura dos Dados
Principais campos utilizados:
- data_inversa
- horário
- BR (rodovia)
- km
- município
- UF
- tipo_acidente
- causa_acidente
- condicao_metereologica

## 3. Pipeline de Dados

### 3.1 Coleta
- Dados obtidos do portal de dados abertos da PRF
- Formato CSV com encoding ISO-8859-1
- Separador ";" (ponto e vírgula)

### 3.2 Tratamento
1. **Processamento com PySpark**:
   - Seleção das colunas relevantes
   - Conversão de tipos de dados
   - Tratamento de datas e horários

2. **Engenharia de Features**:
   - Criação do período do dia (Madrugada, Manhã, Tarde, Noite)
   - Extração do dia da semana
   - Agrupamento de tipos de acidentes em categorias principais

### 3.3 Features Finais
- hora (numérica)
- UF (categórica)
- BR (numérica)
- condição meteorológica (categórica)
- causa do acidente (categórica)
- período do dia (categórica)
- dia da semana (categórica)

## 4. Modelo de Machine Learning

### 4.1 Algoritmo
- **XGBoost Classifier**
- Problema de classificação multiclasse

### 4.2 Parâmetros
```python
XGBClassifier(
    use_label_encoder=False,
    eval_metric="mlogloss",
    random_state=42,
    n_estimators=70,
    max_depth=5,
    learning_rate=0.08
)
```

### 4.3 Classes Previstas
1. Colisão
2. Atropelamento
3. Capotamento/Tombamento
4. Outros

## 5. Métricas de Desempenho

### 5.1 Classification Report
```
                        precision    recall  f1-score   support

         Atropelamento       0.89      0.72      0.80       237
Capotamento/Tombamento       0.53      0.07      0.13       504
               Colisão       0.73      0.94      0.82      2814
                Outros       0.49      0.32      0.39       945

              accuracy                           0.70      4500
             macro avg       0.66      0.51      0.53      4500
          weighted avg       0.66      0.70      0.65      4500
```

### 5.2 Análise das Métricas
- Acurácia geral: 70%
- Melhor desempenho na previsão de Colisões (F1-score: 0.82)
- Bom desempenho para Atropelamentos (F1-score: 0.80)
- Desafios na previsão de Capotamento/Tombamento (F1-score: 0.13)

## 6. Dashboards

O sistema possui dois dashboards interativos:
1. **Dashboard de Dados**: Visualização e análise exploratória dos dados históricos
2. **Dashboard de Predição**: Interface para realizar previsões em tempo real

## 7. Exemplo de Predição

```python
entrada = {
    "hora": 15,
    "uf": "SP",
    "br": 116,
    "condicao_metereologica": "Céu Claro",
    "causa_acidente": "Reação tardia ou ineficiente do condutor",
    "data": "2025-06-15"
}
```

### Interpretação
O modelo analisa as características fornecidas e retorna a classe mais provável de acidente para aquelas condições específicas, auxiliando no planejamento preventivo e na alocação de recursos.

## 8. Recomendações de Uso

1. **Planejamento Preventivo**: Utilizar as previsões para direcionar ações preventivas em locais e horários de maior risco
2. **Alocação de Recursos**: Otimizar a distribuição de equipes de resgate com base nas previsões
3. **Monitoramento**: Acompanhar padrões e tendências de acidentes por região
4. **Limitações**: Considerar que o modelo é uma ferramenta de suporte à decisão, não substituindo o julgamento humano

## 9. Execução do Sistema

O sistema é executado localmente, com os seguintes componentes:
- Pipeline de processamento em PySpark
- Modelo XGBoost para previsões
- Dashboards interativos em Plotly Dash

## 10. Testes Automatizados

O projeto conta com testes automatizados via GitHub Actions, garantindo a qualidade e confiabilidade do código. Os testes incluem:
- Validação do modelo de predição
- Verificação de entradas extremas
- Testes de integração dos componentes

---

*Projeto desenvolvido como trabalho final da disciplina, utilizando dados públicos da PRF para criar um sistema de previsão de acidentes rodoviários.*
