import streamlit as st
import math

st.set_page_config(
    page_title="Calculadora de Etiquetas",
    page_icon="📦",
    layout="centered"
)

st.title("📦 Calculadora de Etiquetas")

# ==========================
# MATERIALES
# ==========================

materiales = {
    "Transferencia Directa": {
        "ancho": 11,
        "largo": 1500,
        "precio": 0.51
    }
}

material_seleccionado = st.selectbox(
    "Selecciona el material",
    list(materiales.keys())
)

material = materiales[material_seleccionado]

# ==========================
# ETIQUETAS
# ==========================

etiquetas = {
    "102x51": {
        "ancho": 102,
        "largo": 51,
        "separacion": 1
    }
}

etiqueta_seleccionada = st.selectbox(
    "Selecciona la etiqueta",
    list(etiquetas.keys())
)

etiqueta = etiquetas[etiqueta_seleccionada]

# ==========================
# VENTAS
# ==========================

st.subheader("💰 Datos de Venta")

millares = st.number_input(
    "Millares vendidos",
    min_value=0.0,
    value=670.0
)

facturacion = st.number_input(
    "Facturación total (MXN)",
    min_value=0.0,
    value=970000.0
)

tipo_cambio = st.number_input(
    "Tipo de cambio (MXN por USD)",
    min_value=0.01,
    value=19.0
)

# ==========================
# CALCULO
# ==========================

if st.button("📊 Calcular"):

    ancho_material = material["ancho"]
    largo_material = material["largo"]
    precio_m2 = material["precio"]

    ancho_etiqueta = etiqueta["ancho"]
    largo_etiqueta = etiqueta["largo"]
    separacion = etiqueta["separacion"]

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

    rollos_utilizados = (
        etiquetas_vendidas /
        etiquetas_por_rollo
    )

    area_rollo = (
        ancho_material / 100
    ) * largo_material

    area_consumida = (
        area_rollo *
        rollos_utilizados
    )

    costo_usd = (
        area_consumida *
        precio_m2
    )

    costo_mxn = (
        costo_usd *
        tipo_cambio
    )

    utilidad = (
        facturacion -
        costo_mxn
    )

    st.success("✅ Resultados")

    st.write(
        f"📦 Material: {material_seleccionado}"
    )

    st.write(
        f"🏷️ Etiqueta: {etiqueta_seleccionada}"
    )

    st.write(
        f"🏷️ Etiquetas vendidas: {etiquetas_vendidas:,.0f}"
    )

    st.write(
        f"📦 Etiquetas por rollo: {etiquetas_por_rollo:,.0f}"
    )

    st.write(
        f"📦 Rollos utilizados: {rollos_utilizados:.2f}"
    )

    st.write(
        f"📐 Área consumida: {area_consumida:,.2f} m²"
    )

    st.write(
        f"💵 Costo material USD: ${costo_usd:,.2f}"
    )

    st.write(
        f"💰 Costo material MXN: ${costo_mxn:,.2f}"
    )

    st.write(
        f"🧾 Facturación: ${facturacion:,.2f}"
    )

    st.write(
        f"📈 Ganancia neta: ${utilidad:,.2f}"
    )
