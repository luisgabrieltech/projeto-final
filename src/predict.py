import pandas as pd
import joblib
import os

model = joblib.load("models/model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")
target_encoder = joblib.load("models/target_encoder.pkl")

def prever_acidente(entrada: dict):
    df = pd.DataFrame([entrada])

    df["periodo_dia"] = pd.cut(
        df["hora"],
        bins=[-1, 6, 12, 18, 24],
        labels=["Madrugada", "Manhã", "Tarde", "Noite"]
    ).astype(str)

    df["data"] = pd.to_datetime(df["data"])
    df["dia_semana"] = df["data"].dt.day_name()

    features = ["hora", "uf", "br", "condicao_metereologica", "causa_acidente", "periodo_dia", "dia_semana"]
    X = df[features].copy()

    for col in X.columns:
        if col in label_encoders:
            X[col] = label_encoders[col].transform(X[col])

    y_pred = model.predict(X)
    classe = target_encoder.inverse_transform(y_pred)[0]
    return classe