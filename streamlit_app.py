
import streamlit as st
import pandas as pd

# Aumentos de movilidad previsional
AUMENTOS = [
    ("2020-03", "fijo", 1500),
    ("2020-03", "porc", 2.3),
    ("2020-06", "porc", 6.12),
    ("2020-09", "porc", 7.5),
    # Agregá más aumentos acá si querés
]

df = pd.DataFrame(AUMENTOS, columns=["fecha","tipo","valor"]).sort_values("fecha")

st.title("Calculadora – Retrotraer Haber Previsional")

haber_final = st.number_input("Importe conocido", value=49731.81, format="%.2f")
fecha_conocida = st.text_input("Fecha del haber (YYYY‑MM)", "2020-10")
fecha_retro = st.text_input("Retrotraer a fecha (YYYY‑MM)", "2020-04")

if st.button("Calcular"):
    df_tramo = df[(df["fecha"] > fecha_retro) & (df["fecha"] <= fecha_conocida)]
    factor = 1.0
    for _, row in df_tramo.iterrows():
        if row.tipo == "porc":
            factor *= 1 + row.valor / 100
        else:
            factor *= 1 + row.valor / haber_final
    haber_retro = haber_final / factor
    st.write(f"**Haber retrotraído:** ${haber_retro:,.2f}")
    if any(df_tramo["fecha"] == "2020-03"):
        st.warning("⚠ Marzo 2020 aplicado como $1500 + 2,3%")
