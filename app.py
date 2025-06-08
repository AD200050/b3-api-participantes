import streamlit as st
import requests
import pandas as pd

st.title("📊 Posição por Participante – Dólar e Índice (via API)")

# Pegando a chave secreta
api_key = st.secrets["API_KEY"]

# Construindo URL da API
url = f"https://api.dadosdemercado.com.br/fluxo?token={api_key}&produtos=futuros_dolar,futuros_indice&tipo=participante"

try:
    r = requests.get(url)
    r.raise_for_status()
    df = pd.DataFrame(r.json())

    for prod in ["futuros_dolar", "futuros_indice"]:
        st.header(prod.replace("_", " ").upper())
        df_filtrado = df[df["produto"] == prod][["data", "tipo_participante", "pos_compradas", "pos_vendidas", "pos_liquida"]]
        st.dataframe(df_filtrado)

except Exception as e:
    st.error("Erro ao acessar os dados da API.")
    st.text(str(e))

