import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

csv_path = "output.csv"
df = pd.read_csv(csv_path)

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")

df_sorted = df.sort_values(by="Rank", ascending=False)

st.title("Ranking de Jugadores CHIFRIJO RAIDERS")

if st.toggle("Mostrar tabla de datos"):
    st.dataframe(df_sorted)

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

fig.update_traces(
    textposition="inside",
    insidetextanchor="end",
    textfont=dict(size=20, color="white")
)

altura_grafico = len(df_sorted) * 40 + 100


fig.update_layout(
    yaxis=dict(autorange="reversed"),
    showlegend=False,
    height=altura_grafico
)

fig.add_shape(
    type="line",
    x0=2500, x1=2500,
    y0=-0.5, y1=len(df_sorted) - 0.5,
    line=dict(color="gray", width=2, dash="dash"),
    xref="x", yref="y"
)


fig.add_annotation(
    x=2500,
    y=-0.5,
    text="Umbral 2500",
    showarrow=False,
    yshift=-10,
    font=dict(color="gray")
)

st.plotly_chart(fig, use_container_width=True)

last_updated = datetime.fromtimestamp(os.path.getmtime(csv_path)).strftime("%d/%m/%Y %H:%M:%S")
st.markdown(
    f"""
    <div style='position: fixed; bottom: 10px; left: 10px; font-size: 12px; color: gray;'>
        Última actualización del archivo: {last_updated}
    </div>
    """,
    unsafe_allow_html=True
)
