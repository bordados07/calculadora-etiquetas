import streamlit as st
import math

st.set_page_config(
    page_title="Calculadora de Etiquetas",
    page_icon="📦",
    layout="centered"
)

st.title("📦 Calculadora Mensual de Etiquetas")

# ==================================
# MATERIALES
# ==================================

materiales = {
    "Transferencia Directa": {
        "ancho": 11,
        "largo": 1500,
        "precio": 0.51
    }
}

# ==================================
# ETIQUETAS
# ==================================

etiquetas = {
    "102x51": {
        "ancho": 102,
        "largo": 51,
        "separacion": 1
    }
}

# ==================================
# CONFIGURACIÓN GENERAL
# ==================================

st.subheader("⚙️ Configuración")

tipo_cambio = st.number_input(
    "Tipo de cambio (MXN por USD)",
    min_value=0.01,
    value=19.0
)

cantidad_pedidos = st.number_input(
    "Cantidad de pedidos",
    min_value=1,
    value=1,
    step=1
)

# ==================================
# ACUMULADORES
# ==================================

total_etiquetas = 0
total_facturacion = 0
total_area = 0
total_rollos = 0
total_costo_usd = 0

# ==================================
# PEDIDOS
# ==================================

for i in range(int(cantidad_pedidos)):

    st.markdown("---")
    st.subheader(f"📋 Pedido {i+1}")

    material_seleccionado = st.selectbox(
        "Material",
        list(materiales.keys()),
        key=f"mat_{i}"
    )

    etiqueta_seleccionada = st.selectbox(
        "Etiqueta",
        list(etiquetas.keys()),
        key=f"eti_{i}"
    )

    millares = st.number_input(
        "Millares vendidos",
        min_value=0.0,
        value=0.0,
        key=f"mil_{i}"
    )

    facturacion = st.number_input(
        "Facturación (MXN)",
        min_value=0.0,
        value=0.0,
        key=f"fac_{i}"
    )

    material = materiales[material_seleccionado]
    etiqueta = etiquetas[etiqueta_seleccionada]

    etiquetas_vendidas = millares * 1000

    ancho_material = material["ancho"]
    largo_material = material["largo"]
    precio_m2 = material["precio"]

    ancho_etiqueta = etiqueta["ancho"]
    largo_etiqueta = etiqueta["largo"]
    separacion = etiqueta["separacion"]

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

    etiquetas_por_rollo = (
        etiquetas_por_fila * filas
    )

    rollos_utilizados = (
        etiquetas_vendidas /
        etiquetas_por_rollo
        if etiquetas_por_rollo > 0 else 0
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

    total_etiquetas += etiquetas_vendidas
    total_facturacion += facturacion
    total_area += area_consumida
    total_rollos += rollos_utilizados
    total_costo_usd += costo_usd

# ==================================
# RESULTADO FINAL
# ==================================

if st.button("📊 Calcular Mes"):

    costo_mxn = total_costo_usd * tipo_cambio

    utilidad = (
        total_facturacion -
        costo_mxn
    )

    st.markdown("---")
    st.header("📈 Resultado Mensual")

    st.write(
        f"📋 Total de pedidos: {cantidad_pedidos}"
    )

    st.write(
        f"🏷️ Total etiquetas vendidas: {total_etiquetas:,.0f}"
    )

    st.write(
        f"📦 Rollos utilizados: {total_rollos:.2f}"
    )

    st.write(
        f"📐 Área consumida: {total_area:,.2f} m²"
    )

    st.write(
        f"💵 Costo material USD: ${total_costo_usd:,.2f}"
    )

    st.write(
        f"💰 Costo material MXN: ${costo_mxn:,.2f}"
    )

    st.write(
        f"🧾 Facturación total: ${total_facturacion:,.2f}"
    )

    st.write(
        f"📈 Ganancia neta: ${utilidad:,.2f}"
    )
