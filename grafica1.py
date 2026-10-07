import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

movies_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv", encoding='latin1') 

st.dataframe(movies_data)
st.header("Data Description")

fig, ax = plt.subplots()
ax.hist(movies_data['budget'])

st.header("Histograma de Presupuestos")
st.pyplot(fig)