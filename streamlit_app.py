
import streamlit as st
import pandas as pd
from datetime import datetime

# Aumentos extraídos del Excel (2014 a 2025)
AUMENTOS = [
    ("2020-03", "fijo", 1500),
    ("2020-03", "porc", 2.3),
    ("2020-06", "porc", 6.12),
    ("2020-09", "porc", 7.5),
    ("2020-12", "porc", 5.0),
    ("2021-03", "porc", 8.07),
    ("2021-06", "porc", 12.12),
    ("2021-09", "porc", 12.39),
    ("2021-12", "porc", 12.11),
    ("2022-03", "porc", 12.28),
    ("2022-06", "porc", 15.0),
    ("2022-09", "porc", 15.53),
    ("2022-12", "porc", 15.62),
    ("2023-03", "porc", 17.04),
    ("2023-06", "porc", 20.92),
    ("2023-09", "porc", 23.29),
    ("2023-12", "porc", 20.87),
    ("2024-03", "porc", 27.4),
    ("2024-06", "porc", 41.48),
]

df = pd.DataFrame(AUMENTOS, columns=["fecha", "tipo", "valor"])
df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m")

st.title("Calculadora – Retrotraer Haber Previsional")

haber_final = st.number_input("Importe conocido", value=53036.00, format="%.2f")
fecha_conocida = st.text_input("Fecha del haber (YYYY‑MM)", "2022-11")
fecha_retro = st.text_input("Retrotraer a fecha (YYYY‑MM)", "2022-01")

try:
    fecha_conocida_dt = datetime.strptime(fecha_conocida, "%Y-%m")
    fecha_retro_dt = datetime.strptime(fecha_retro, "%Y-%m")

    if st.button("Calcular"):
        df_tramo = df[(df["fecha"] > fecha_retro_dt) & (df["fecha"] <= fecha_conocida_dt)]
        factor = 1.0
        for _, row in df_tramo.iterrows():
            if row.tipo == "porc":
                factor *= 1 + row.valor / 100
            else:
                factor *= 1 + row.valor / haber_final
        haber_retro = haber_final / factor
        st.write(f"**Haber retrotraído:** ${haber_retro:,.2f}")
        if any(df_tramo["fecha"] == pd.to_datetime("2020-03")):
            st.warning("⚠ Marzo 2020 aplicado como $1500 + 2,3%")
except ValueError:
    st.error("⚠ Ingresá las fechas en formato YYYY-MM (ejemplo: 2022-11)")
