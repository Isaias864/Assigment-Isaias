import pandas as pd

# Carga los datos directo desde tu app en Vercel.
# Reemplaza la URL por la de tu app + /portfolio.csv una vez desplegada.
url = url = "https://assigment-isaias.vercel.app/portfolio.csv"
df = pd.read_csv(url)

# --- Cálculo del KPI ---
df["ganancia"] = df["valor_actual"] - df["monto_invertido"]
df["rendimiento_%"] = (df["ganancia"] / df["monto_invertido"]) * 100

total_invertido = df["monto_invertido"].sum()
total_actual = df["valor_actual"].sum()
kpi_rendimiento = (total_actual - total_invertido) / total_invertido * 100

print(df.round(2))
print()
print(f"Total invertido: ${total_invertido:,.0f}")
print(f"Valor actual:    ${total_actual:,.0f}")
print(f"KPI · Rendimiento total de la cartera: {kpi_rendimiento:.1f}%")
