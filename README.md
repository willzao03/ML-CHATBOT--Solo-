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
- `aula02_ml.py` - Análise e treinamento do modelo de classificação
- `chatbot_data.csv` - Dataset gerado com intenções e respostas
- `check_env.py` - Verificação do ambiente de desenvolvimento

## 💻 Como Usar

### Verificar ambiente:
```bash
python check_env.py
```

### Gerar dados do chatbot:
```bash
python gerador_01.py
```

### Executar análise e treinamento:
```bash
python aula02_ml.py
```

### Visualizar regressão linear:
```bash
python Main.py
```

## 📊 Resultados

O projeto gera:
- Dataset com 100 registros de intenções do chatbot
- Análise de distribuição de intenções
- Modelo de classificação com Naive Bayes
- Gráficos de visualização salvos em `analise_chatbot.png`
- Métricas de acurácia e relatório de classificação

## 📝 Intenções Suportadas

- Saudação
- Despedida
- Ajuda
- Informação
- Reclamação

## 👤 Autor

William - [@willzao03](https://github.com/willzao03)

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
