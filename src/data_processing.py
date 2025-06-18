from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
import os

spark = SparkSession.builder.appName("ProcessamentoAcidentesPRF").getOrCreate()

INPUT_PATH = "data/raw/acidentes.csv"
OUTPUT_PATH = "data/processed/acidentes_tratado.csv"

os.makedirs("data/processed", exist_ok=True)

df = spark.read.csv(INPUT_PATH, header=True, sep=";", encoding="iso-8859-1")

colunas_interesse = [
    "data_inversa", "horario", "br", "km", "municipio", 
    "uf", "tipo_acidente", "causa_acidente", "condicao_metereologica"
]

df_filtrado = df.select(*[col(c) for c in colunas_interesse if c in df.columns])

if "data_inversa" in df_filtrado.columns:
    df_filtrado = df_filtrado.withColumn("data", to_timestamp(col("data_inversa"), "yyyy-MM-dd"))

if "horario" in df_filtrado.columns:
    df_filtrado = df_filtrado.withColumn("hora", col("horario").substr(1, 2).cast("int"))

df_filtrado.toPandas().to_csv(OUTPUT_PATH, index=False)
print(f"[INFO] Dados tratados salvos em: {OUTPUT_PATH}")