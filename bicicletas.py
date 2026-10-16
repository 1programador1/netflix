import streamlit as st
import pandas as pd

st.title("Mapa de Bicicletas")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/1programador1/netflix/refs/heads/main/citibike-tripdata.csv" 
    
    try:
        df = pd.read_csv(url)
        # Convertimos la columna de fecha/hora para poder extraer la hora más adelante
        if 'started_at' in df.columns:
            df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce')
        return df
    except Exception as e:
        st.warning(f"Por favor, ingresa un enlace válido. Error: {e}")
        # Datos de prueba actualizados con coordenadas para que el mapa funcione si falla el link
        return pd.DataFrame({
            "ride_id": ["228F2E2FEBFBF843", "DCDBD0A5178BAB5", "DD7AD7B81588187B"],
            "rideable_type": ["classic_bike", "classic_bike", "docked_bike"],
            "started_at": pd.to_datetime(["2021-09-11 16:03:10", "2021-09-14 17:27:50", "2021-09-04 20:29:34"]),
            "start_station_name": ["Jersey & 6th St", "Jersey & 6th St", "12 St & Sinatra Dr N"],
            "start_lat": [40.719282, 40.719282, 40.740113],
            "start_lng": [-74.043117, -74.043117, -74.028913]
        })

data = load_data()

# Barra lateral
view_raw_data = st.sidebar.checkbox("View RAW data")
recorridos_por_hora = st.sidebar.checkbox("Recorridos por hora")
mapa = st.sidebar.checkbox("Mapa")

# Lógica de las opciones
if view_raw_data:
    st.dataframe(data)

if recorridos_por_hora:
    st.subheader("Recorridos por hora")
    if 'started_at' in data.columns:
        # Extraemos la hora, contamos cuántos viajes hay en cada hora y ordenamos
        recorridos = data['started_at'].dt.hour.value_counts().sort_index()
        st.bar_chart(recorridos)
    else:
        st.write("El archivo no tiene la columna 'started_at' para calcular las horas.")

if mapa:
    st.subheader("Mapa de recorridos")
    # Streamlit necesita que las columnas se llamen 'lat' y 'lon' para st.map()
    if 'start_lat' in data.columns and 'start_lng' in data.columns:
        datos_mapa = data[['start_lat', 'start_lng']].dropna()
        datos_mapa = datos_mapa.rename(columns={'start_lat': 'lat', 'start_lng': 'lon'})
        st.map(datos_mapa)
    else:
        st.write("El archivo no contiene las columnas de coordenadas ('start_lat', 'start_lng').")

# Integrantes del equipo
st.write("---") 
st.markdown("### Integrantes del equipo")
st.write("Enrique Ginez Sandoval")
st.write("Alvaro Eli Sanchez Larrazabal")
st.write("Daniela Rojas Vázquez")
st.write("Gustavo daniel cuevas baez")