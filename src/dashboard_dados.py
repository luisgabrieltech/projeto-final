import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/processed/acidentes_tratado.csv")

# Gráfico 1: Causas de Acidentes
causas_df = df["causa_acidente"].value_counts().reset_index()
causas_df.columns = ["Causa", "Quantidade"]
causas_df = causas_df[causas_df["Quantidade"] >= 50]  # Filtra causas com >= 50 ocorrências
fig_causa = px.bar(causas_df, x="Causa", y="Quantidade", title="Principais Causas de Acidentes (≥ 50 casos)", template="plotly_white")
fig_causa.update_layout(xaxis_tickangle=-60, height=400)

# Gráfico 2: Acidentes por Estado
uf_df = df["uf"].value_counts().reset_index()
uf_df.columns = ["UF", "Quantidade"]
fig_uf = px.bar(uf_df, x="UF", y="Quantidade", title="Acidentes por Estado (UF)", template="plotly_white")
fig_uf.update_layout(height=400)

# Gráfico 3: Distribuição por Hora
hora_df = df["hora"].value_counts().sort_index().reset_index()
hora_df.columns = ["Hora", "Quantidade"]
fig_hora = px.bar(hora_df, x="Hora", y="Quantidade", title="Distribuição de Acidentes por Hora", template="plotly_white")
fig_hora.update_layout(height=400)

# Gráfico 4: Tipo de Acidente
tipo_df = df["tipo_acidente"].value_counts().reset_index()
tipo_df.columns = ["Tipo de Acidente", "Quantidade"]
fig_tipo = px.bar(tipo_df, x="Tipo de Acidente", y="Quantidade", title="Distribuição por Tipo de Acidente", template="plotly_white")
fig_tipo.update_layout(xaxis_tickangle=-45, height=400)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard Acidentes"

app.layout = dbc.Container([
    html.H1("📊 Painel Interativo de Acidentes de Trânsito", className="text-center my-4"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Causas"),
            dbc.CardBody(dcc.Graph(figure=fig_causa))
        ]), md=6),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Por Estado (UF)"),
            dbc.CardBody(dcc.Graph(figure=fig_uf))
        ]), md=6)
    ]),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Distribuição por Hora"),
            dbc.CardBody(dcc.Graph(figure=fig_hora))
        ]), md=6),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Tipos de Acidente"),
            dbc.CardBody(dcc.Graph(figure=fig_tipo))
        ]), md=6)
    ], className="mt-4")
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)