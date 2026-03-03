import pandas as pd
import random

# Gerar dados fictícios para chatbot
def gerar_dados_chatbot(num_registros=100):
    intencoes = ['saudacao', 'despedida', 'ajuda', 'informacao', 'reclamacao']
    respostas = {
        'saudacao': ['Olá!', 'Oi, como posso ajudar?', 'Bem-vindo!'],
        'despedida': ['Até logo!', 'Tchau!', 'Volte sempre!'],
        'ajuda': ['Como posso ajudar?', 'Estou aqui para ajudar!', 'Diga-me o que precisa.'],
        'informacao': ['Aqui está a informação.', 'Veja os detalhes.', 'Confira os dados.'],
        'reclamacao': ['Lamento o inconveniente.', 'Vamos resolver isso.', 'Desculpe pelo problema.']
    }
    
    dados = []
    for _ in range(num_registros):
        intencao = random.choice(intencoes)
        resposta = random.choice(respostas[intencao])
        confianca = random.uniform(0.7, 1.0)
        
        dados.append({
            'intencao': intencao,
            'resposta': resposta,
            'confianca': round(confianca, 2)
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('chatbot_data.csv', index=False)
    print(f"✓ Arquivo 'chatbot_data.csv' gerado com {num_registros} registros!")
    return df

if __name__ == "__main__":
    df = gerar_dados_chatbot(100)
    print("\nPrimeiras linhas do dataset:")
    print(df.head())
    print(f"\nDistribuição de intenções:")
    print(df['intencao'].value_counts())
