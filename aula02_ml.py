import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Carregar dados
print("=" * 50)
print("ANÁLISE DE DADOS DO CHATBOT")
print("=" * 50)

df = pd.read_csv('chatbot_data.csv')

print(f"\n✓ Dataset carregado: {len(df)} registros")
print(f"\nPrimeiras linhas:")
print(df.head())

print(f"\n\nDistribuição de Intenções:")
print(df['intencao'].value_counts())

# Análise de confiança
print(f"\n\nEstatísticas de Confiança:")
print(df['confianca'].describe())

# Visualização 1: Distribuição de Intenções
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
df['intencao'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribuição de Intenções')
plt.xlabel('Intenção')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Visualização 2: Confiança por Intenção
plt.subplot(1, 2, 2)
df.groupby('intencao')['confianca'].mean().plot(kind='bar', color='coral')
plt.title('Confiança Média por Intenção')
plt.xlabel('Intenção')
plt.ylabel('Confiança Média')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('analise_chatbot.png')
print("\n✓ Gráfico salvo como 'analise_chatbot.png'")
plt.show()

# Machine Learning Simples
print("\n" + "=" * 50)
print("TREINAMENTO DO MODELO")
print("=" * 50)

# Preparar dados
X = df['resposta']
y = df['intencao']

# Vetorização
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Treinar modelo
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# Avaliar
y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)

print(f"\n✓ Modelo treinado!")
print(f"✓ Acurácia: {acuracia:.2%}")
print(f"\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!")
print("=" * 50)
