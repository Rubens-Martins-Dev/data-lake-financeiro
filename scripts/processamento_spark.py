
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def main():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("DataLakeFinanceiro")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    try:
        # 1. RAW - Leitura dos dados
        raw = DATA_DIR / "raw"

        clientes = spark.read.option(
            "header", True
        ).csv(str(raw / "clientes.csv"))

        transacoes = spark.read.json(
            str(raw / "transacoes.json")
        )

        print("RAW: dados carregados")

        # 2. BRONZE - Tipagem e limpeza
        clientes_bronze = (
            clientes
            .withColumn(
                "cliente_id",
                F.col("cliente_id").cast("int")
            )
            .withColumn(
                "renda_mensal",
                F.col("renda_mensal").cast("double")
            )
            .withColumn(
                "score_credito",
                F.col("score_credito").cast("int")
            )
            .withColumn(
                "data_nascimento",
                F.to_date("data_nascimento")
            )
            .filter(F.col("cliente_id").isNotNull())
            .dropDuplicates(["cliente_id"])
        )

        transacoes_bronze = (
            transacoes
            .withColumn(
                "valor",
                F.col("valor").cast("double")
            )
            .withColumn(
                "data_transacao",
                F.to_timestamp("data_transacao")
            )
            .filter(F.col("valor") > 0)
            .filter(F.col("cliente_id").isNotNull())
            .filter(F.col("transacao_id").isNotNull())
            .dropDuplicates(["transacao_id"])
        )

        bronze = DATA_DIR / "bronze"

        clientes_bronze.write.mode(
            "overwrite"
        ).parquet(str(bronze / "clientes"))

        transacoes_bronze.write.mode(
            "overwrite"
        ).parquet(str(bronze / "transacoes"))

        print("BRONZE: limpeza concluída")

        # 3. SILVER - Enriquecimento
        clientes_silver = (
            clientes_bronze
            .withColumn(
                "idade",
                F.floor(
                    F.months_between(
                        F.current_date(),
                        F.col("data_nascimento")
                    ) / 12
                )
            )
            .withColumn(
                "faixa_etaria",
                F.when(F.col("idade") < 25, "Jovem")
                .when(F.col("idade") < 45, "Adulto")
                .when(F.col("idade") < 65, "Meia-idade")
                .otherwise("Idoso")
            )
            .withColumn(
                "classe_renda",
                F.when(
                    F.col("renda_mensal") < 2500, "Baixa"
                )
                .when(
                    F.col("renda_mensal") < 8000, "Média"
                )
                .otherwise("Alta")
            )
        )

        transacoes_silver = (
            transacoes_bronze
            .join(
                clientes_silver.select(
                    "cliente_id",
                    "faixa_etaria",
                    "classe_renda"
                ),
                "cliente_id",
                "inner"
            )
            .withColumn(
                "ano_mes",
                F.date_format(
                    "data_transacao", "yyyy-MM"
                )
            )
            .withColumn(
                "hora",
                F.hour("data_transacao")
            )
            .withColumn(
                "periodo_dia",
                F.when(F.col("hora") < 6, "Madrugada")
                .when(F.col("hora") < 12, "Manhã")
                .when(F.col("hora") < 18, "Tarde")
                .otherwise("Noite")
            )
        )

        silver = DATA_DIR / "silver"

        clientes_silver.write.mode(
            "overwrite"
        ).parquet(str(silver / "clientes"))

        transacoes_silver.write.mode(
            "overwrite"
        ).parquet(str(silver / "transacoes"))

        print("SILVER: enriquecimento concluído")

        # 4. GOLD - Indicadores financeiros
        aprovadas = transacoes_silver.filter(
            F.col("status") == "Aprovada"
        )

        resumo_clientes = (
            aprovadas
            .groupBy("cliente_id")
            .agg(
                F.count("*").alias("total_transacoes"),
                F.round(
                    F.sum("valor"), 2
                ).alias("valor_total"),
                F.round(
                    F.avg("valor"), 2
                ).alias("ticket_medio")
            )
        )

        performance_tipo = (
            transacoes_silver
            .groupBy("tipo_transacao", "status")
            .agg(
                F.count("*").alias("quantidade"),
                F.round(
                    F.sum("valor"), 2
                ).alias("valor_total")
            )
        )

        analise_temporal = (
            aprovadas
            .groupBy("ano_mes", "periodo_dia")
            .agg(
                F.count("*").alias("total_transacoes"),
                F.round(
                    F.sum("valor"), 2
                ).alias("valor_total")
            )
        )

        gold = DATA_DIR / "gold"

        resumo_clientes.write.mode(
            "overwrite"
        ).parquet(str(gold / "resumo_clientes"))

        performance_tipo.write.mode(
            "overwrite"
        ).parquet(str(gold / "performance_tipo"))

        analise_temporal.write.mode(
            "overwrite"
        ).parquet(str(gold / "analise_temporal"))

        print("GOLD: indicadores gerados")

        # 5. Validação final
        print("\nRESULTADOS")
        print("Clientes:", clientes_silver.count())
        print("Transações:", transacoes_silver.count())

        print("\nResumo por tipo:")
        performance_tipo.show(truncate=False)

        print("Pipeline concluído com sucesso!")

    finally:
        spark.stop()


if __name__ == "__main__":
    main()
