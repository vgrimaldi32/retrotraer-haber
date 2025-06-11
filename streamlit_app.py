
import streamlit as st
import pandas as pd

AUMENTOS = [
    ("2020-03", "fijo", 1500),
    ("2020-03", "porc", 2.3),
    ("2014-09", "porc", 0.1721),
    ("2015-03", "porc", 0.1826),
    ("2015-09", "porc", 0.1449),
    ("2016-03", "porc", 0.1535),
    ("2016-09", "porc", 0.1416),
    ("2017-03", "porc", 0.1296),
    ("2017-09", "porc", 0.1332),
    ("2018-03", "porc", 0.0571),
    ("2018-06", "porc", 0.056900000000000006),
    ("2018-09", "porc", 0.0667),
    ("2018-12", "porc", 0.07780000000000001),
    ("2019-03", "porc", 0.1183),
    ("2019-06", "porc", 0.1074),
    ("2019-09", "porc", 0.1222),
    ("2019-12", "porc", 0.0874),
    ("2020-03", "porc", 2.3),
    ("2020-06", "porc", 0.061200000000000004),
    ("2020-09", "porc", 0.075),
    ("2020-12", "porc", 0.05),
    ("2021-03", "porc", 0.0807),
    ("2021-06", "porc", 0.12119999999999999),
    ("2021-09", "porc", 0.12390000000000001),
    ("2021-12", "porc", 0.1211),
    ("2022-03", "porc", 0.12279999999999999),
    ("2022-06", "porc", 0.15),
    ("2022-09", "porc", 0.1553),
    ("2022-12", "porc", 0.1562),
    ("2023-03", "porc", 0.1704),
    ("2023-06", "porc", 0.20920000000000002),
    ("2023-09", "porc", 0.2329),
    ("2023-12", "porc", 0.2087),
    ("2024-03", "porc", 0.2718),
    ("2024-04", "porc", 0.274),
    ("2024-05", "porc", 0.1101),
    ("2024-06", "porc", 0.0883),
    ("2024-07", "porc", 0.0418),
    ("2024-08", "porc", 0.0458),
    ("2024-09", "porc", 0.04),
    ("2024-10", "porc", 0.0417),
    ("2024-11", "porc", 0.0347),
    ("2024-12", "porc", 0.01027),
    ("2025-01", "porc", 0.0243),
    ("2025-02", "porc", 0.027),
    ("2025-03", "porc", 0.022099999999999998),
    ("2025-04", "porc", 0.024),
    ("2025-05", "porc", 0.0373),
    ("2025-06", "porc", 0.0278)
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
