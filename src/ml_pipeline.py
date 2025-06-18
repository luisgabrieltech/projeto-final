import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/processed/acidentes_tratado.csv")

grupo_acidente = {
    "Colisão frontal": "Colisão",
    "Colisão traseira": "Colisão",
    "Colisão com objeto": "Colisão",
    "Colisão lateral mesmo sentido": "Colisão",
    "Colisão lateral sentido oposto": "Colisão",
    "Colisão transversal": "Colisão",
    "Atropelamento de Animal": "Atropelamento",
    "Atropelamento de Pedestre": "Atropelamento",
    "Capotamento": "Capotamento/Tombamento",
    "Tombamento": "Capotamento/Tombamento",
    "Eventos atípicos": "Outros",
    "Sinistro pessoal de trânsito": "Outros",
    "Derramamento de carga": "Outros",
    "Queda de ocupante de veículo": "Outros",
    "Engavetamento": "Colisão",
    "Incêndio": "Outros",
    "Saída de leito carroçável": "Outros"
}
df["grupo_acidente"] = df["tipo_acidente"].map(grupo_acidente)

df["periodo_dia"] = pd.cut(
    df["hora"],
    bins=[-1, 6, 12, 18, 24],
    labels=["Madrugada", "Manhã", "Tarde", "Noite"]
)
df["periodo_dia"] = df["periodo_dia"].astype(str)
df["data"] = pd.to_datetime(df["data"])
df["dia_semana"] = df["data"].dt.day_name()

features = ["hora", "uf", "br", "condicao_metereologica", "causa_acidente", "periodo_dia", "dia_semana"]
target = "grupo_acidente"
X = df[features].copy()
y = df[target].copy()

label_encoders = {}
for col in X.columns:
    if X[col].dtype.name == "category" or X[col].dtype == object:
        X[col] = X[col].astype(str)
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        label_encoders[col] = le

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
model = XGBClassifier(
    use_label_encoder=False,
    eval_metric="mlogloss",
    random_state=42,
    n_estimators=70,
    max_depth=5,
    learning_rate=0.08
)
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
report = classification_report(
    y_test, y_pred,
    labels=list(range(len(target_encoder.classes_))),
    target_names=target_encoder.classes_,
    zero_division=0
)
matrix = confusion_matrix(y_test, y_pred)

joblib.dump(model, "models/model.pkl")
joblib.dump(label_encoders, "models/label_encoders.pkl")
joblib.dump(target_encoder, "models/target_encoder.pkl")
with open("models/classification_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("Modelo salvo em: models/model.pkl")
print("Relatório de classificação:")
print(report)