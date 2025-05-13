import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV
df = pd.read_csv("output.csv")  # Asegurate que el archivo esté en la misma carpeta

# Convertir columna de fechas si es necesario
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")

# Ordenar por Rank descendente
df_sorted = df.sort_values(by="Rank", ascending=False)

# Mostrar tabla
st.title("Ranking de Jugadores desde CSV")
st.dataframe(df_sorted)

# Gráfico tipo ranking
st.subheader("Visualización del Ranking")
colores = ['purple' if rank > 2500 else 'red' for rank in df_sorted["Rank"]]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df_sorted["Nombre"], df_sorted["Rank"], color=colores)
ax.invert_yaxis()
ax.set_xlabel("Rank")
ax.set_title("Ranking de Jugadores")

for bar in bars:
    width = bar.get_width()
    ax.text(width + 20, bar.get_y() + bar.get_height()/2, f"{width:.1f}", va='center')

st.pyplot(fig)