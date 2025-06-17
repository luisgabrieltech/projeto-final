from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
import os

# Inicializar Spark
spark = SparkSession.builder.appName("ProcessamentoAcidentesPRF").getOrCreate()

# Caminhos
INPUT_PATH = "data/raw/acidentes.csv"
OUTPUT_PATH = "data/processed/acidentes_tratado.csv"

# Garantir que diretório de saída existe
os.makedirs("data/processed", exist_ok=True)

# Ler o CSV original
df = spark.read.csv(INPUT_PATH, header=True, sep=";", encoding="iso-8859-1")

# Selecionar colunas de interesse (ajuste conforme o CSV real)
colunas_interesse = [
    "data_inversa", "horario", "br", "km", "municipio", 
    "uf", "tipo_acidente", "causa_acidente", "condicao_metereologica"
]

df_filtrado = df.select(*[col(c) for c in colunas_interesse if c in df.columns])

# Converter data/hora se existirem
if "data_inversa" in df_filtrado.columns:
    df_filtrado = df_filtrado.withColumn("data", to_timestamp(col("data_inversa"), "yyyy-MM-dd"))

if "horario" in df_filtrado.columns:
    df_filtrado = df_filtrado.withColumn("hora", col("horario").substr(1, 2).cast("int"))

# Salvar dados tratados
df_filtrado.toPandas().to_csv(OUTPUT_PATH, index=False)
print(f"[INFO] Dados tratados salvos em: {OUTPUT_PATH}")