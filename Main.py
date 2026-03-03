import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados fictícios
dados = {
    'horas_estudo': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nota': [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
}

df = pd.DataFrame(dados)

# Preparar dados para o modelo
X = df[['horas_estudo']]
y = df['nota']

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer predições
y_pred = modelo.predict(X)

# Visualizar
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Reais')
plt.plot(X, y_pred, color='red', linewidth=2, label='Linha de Regressão')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota')
plt.title('Relação entre Horas de Estudo e Nota')
plt.legend()
plt.grid(True)
plt.show()

print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")
