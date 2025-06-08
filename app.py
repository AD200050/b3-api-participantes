import streamlit as st
import requests
import pandas as pd

st.title("📊 Posição por Participante – Dólar e Índice (via API)")

api_key = st.secrets["API_KEY"]  # opção segura
url = f"https://api.dadosdemercado.com.br/fluxo?token={api_key}&produtos=futuros_dolar,futuros_indice&tipo=participante"
r = requests.get(url)
df = pd.DataFrame(r.json())

for prod in ["futuros_dolar", "futuros_indice"]:
    st.header(prod.replace("_", " ").upper())
    st.dataframe(df[df["produto"] == prod][["data", "tipo_participante", "pos_compradas", "pos_vendidas", "pos_liquida"]])
