# 🏦 Data Lake Financeiro com Apache Spark e Docker

## 📋 Sobre o Projeto

Projeto completo de **Data Lake** para análise de dados financeiros, implementando arquitetura moderna de Big Data com **Apache Spark**, **PySpark**, **Docker** e **Jupyter Notebook**.

### 🎯 Objetivos
- Construir pipeline de ETL escalável
- Implementar arquitetura de dados em camadas
- Processar dados financeiros com Spark
- Gerar insights para tomada de decisão

## 🏗️ Arquitetura

```
Data Lake Financeiro
├── RAW Layer      → Dados brutos (CSV, JSON)
├── BRONZE Layer   → Dados limpos e tipados
├── SILVER Layer   → Dados transformados e enriquecidos
└── GOLD Layer     → Dados agregados para análise
```

## 🛠️ Tecnologias Utilizadas

- **Apache Spark 3.4+** - Processamento distribuído
- **PySpark** - Interface Python para Spark
- **Docker** - Containerização
- **Jupyter Notebook** - Desenvolvimento interativo
- **Pandas** - Manipulação de dados
- **Python** - Linguagem principal

## 📊 Dados Gerados

### Clientes (10.000 registros)
- **Informações pessoais**: Nome, CPF, idade
- **Dados financeiros**: Renda, score de crédito
- **Segmentação**: Faixa etária, classe de renda

### Transações (50.000+ registros)
- **Tipos**: PIX, TED, DOC, Cartões, Saques
- **Métricas**: Valores, status, canais
- **Análise temporal**: Período do dia, dia da semana

## 🚀 Como Executar

### Pré-requisitos
- Docker Desktop instalado
- Git (para clonar o repositório)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/Rubens-Martins-Dev/data-lake-financeiro.git
cd data-lake-financeiro
```

2. **Inicie o container Docker**
```bash
docker run -d -p 8888:8888 --name jupyter-spark jupyter/pyspark-notebook
```

3. **Acesse o Jupyter Lab**
```bash
# Obter token de acesso
docker logs jupyter-spark

# Acesse: http://localhost:8888 (com o token)
```

4. **Execute os notebooks na ordem**
- `01_gerador_dados_financeiros.ipynb`
- `02_processamento_spark.ipynb`

## 📁 Estrutura do Projeto

```
data-lake-financeiro/
├── notebooks/
│   ├── 01_gerador_dados_financeiros.ipynb
│   └── 02_processamento_spark.ipynb
├── data/
│   ├── raw/           # Dados originais
│   ├── bronze/        # Dados limpos
│   ├── silver/        # Dados transformados
│   └── gold/          # Dados para análise
├── scripts/           # Scripts Python auxiliares
├── docker-compose.yml # Configuração Docker
└── README.md         # Este arquivo
```

## 🔄 Pipeline ETL

### 1. RAW Layer
- **Clientes**: CSV com dados pessoais e financeiros
- **Transações**: JSON com movimentações bancárias

### 2. BRONZE Layer
- Limpeza de dados nulos
- Tipagem correta dos campos
- Validações básicas
- Formato Parquet para otimização

### 3. SILVER Layer
- Enriquecimento com cálculos derivados
- Join entre clientes e transações
- Categorização por faixas (idade, renda, valor)
- Análise temporal (período do dia, dia da semana)

### 4. GOLD Layer
- **Resumo por Cliente**: Total de transações, ticket médio
- **Performance por Tipo**: Análise por modalidade
- **Análise Temporal**: Sazonalidade e padrões

## 📈 Métricas e Insights

- **Volume Processado**: 60.000+ registros
- **Valor Transacionado**: R$ 50M+ simulados
- **Taxa de Aprovação**: ~75% das transações
- **Ticket Médio**: R$ 800-1.200 por transação

## 🔧 Configurações Spark

```python
spark = SparkSession.builder \
    .appName("DataLakeFinanceiro") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()
```
## 📝 Aprendizados

Este projeto demonstra:
- **Arquitetura de Big Data** em ambiente real
- **Processamento distribuído** com Apache Spark
- **Boas práticas** de ETL e Data Engineering
- **Containerização** com Docker
- **Modelagem dimensional** para analytics

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request.

## 📧 Contato

**[Rubens Martins]**
- LinkedIn: [https://www.linkedin.com/in/rubens-martins-084b97307/]
- Email: [rubensdev08@gmail.com]
- GitHub: [https://github.com/Rubens-Martins-Dev]

---
⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!
