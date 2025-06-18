from src.predict import prever_acidente

def test_prever_acidente_valido():
    entrada = {
        "hora": 15,
        "uf": "SP",
        "br": 116,
        "condicao_metereologica": "Céu Claro",
        "causa_acidente": "Reação tardia ou ineficiente do condutor",
        "data": "2025-06-15"
    }
    resultado = prever_acidente(entrada)
    assert resultado in ["Colisão", "Atropelamento", "Capotamento/Tombamento", "Outros"]

def test_prever_acidente_com_data_extrema():
    entrada = {
        "hora": 2,
        "uf": "PE",
        "br": 101,
        "condicao_metereologica": "Sol",
        "causa_acidente": "Reação tardia ou ineficiente do condutor",
        "data": "2020-01-01"
    }
    resultado = prever_acidente(entrada)
    assert isinstance(resultado, str)