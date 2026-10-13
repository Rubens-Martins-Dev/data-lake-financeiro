
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from gerar_clientes import gerar_clientes


def gerar_transacoes(df_clientes, n_transacoes=50000):
    """Gera transações financeiras sintéticas."""

    if df_clientes.empty:
        raise ValueError("A base de clientes não pode estar vazia.")

    if n_transacoes <= 0:
        raise ValueError(
            "A quantidade de transações deve ser maior que zero."
        )

    tipos_transacao = [
        "PIX", "TED", "DOC",
        "Cartão Débito", "Cartão Crédito", "Saque"
    ]

    ids_clientes = df_clientes["cliente_id"].tolist()
    agora = datetime.now()
    transacoes = []

    for i in range(1, n_transacoes + 1):
        cliente_id = random.choice(ids_clientes)
        tipo = random.choice(tipos_transacao)

        if tipo == "PIX":
            valor = round(random.uniform(10, 1000), 2)
        elif tipo in ["Cartão Crédito", "Cartão Débito"]:
            valor = round(random.uniform(15, 2500), 2)
        else:
            valor = round(random.uniform(50, 5000), 2)

        data = agora - timedelta(
            days=random.randint(1, 365),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        transacoes.append({
            "transacao_id": i,
            "cliente_id": cliente_id,
            "tipo_transacao": tipo,
            "valor": valor,
            "data_transacao": data.strftime("%Y-%m-%d %H:%M:%S"),
            "status": random.choice([
                "Aprovada", "Aprovada", "Aprovada", "Negada"
            ]),
            "canal": random.choice([
                "App", "Internet Banking", "ATM", "Agência"
            ])
        })

    return pd.DataFrame(transacoes)


def main():
    print("Iniciando geração de dados financeiros...")

    raiz_projeto = Path(__file__).resolve().parent.parent
    diretorio_raw = raiz_projeto / "data" / "raw"
    diretorio_raw.mkdir(parents=True, exist_ok=True)

    # Gera os clientes
    df_clientes = gerar_clientes()

    # Exporta clientes para CSV
    df_clientes.to_csv(
        diretorio_raw / "clientes.csv",
        index=False,
        encoding="utf-8"
    )

    # Gera as transações
    df_transacoes = gerar_transacoes(df_clientes)

    # Exporta JSON Lines, compatível com Spark
    df_transacoes.to_json(
        diretorio_raw / "transacoes.json",
        orient="records",
        lines=True,
        force_ascii=False
    )

    print(f"Clientes gerados: {len(df_clientes):,}")
    print(f"Transações geradas: {len(df_transacoes):,}")
    print(f"Arquivos salvos em: {diretorio_raw}")

    print("\nAmostra das transações:")
    print(df_transacoes.head())


if __name__ == "__main__":
    main()
