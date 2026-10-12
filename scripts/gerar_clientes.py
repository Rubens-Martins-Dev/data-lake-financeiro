
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


def gerar_clientes(n_clientes=10000):
    """
    Gera uma base sintética de clientes financeiros.

    Parâmetros:
        n_clientes: Quantidade de clientes desejada.

    Retorno:
        DataFrame contendo os clientes gerados.
    """

    if n_clientes <= 0:
        raise ValueError(
            "A quantidade de clientes deve ser maior que zero."
        )

    nomes = [
        "João", "Maria", "Pedro", "Ana",
        "Carlos", "Fernanda", "Ricardo", "Juliana"
    ]

    sobrenomes = [
        "Silva", "Santos", "Oliveira", "Souza",
        "Rodrigues", "Ferreira", "Alves", "Pereira"
    ]

    cidades = [
        "São Paulo",
        "Rio de Janeiro",
        "Belo Horizonte",
        "Salvador",
        "Fortaleza"
    ]

    clientes = []
    agora = datetime.now()

    for i in range(1, n_clientes + 1):

        cliente = {
            "cliente_id": i,
            "nome": (
                f"{random.choice(nomes)} "
                f"{random.choice(sobrenomes)}"
            ),
            "cpf": f"{random.randint(0, 99999999999):011d}",
            "data_nascimento": (
                agora - timedelta(
                    days=random.randint(6570, 25550)
                )
            ).strftime("%Y-%m-%d"),
            "renda_mensal": round(
                random.uniform(1500, 25000), 2
            ),
            "score_credito": random.randint(300, 850),
            "cidade": random.choice(cidades),
            "data_cadastro": (
                agora - timedelta(
                    days=random.randint(1, 1095)
                )
            ).strftime("%Y-%m-%d %H:%M:%S")
        }

        clientes.append(cliente)

    return pd.DataFrame(clientes)


def main():

    print("Iniciando geração de clientes...")

    df_clientes = gerar_clientes()

    # Define o diretório RAW na raiz do projeto
    diretorio_projeto = Path(__file__).resolve().parent.parent
    diretorio_raw = diretorio_projeto / "data" / "raw"

    diretorio_raw.mkdir(parents=True, exist_ok=True)

    caminho_arquivo = diretorio_raw / "clientes.csv"

    df_clientes.to_csv(
        caminho_arquivo,
        index=False,
        encoding="utf-8"
    )

    print(f"Clientes gerados: {len(df_clientes):,}")
    print(f"Arquivo salvo em: {caminho_arquivo}")

    print("\nAmostra dos clientes:")
    print(df_clientes.head())


if __name__ == "__main__":
    main()
