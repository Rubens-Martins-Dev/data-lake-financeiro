import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
import os

print("✅ Bibliotecas carregadas!")

def gerar_clientes(n_clientes=10000):
    nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Fernanda', 'Ricardo', 'Juliana']
    sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Alves', 'Pereira']
    
    clientes = []
    for i in range(1, n_clientes + 1):
        cliente = {
            'cliente_id': i,
            'nome': f"{random.choice(nomes)} {random.choice(sobrenomes)}",
            'cpf': f"{random.randint(10000000000, 99999999999)}",
            'data_nascimento': (datetime.now() - timedelta(days=random.randint(6570, 25550))).strftime('%Y-%m-%d'),
            'renda_mensal': round(random.uniform(1500, 25000), 2),
            'score_credito': random.randint(300, 850),
            'cidade': random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza']),
            'data_cadastro': (datetime.now() - timedelta(days=random.randint(1, 1095))).strftime('%Y-%m-%d %H:%M:%S')
        }
        clientes.append(cliente)
    
    return pd.DataFrame(clientes)

# Gerar dados
df_clientes = gerar_clientes()
print(f"✅ {len(df_clientes)} clientes gerados!")
df_clientes.head()
