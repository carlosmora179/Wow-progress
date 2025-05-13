import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# Cargar el archivo CSV
csv_path = "output.csv"
df = pd.read_csv(csv_path)

# Convertir fechas si existen
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")

# Ordenar por Rank descendente
df_sorted = df.sort_values(by="Rank", ascending=False)

# Título principal
st.title("Ranking de Jugadores CHIFRIJO RAIDERS")

# ✅ Mostrar tabla solo si se activa el botón
if st.toggle("Mostrar tabla de datos"):
    st.dataframe(df_sorted)

# Gráfico
st.subheader("Visualización del Ranking")
df_sorted["Color"] = df_sorted["Rank"].apply(lambda x: "purple" if x > 2500 else "red")

fig = px.bar(
    df_sorted,
    x="Rank",
    y="Nombre",
    orientation="h",
    color="Color",
    color_discrete_map={"purple": "purple", "red": "red"},
    text="Rank",
    title="Ranking de Jugadores"
)

# ✅ Aumentar el tamaño del texto en la gráfica
fig.update_traces(
    textposition='outside',
    textfont=dict(size=14, color="black")
)

fig.update_layout(
    yaxis=dict(autorange="reversed"),
    showlegend=False,
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# Mostrar fecha de última actualización
last_updated = datetime.fromtimestamp(os.path.getmtime(csv_path)).strftime("%d/%m/%Y %H:%M:%S")
st.markdown(
    f"""
    <div style='position: fixed; bottom: 10px; left: 10px; font-size: 12px; color: gray;'>
        Última actualización del archivo: {last_updated}
    </div>
    """,
    unsafe_allow_html=True
)
