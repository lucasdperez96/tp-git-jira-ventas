
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Calcular métricas
ventas_totales = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Promedio de ventas:", round(promedio_ventas, 2))
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)

# Generar gráfico
plt.figure(figsize=(10,5))
plt.plot(df["sales_date"], df["sales_amount"])

plt.title("Evolución de Ventas")
plt.xlabel("Fecha")
plt.ylabel("Monto de Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado correctamente.")
