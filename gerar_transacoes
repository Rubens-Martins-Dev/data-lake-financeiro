def gerar_transacoes(df_clientes, n_transacoes=50000):
    tipos_transacao = ['PIX', 'TED', 'DOC', 'Cartão Débito', 'Cartão Crédito', 'Saque']
    
    transacoes = []
    for i in range(1, n_transacoes + 1):
        cliente_id = random.choice(df_clientes['cliente_id'].tolist())
        tipo = random.choice(tipos_transacao)
        
        # Valores baseados no tipo
        if tipo == 'PIX':
            valor = round(random.uniform(10, 1000), 2)
        elif tipo in ['Cartão Crédito', 'Cartão Débito']:
            valor = round(random.uniform(15, 2500), 2)
        else:
            valor = round(random.uniform(50, 5000), 2)
        
        transacao = {
            'transacao_id': i,
            'cliente_id': cliente_id,
            'tipo_transacao': tipo,
            'valor': valor,
            'data_transacao': (datetime.now() - timedelta(days=random.randint(1, 365), 
                                                         hours=random.randint(0, 23),
                                                         minutes=random.randint(0, 59))).strftime('%Y-%m-%d %H:%M:%S'),
            'status': random.choice(['Aprovada', 'Aprovada', 'Aprovada', 'Negada']),
            'canal': random.choice(['App', 'Internet Banking', 'ATM', 'Agência'])
        }
        transacoes.append(transacao)
    
    return pd.DataFrame(transacoes)

# Gerar transações
df_transacoes = gerar_transacoes(df_clientes)
print(f"✅ {len(df_transacoes)} transações geradas!")
df_transacoes.head()
