# Data Lake Financeiro — Pipeline ETL com PySpark

Projeto de engenharia e análise de dados financeiros utilizando **Python, Pandas e Apache Spark**, com organização dos dados em camadas RAW, Bronze, Silver e Gold.

## 1. Problema de negócio

Uma operação financeira que processa milhares de transações precisa transformar registros brutos em informações confiáveis para acompanhar seu desempenho.

Sem um processo estruturado de tratamento e consolidação, torna-se difícil responder a perguntas como:

- Qual o volume financeiro movimentado?
- Quais modalidades concentram mais transações?
- Como as transações aprovadas e negadas se distribuem?
- Qual o ticket médio por cliente?
- Como o volume transacionado varia ao longo do tempo?

**Objetivo:** construir um pipeline ETL que organize, trate e agregue dados financeiros para apoiar análises operacionais e decisões de negócio.

## 2. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento dos scripts |
| Pandas | Geração e exportação dos dados sintéticos |
| PySpark 4.1.1 | Processamento, transformação e agregação |
| Apache Parquet | Armazenamento das camadas processadas |
| Git e GitHub | Versionamento e documentação |
| GitHub Codespaces | Ambiente de desenvolvimento e testes |

## 3. Arquitetura do pipeline

```text
RAW
  |
  v
BRONZE
  |
  v
SILVER
  |
  v
GOLD
```

**RAW — Dados brutos**

Geração de duas bases sintéticas:
- 10.000 clientes em CSV.
- 50.000 transações financeiras em JSON Lines.

**BRONZE — Limpeza e padronização**

- Conversão de tipos de dados.
- Remoção de registros inválidos conforme regras implementadas.
- Tratamento de identificadores duplicados.
- Gravação em Parquet.

**SILVER — Enriquecimento**

- Cálculo da idade dos clientes.
- Classificação por faixa etária.
- Segmentação por renda.
- Integração de clientes e transações.
- Criação de indicadores temporais.

**GOLD — Indicadores de negócio**

Geração de três conjuntos analíticos:

1. **Resumo por cliente:** quantidade de transações aprovadas, valor movimentado e ticket médio.
2. **Performance por modalidade:** quantidade e valor financeiro por tipo e status de transação.
3. **Análise temporal:** quantidade de transações aprovadas e valores movimentados por mês e período do dia.

## 4. Estrutura do repositório

```text
data-lake-financeiro/
├── scripts/
│   ├── gerar_clientes.py
│   ├── gerar_transacoes.py
│   └── processamento_spark.py
├── .gitignore
├── requirements.txt
└── README.md
```

Os arquivos de dados são gerados durante a execução e não são versionados no repositório.

## 5. Como executar

O projeto foi testado no GitHub Codespaces, utilizando Python 3.14.2, Java 21 e PySpark 4.1.1.

**Pré-requisitos:** Python, Java 21 e pip disponíveis no ambiente.

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Gere as bases sintéticas:

```bash
python scripts/gerar_transacoes.py
```

Execute o processamento:

```bash
python scripts/processamento_spark.py
```

Os resultados serão armazenados automaticamente nas pastas locais `data/bronze`, `data/silver` e `data/gold`, em formato Parquet.

## 6. Resultados dos testes

O pipeline foi executado no GitHub Codespaces com os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Clientes gerados | 10.000 |
| Transações geradas | 50.000 |
| Total de registros de entrada | 60.000 |
| IDs de transações duplicados no teste | 0 |
| Transações com clientes inexistentes no teste | 0 |
| Transações com valor menor ou igual a zero no teste | 0 |
| Clientes processados pelo Spark | 10.000 |
| Transações processadas pelo Spark | 50.000 |

As etapas RAW, Bronze, Silver e Gold foram executadas com sucesso, incluindo a gravação dos conjuntos analíticos em Parquet.

Esses testes verificaram a execução e algumas regras básicas de integridade. Eles não representam uma validação de produção.

## 7. Aplicação para o negócio

O pipeline disponibiliza dados consolidados que podem apoiar análises de:

- Volume e valor financeiro das transações.
- Desempenho das modalidades PIX, TED, DOC, cartões e saques.
- Distribuição entre transações aprovadas e negadas.
- Comportamento das movimentações por período.
- Atividade financeira individual dos clientes.

A camada Gold oferece uma base estruturada para relatórios, análises exploratórias e futuros dashboards.

## 8. Limitações

Este projeto utiliza **dados integralmente sintéticos**, gerados para fins educacionais e de demonstração técnica.

Os valores e padrões financeiros não representam uma instituição real.

O processamento foi testado em ambiente local do Spark dentro do Codespaces, não em um cluster distribuído de produção.

## 9. Autor

**Rubens Martins**

Estudante de Tecnologia em Banco de Dados, com foco em Análise de Dados, SQL, Python e Business Intelligence.

[GitHub](https://github.com/Rubens-Martins-Dev) | [LinkedIn](https://www.linkedin.com/in/rubens-martins-084b97307/)
