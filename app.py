import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Etiquetas", layout="centered")

st.title("📦 Calculadora de Etiquetas")

st.subheader("Material")

ancho_material = st.number_input(
    "Ancho del material (cm)",
    value=11.0
)

largo_material = st.number_input(
    "Largo del material (m)",
    value=1500.0
)

precio_m2 = st.number_input(
    "Costo por m² (USD)",
    value=0.51
)

tipo_cambio = st.number_input(
    "Tipo de cambio (MXN por USD)",
    value=19.0
)

st.subheader("Etiqueta")

ancho_etiqueta = st.number_input(
    "Ancho etiqueta (mm)",
    value=102.0
)

largo_etiqueta = st.number_input(
    "Largo etiqueta (mm)",
    value=51.0
)

separacion = st.number_input(
    "Separación entre etiquetas (mm)",
    value=1.0
)

st.subheader("Ventas")

millares = st.number_input(
    "Millares vendidos",
    value=670
)

facturacion = st.number_input(
    "Facturación total (MXN)",
    value=970000.0
)

if st.button("Calcular"):

    etiquetas_vendidas = millares * 1000

    ancho_material_mm = ancho_material * 10

    etiquetas_por_fila = max(
        1,
        math.floor(ancho_material_mm / ancho_etiqueta)
    )

    avance = largo_etiqueta + separacion

    largo_material_mm = largo_material * 1000

    filas = math.floor(
        largo_material_mm / avance
    )

    etiquetas_por_rollo = etiquetas_por_fila * filas

    rollos_utilizados = etiquetas_vendidas / etiquetas_por_rollo

    area_rollo = (ancho_material / 100) * largo_material

    area_consumida = area_rollo * rollos_utilizados

    costo_usd = area_consumida * precio_m2

    costo_mxn = costo_usd * tipo_cambio

    utilidad = facturacion - costo_mxn

    st.success("Resultados")

    st.write(f"🏷️ Etiquetas vendidas: {etiquetas_vendidas:,.0f}")

    st.write(f"📦 Etiquetas por rollo: {etiquetas_por_rollo:,.0f}")

    st.write(f"📦 Rollos utilizados: {rollos_utilizados:.2f}")

    st.write(f"📐 Área consumida: {area_consumida:,.2f} m²")

    st.write(f"💵 Costo material USD: ${costo_usd:,.2f}")

    st.write(f"💰 Costo material MXN: ${costo_mxn:,.2f}")

    st.write(f"🧾 Facturación: ${facturacion:,.2f}")

    st.write(f"📈 Ganancia neta: ${utilidad:,.2f}")
