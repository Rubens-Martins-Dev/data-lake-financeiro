
import random
from datetime import datetime, timedelta

import pandas as pd
from gerar_clientes import gerar_clientes


def gerar_transacoes(df_clientes, n_transacoes=50000):
    """
    Gera transações financeiras sintéticas para clientes.

    Parâmetros:
        df_clientes: DataFrame com os clientes cadastrados.
        n_transacoes: Quantidade de transações desejadas.

    Retorno:
        DataFrame com as transações geradas.
    """

    if df_clientes.empty:
        raise ValueError("A base de clientes não pode estar vazia.")

    tipos_transacao = [
        "PIX",
        "TED",
        "DOC",
        "Cartão Débito",
        "Cartão Crédito",
        "Saque"
    ]

    ids_clientes = df_clientes["cliente_id"].tolist()
    transacoes = []

    for i in range(1, n_transacoes + 1):
        cliente_id = random.choice(ids_clientes)
        tipo = random.choice(tipos_transacao)

        # Define valores conforme o tipo de transação
        if tipo == "PIX":
            valor = round(random.uniform(10, 1000), 2)
        elif tipo in ["Cartão Crédito", "Cartão Débito"]:
            valor = round(random.uniform(15, 2500), 2)
        else:
            valor = round(random.uniform(50, 5000), 2)

        data_transacao = datetime.now() - timedelta(
            days=random.randint(1, 365),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        transacao = {
            "transacao_id": i,
            "cliente_id": cliente_id,
            "tipo_transacao": tipo,
            "valor": valor,
            "data_transacao": data_transacao.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "status": random.choice([
                "Aprovada",
                "Aprovada",
                "Aprovada",
                "Negada"
            ]),
            "canal": random.choice([
                "App",
                "Internet Banking",
                "ATM",
                "Agência"
            ])
        }

        transacoes.append(transacao)

    return pd.DataFrame(transacoes)


def main():
    # Gera a base sintética de clientes
    df_clientes = gerar_clientes()

    # Gera as transações
    df_transacoes = gerar_transacoes(df_clientes)

    print(f"Clientes gerados: {len(df_clientes):,}")
    print(f"Transações geradas: {len(df_transacoes):,}")

    # Exibe as primeiras transações
    print("\nAmostra das transações:")
    print(df_transacoes.head())


if __name__ == "__main__":
    main()
