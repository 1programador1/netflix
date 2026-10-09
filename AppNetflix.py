import streamlit as st
import pandas as pd

st.title("WikiNetflix")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv"
    df = pd.read_csv(url, encoding='latin1')
    return df

data = load_data()

st.sidebar.header("Netflix")

mostrar_todos = st.sidebar.checkbox("Mostrar todos los filmes")

titulo_filme = st.sidebar.text_input("Título del filme:")
btn_buscar = st.sidebar.button("Buscar filmes")

directores = data['director'].dropna().unique()
director_seleccionado = st.sidebar.selectbox("Seleccionar Director", directores)
btn_filtrar = st.sidebar.button("Filtrar director")

if btn_buscar and titulo_filme:
    filtro_titulo = data[data['name'].str.contains(titulo_filme, case=False, na=False)]
    st.dataframe(filtro_titulo)
elif btn_filtrar:
    filtro_director = data[data['director'] == director_seleccionado]
    st.dataframe(filtro_director)
elif mostrar_todos:
    st.dataframe(data)
else:
    st.write("Usa la barra lateral para buscar, filtrar directores o selecciona 'Mostrar todos los filmes'.")