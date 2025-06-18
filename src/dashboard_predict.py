import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

model = joblib.load("models/model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")
target_encoder = joblib.load("models/target_encoder.pkl")

st.set_page_config(page_title="Prevenção de Acidentes", layout="centered")

st.title("🚧 Previsão de Tipo de Acidente")
st.write("Insira os dados abaixo para prever o tipo de acidente:")

uf = st.selectbox("UF", sorted(label_encoders["uf"].classes_))
br = st.number_input("Rodovia (BR)", min_value=0, max_value=999, value=101)
hora = st.slider("Hora do dia", 0, 23, 14)
clima = st.selectbox("Condição Meteorológica", sorted(label_encoders["condicao_metereologica"].classes_))
causa = st.selectbox("Causa Provável", sorted(label_encoders["causa_acidente"].classes_))
data = st.date_input("Data do acidente", value=datetime.today())

if st.button("Prever Tipo de Acidente"):
    df = pd.DataFrame([{
        "hora": hora,
        "uf": uf,
        "br": br,
        "condicao_metereologica": clima,
        "causa_acidente": causa,
        "data": str(data)
    }])

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

    st.success(f"✅ Tipo de acidente previsto: **{classe}**")