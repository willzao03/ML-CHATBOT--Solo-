# ML-CHATBOT--Solo-

Projeto de Machine Learning para desenvolvimento de chatbot com análise de dados e predição de intenções.

## 📋 Descrição

Este projeto implementa um sistema de chatbot utilizando técnicas de Machine Learning para classificação de intenções e análise de dados de conversação.

## 🚀 Tecnologias Utilizadas

- Python 3.11.9
- Pandas - Manipulação de dados
- Matplotlib - Visualização de dados
- Scikit-learn - Machine Learning
- NumPy - Computação numérica

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/willzao03/ML-CHATBOT--Solo-.git
cd ML-CHATBOT--Solo-
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎯 Estrutura do Projeto

- `Main.py` - Análise de regressão linear (horas de estudo vs notas)
- `gerador_01.py` - Gerador de dados fictícios para o chatbot
- `aula02_ml.py` - Modelo de classificação com DecisionTreeClassifier
- `analise_satisfacao.py` - Análise de satisfação do cliente vs investimento
- `previsao_precos.py` - Previsão de preços de imóveis com regressão linear
- `chatbot_data.csv` - Dataset gerado com features de mensagens
- `check_env.py` - Diagnóstico completo do ambiente de desenvolvimento

## 💻 Como Usar

### 1. Verificar ambiente:
```bash
python check_env.py
```

### 2. Gerar dados do chatbot:
```bash
python gerador_01.py
```

### 3. Treinar modelo de classificação:
```bash
python aula02_ml.py
```

### 4. Visualizar regressão linear (estudo vs notas):
```bash
python Main.py
```

### 5. Análise de satisfação do cliente:
```bash
python analise_satisfacao.py
```

### 6. Previsão de preços de imóveis:
```bash
python previsao_precos.py
```

## 📊 Resultados

### Modelo de Classificação (aula02_ml.py)
- Dataset com 200 registros de mensagens
- Acurácia: 97.50% - 100%
- Classificação: Dúvida (0) ou Reclamação (1)
- Features: comprimento_msg, contem_exclamacao, palavras_negativas

### Análise de Satisfação (analise_satisfacao.py)
- 10 transações analisadas
- Correlação entre valor gasto e satisfação do cliente
- Gráfico de dispersão gerado

### Previsão de Preços (previsao_precos.py)
- Modelo de regressão linear
- Previsão de preços de imóveis baseado na área
- Exemplo: 110m² = R$ 542.86 mil

### Regressão Linear (Main.py)
- Análise da relação entre horas de estudo e notas
- Visualização com linha de regressão

## 👤 Autor

Willian - [@willzao03](https://github.com/willzao03)

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
