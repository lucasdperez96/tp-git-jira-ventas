
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PROY-11
# Validar lectura de datos
# =========================

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"])

# =========================
# PROY-15
# Resumen estadístico
# =========================

ventas_totales = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()

print("Ventas totales:", ventas_totales)
print("Promedio de ventas:", round(promedio_ventas, 2))
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)

# =========================
# PROY-14
# Períodos con mayor volumen
# =========================

mayor_venta = df.loc[df["sales_amount"].idxmax()]
menor_venta = df.loc[df["sales_amount"].idxmin()]

print("\nPeríodo con mayor volumen de ventas:")
print(mayor_venta)

print("\nPeríodo con menor volumen de ventas:")
print(menor_venta)

# =========================
# PROY-17
# Evolución temporal de ventas
# =========================

# BUG intencional para revisión QA
ventas_por_periodo = df.groupby(
    df["sales_date"].dt.day
)["sales_amount"].sum()

# =========================
# Generación de gráfico
# =========================

plt.figure(figsize=(10, 5))

plt.plot(
    ventas_por_periodo.index,
    ventas_por_periodo.values
)

plt.title("Evolución de Ventas")
plt.xlabel("Periodo")
plt.ylabel("Monto de Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("\nGráfico guardado correctamente.")

# =========================
# PROY-16
# Exportar resultados
# =========================

resumen = pd.DataFrame({
    "Metrica": [
        "Ventas Totales",
        "Promedio",
        "Venta Maxima",
        "Venta Minima"
    ],
    "Valor": [
        ventas_totales,
        promedio_ventas,
        venta_maxima,
        venta_minima
    ]
})

resumen.to_csv(
    "resultados/resumen_ventas.csv",
    index=False
)

print("\nResumen exportado correctamente.")

# =========================
# PROY-19
# Validación de visualización
# =========================

if not ventas_por_periodo.empty:
    print("\nVisualización validada correctamente.")
else:
    print("\nError en la visualización.")

