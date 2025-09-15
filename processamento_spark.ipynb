from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os

# Criar sessão Spark
spark = SparkSession.builder \
    .appName("DataLakeFinanceiro") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

print("✅ Spark inicializado!")
spark.sparkContext.setLogLevel("WARN")  # Reduzir logs

# Ler dados da camada RAW
df_clientes_raw = spark.read.option("header", "true").csv("/home/jovyan/data/raw/clientes.csv")
df_transacoes_raw = spark.read.json("/home/jovyan/data/raw/transacoes.json")

print("✅ Dados RAW carregados!")
print(f"Clientes: {df_clientes_raw.count()} registros")
print(f"Transações: {df_transacoes_raw.count()} registros")

# Mostrar schema
print("\n=== SCHEMA CLIENTES ===")
df_clientes_raw.printSchema()


# Criar pastas para Bronze
os.makedirs('/home/jovyan/data/bronze', exist_ok=True)

# BRONZE - Limpeza básica e tipagem
# Clientes Bronze
df_clientes_bronze = df_clientes_raw \
    .withColumn("cliente_id", col("cliente_id").cast("integer")) \
    .withColumn("renda_mensal", col("renda_mensal").cast("double")) \
    .withColumn("score_credito", col("score_credito").cast("integer")) \
    .withColumn("data_nascimento", to_date(col("data_nascimento"), "yyyy-MM-dd")) \
    .withColumn("data_cadastro", to_timestamp(col("data_cadastro"), "yyyy-MM-dd HH:mm:ss")) \
    .filter(col("nome").isNotNull()) \
    .filter(col("cpf").isNotNull())

# Transações Bronze  
df_transacoes_bronze = df_transacoes_raw \
    .withColumn("transacao_id", col("transacao_id").cast("integer")) \
    .withColumn("cliente_id", col("cliente_id").cast("integer")) \
    .withColumn("valor", col("valor").cast("double")) \
    .withColumn("data_transacao", to_timestamp(col("data_transacao"), "yyyy-MM-dd HH:mm:ss")) \
    .filter(col("valor") > 0) \
    .filter(col("status").isNotNull())

print("✅ Dados BRONZE processados!")
print(f"Clientes Bronze: {df_clientes_bronze.count()} registros")
print(f"Transações Bronze: {df_transacoes_bronze.count()} registros")


# Salvar em formato Parquet (mais eficiente)
df_clientes_bronze.write.mode("overwrite").parquet("/home/jovyan/data/bronze/clientes")
df_transacoes_bronze.write.mode("overwrite").parquet("/home/jovyan/data/bronze/transacoes")

print("✅ Dados BRONZE salvos em Parquet!")
print("📁 /data/bronze/clientes/")
print("📁 /data/bronze/transacoes/")


# Criar pastas para Silver
os.makedirs('/home/jovyan/data/silver', exist_ok=True)

# SILVER - Enriquecimento e modelagem dimensional
# Clientes Silver - com análises adicionais
df_clientes_silver = df_clientes_bronze \
    .withColumn("idade", floor(datediff(current_date(), col("data_nascimento")) / 365.25)) \
    .withColumn("faixa_etaria", 
                when(col("idade") < 25, "Jovem")
                .when(col("idade") < 45, "Adulto")
                .when(col("idade") < 65, "Meia-idade")
                .otherwise("Idoso")) \
    .withColumn("classe_renda",
                when(col("renda_mensal") < 2500, "Baixa")
                .when(col("renda_mensal") < 8000, "Média")
                .otherwise("Alta")) \
    .withColumn("categoria_score",
                when(col("score_credito") < 500, "Baixo")
                .when(col("score_credito") < 700, "Médio")
                .otherwise("Alto"))

print("✅ Clientes SILVER processados!")
df_clientes_silver.select("nome", "idade", "faixa_etaria", "classe_renda", "categoria_score").show(5)



# Transações Silver - enriquecidas com dados do cliente
df_transacoes_silver = df_transacoes_bronze \
    .join(df_clientes_silver.select("cliente_id", "faixa_etaria", "classe_renda", "categoria_score"), "cliente_id", "left") \
    .withColumn("ano_mes", date_format(col("data_transacao"), "yyyy-MM")) \
    .withColumn("dia_semana", date_format(col("data_transacao"), "EEEE")) \
    .withColumn("hora", hour(col("data_transacao"))) \
    .withColumn("periodo_dia",
                when(col("hora") < 6, "Madrugada")
                .when(col("hora") < 12, "Manhã")
                .when(col("hora") < 18, "Tarde")
                .otherwise("Noite")) \
    .withColumn("faixa_valor",
                when(col("valor") < 100, "Baixo")
                .when(col("valor") < 1000, "Médio")
                .otherwise("Alto"))

print("✅ Transações SILVER processadas!")
df_transacoes_silver.select("transacao_id", "tipo_transacao", "valor", "faixa_valor", "periodo_dia", "classe_renda").show(5)


# Transações Silver - enriquecidas com dados do cliente
df_transacoes_silver = df_transacoes_bronze \
    .join(df_clientes_silver.select("cliente_id", "faixa_etaria", "classe_renda", "categoria_score"), "cliente_id", "left") \
    .withColumn("ano_mes", date_format(col("data_transacao"), "yyyy-MM")) \
    .withColumn("dia_semana", date_format(col("data_transacao"), "EEEE")) \
    .withColumn("hora", hour(col("data_transacao"))) \
    .withColumn("periodo_dia",
                when(col("hora") < 6, "Madrugada")
                .when(col("hora") < 12, "Manhã")
                .when(col("hora") < 18, "Tarde")
                .otherwise("Noite")) \
    .withColumn("faixa_valor",
                when(col("valor") < 100, "Baixo")
                .when(col("valor") < 1000, "Médio")
                .otherwise("Alto"))

print("✅ Transações SILVER processadas!")
df_transacoes_silver.select("transacao_id", "tipo_transacao", "valor", "faixa_valor", "periodo_dia", "classe_renda").show(5)


# Criar pastas para Gold
os.makedirs('/home/jovyan/data/gold', exist_ok=True)

# GOLD - Métricas de negócio prontas para dashboards
# 1. Resumo por cliente
resumo_clientes = df_transacoes_silver \
    .filter(col("status") == "Aprovada") \
    .groupBy("cliente_id", "faixa_etaria", "classe_renda", "categoria_score") \
    .agg(
        count("transacao_id").alias("total_transacoes"),
        sum("valor").alias("valor_total"),
        avg("valor").alias("ticket_medio"),
        countDistinct("tipo_transacao").alias("tipos_diferentes"),
        max("data_transacao").alias("ultima_transacao")
    ) \
    .withColumn("ticket_medio", round(col("ticket_medio"), 2))

print("✅ Resumo por cliente criado!")
resumo_clientes.orderBy(desc("valor_total")).show(10)


# 2. Performance por tipo de transação
performance_tipo = df_transacoes_silver \
    .groupBy("tipo_transacao", "status") \
    .agg(
        count("transacao_id").alias("quantidade"),
        sum("valor").alias("valor_total"),
        avg("valor").alias("ticket_medio")
    ) \
    .withColumn("ticket_medio", round(col("ticket_medio"), 2))

# 3. Análise temporal
analise_temporal = df_transacoes_silver \
    .filter(col("status") == "Aprovada") \
    .groupBy("ano_mes", "periodo_dia") \
    .agg(
        count("transacao_id").alias("total_transacoes"),
        sum("valor").alias("valor_total"),
        countDistinct("cliente_id").alias("clientes_unicos")
    )

print("✅ Métricas GOLD criadas!")
print("\n=== PERFORMANCE POR TIPO ===")
performance_tipo.show()


# Salvar todas as tabelas GOLD
resumo_clientes.write.mode("overwrite").parquet("/home/jovyan/data/gold/resumo_clientes")
performance_tipo.write.mode("overwrite").parquet("/home/jovyan/data/gold/performance_tipo")
analise_temporal.write.mode("overwrite").parquet("/home/jovyan/data/gold/analise_temporal")

print("✅ Tabelas GOLD salvas!")
print("📁 /data/gold/resumo_clientes/")
print("📁 /data/gold/performance_tipo/") 
print("📁 /data/gold/analise_temporal/")

# Verificar estrutura completa do Data Lake
def listar_arquivos(caminho):
    try:
        arquivos = os.listdir(caminho)
        return arquivos
    except:
        return []

print("🏗️ ESTRUTURA COMPLETA DO DATA LAKE")
print("="*50)
print("📁 RAW:", listar_arquivos('/home/jovyan/data/raw'))
print("📁 BRONZE:", listar_arquivos('/home/jovyan/data/bronze'))
print("📁 SILVER:", listar_arquivos('/home/jovyan/data/silver'))
print("📁 GOLD:", listar_arquivos('/home/jovyan/data/gold'))

# Estatísticas finais
print("\n📊 ESTATÍSTICAS FINAIS")
print("="*30)
print(f"Total registros processados: {df_transacoes_silver.count():,}")
print(f"Clientes únicos: {df_clientes_silver.count():,}")
print(f"Volume financeiro: R$ {df_transacoes_silver.filter(col('status') == 'Aprovada').agg(sum('valor')).collect()[0][0]:,.2f}")

spark.stop()
print("\n✅ Data Lake Financeiro concluído!")

