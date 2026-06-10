import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Etiquetas", page_icon="📦", layout="centered")
st.title("📦 Calculadora Mensual de Etiquetas")

materiales = {
    "Transferencia Directa": {"ancho": 11, "largo": 1500, "precio": 0.51},
    "Termico Grande": {"ancho": 20, "largo": 1500, "precio": 0.51}
}

etiquetas_por_tipo = {
    "Rectangular": {
        "21x147": {"ancho": 21, "largo": 147},
        "22x148": {"ancho": 22, "largo": 148},
        "25x177": {"ancho": 25, "largo": 177},
        "29x141": {"ancho": 29, "largo": 141},
        "30x22": {"ancho": 30, "largo": 22},
        "32x24": {"ancho": 32, "largo": 24},
        "35x73": {"ancho": 35, "largo": 73},
        "36x236": {"ancho": 36, "largo": 236},
        "44x25": {"ancho": 44, "largo": 25},
        "45x180": {"ancho": 45, "largo": 180},
        "47x53": {"ancho": 47, "largo": 53},
        "50x32": {"ancho": 50, "largo": 32},
        "51x25": {"ancho": 51, "largo": 25},
        "51x121": {"ancho": 51, "largo": 121},
        "51x147": {"ancho": 51, "largo": 147},
        "56x120": {"ancho": 56, "largo": 120},
        "57x176": {"ancho": 57, "largo": 176},
        "58x40": {"ancho": 58, "largo": 40},
        "59x40": {"ancho": 59, "largo": 40},
        "63x38": {"ancho": 63, "largo": 38},
        "64x47": {"ancho": 64, "largo": 47},
        "68x45": {"ancho": 68, "largo": 45},
        "70x90": {"ancho": 70, "largo": 90},
        "70x267": {"ancho": 70, "largo": 267},
        "76x43": {"ancho": 76, "largo": 43},
        "76x76": {"ancho": 76, "largo": 76},
        "76x81": {"ancho": 76, "largo": 81},
        "76x305": {"ancho": 76, "largo": 305},
        "80x30": {"ancho": 80, "largo": 30},
        "81x31": {"ancho": 81, "largo": 31},
        "82x152": {"ancho": 82, "largo": 152},
        "89x159": {"ancho": 89, "largo": 159},
        "89x267": {"ancho": 89, "largo": 267},
        "92x28": {"ancho": 92, "largo": 28},
        "96x324": {"ancho": 96, "largo": 324},
        "102x38": {"ancho": 102, "largo": 38},
        "102x51": {"ancho": 102, "largo": 51},
        "102x76": {"ancho": 102, "largo": 76},
        "102x96": {"ancho": 102, "largo": 96},
        "102x102": {"ancho": 102, "largo": 102},
        "102x147": {"ancho": 102, "largo": 147},
        "108x178": {"ancho": 108, "largo": 178},
        "110x60": {"ancho": 110, "largo": 60},
        "110x300": {"ancho": 110, "largo": 300},
        "114x203": {"ancho": 114, "largo": 203},
        "126x52": {"ancho": 126, "largo": 52},
        "127x102": {"ancho": 127, "largo": 102},
        "130x130": {"ancho": 130, "largo": 130},
        "135x175": {"ancho": 135, "largo": 175},
        "145x120": {"ancho": 145, "largo": 120},
        "150x120": {"ancho": 150, "largo": 120},
        "155x165": {"ancho": 155, "largo": 165},
        "157x215": {"ancho": 157, "largo": 215},
        "181x357": {"ancho": 181, "largo": 357},
        "203x203": {"ancho": 203, "largo": 203}
    },
    "Óvalo": {
        "18x23.5": {"ancho": 18, "largo": 23.5},
        "25x30": {"ancho": 25, "largo": 30},
        "51x73": {"ancho": 51, "largo": 73}
    },
    "Circular": {
        "19x19": {"ancho": 19, "largo": 19},
        "30x30": {"ancho": 30, "largo": 30},
        "50x50": {"ancho": 50, "largo": 50},
        "54x54": {"ancho": 54, "largo": 54},
        "70x70": {"ancho": 70, "largo": 70},
        "89x89": {"ancho": 89, "largo": 89}
    },
    "Especial": {
        "110x195": {"ancho": 110, "largo": 195},
        "126.5x82.6": {"ancho": 126.5, "largo": 82.6}
    }
}

tipo_cambio = st.number_input("Tipo de cambio (MXN por USD)", min_value=0.01, value=19.0, format="%.6f")
cantidad_pedidos = st.number_input("Cantidad de pedidos", min_value=1, value=1, step=1)

total_etiquetas = total_area = total_rollos = total_costo_usd = 0
total_facturacion_usd = 0

for i in range(int(cantidad_pedidos)):
    st.markdown("---")
    st.subheader(f"📋 Pedido {i+1}")

    material_sel = st.selectbox("Material", list(materiales.keys()), key=f"m{i}")
    tipo = st.selectbox("Tipo de etiqueta", list(etiquetas_por_tipo.keys()), key=f"t{i}")
    medida = st.selectbox("Medida", list(etiquetas_por_tipo[tipo].keys()), key=f"e{i}")

    millares = st.number_input("Millares vendidos", min_value=0.0, value=0.0, format="%.6f", key=f"mil{i}")
    precio_millar = st.number_input("Precio por millar (USD)", min_value=0.0, value=0.0, format="%.8f", key=f"pre{i}")

    material = materiales[material_sel]
    etiqueta = etiquetas_por_tipo[tipo][medida]

    facturacion_usd = millares * precio_millar
    total_facturacion_usd += facturacion_usd

    etiquetas_vendidas = millares * 1000
    ancho_material_mm = material["ancho"] * 10
    etiquetas_por_fila = max(1, math.floor(ancho_material_mm / etiqueta["ancho"]))
    avance = etiqueta["largo"] + 3.175
    largo_material_mm = material["largo"] * 1000
    filas = math.floor(largo_material_mm / avance)
    etiquetas_por_rollo = max(1, etiquetas_por_fila * filas)

    rollos = etiquetas_vendidas / etiquetas_por_rollo
    area_rollo = (material["ancho"] / 100) * material["largo"]
    area_consumida = area_rollo * rollos
    costo_usd = area_consumida * material["precio"]

    total_etiquetas += etiquetas_vendidas
    total_area += area_consumida
    total_rollos += rollos
    total_costo_usd += costo_usd

if st.button("📊 Calcular Mes"):
    costo_mxn = total_costo_usd * tipo_cambio
    facturacion_mxn = total_facturacion_usd * tipo_cambio
    utilidad = facturacion_mxn - costo_mxn

    st.header("📈 Resultado Mensual")
    st.write(f"📋 Total de pedidos: {cantidad_pedidos}")
    st.write(f"🏷️ Total etiquetas vendidas: {total_etiquetas:,.0f}")
    st.write(f"📦 Rollos utilizados: {total_rollos:.8f}")
    st.write(f"📐 Área consumida: {total_area:.8f} m²")
    st.write(f"💵 Costo material USD: ${total_costo_usd:.8f}")
    st.write(f"💰 Costo material MXN: ${costo_mxn:.8f}")
    st.write(f"🧾 Facturación USD: ${total_facturacion_usd:.8f}")
    st.write(f"🧾 Facturación MXN: ${facturacion_mxn:.8f}")
    st.write(f"📈 Ganancia neta MXN: ${utilidad:.8f}")
