import streamlit as st
import pandas as pd
st.title("hello world web")
st.write("hello world streamlit")

dataframe = pd.read_csv(
    "https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",
    encoding="latin-1"
)

st.dataframe(dataframe)