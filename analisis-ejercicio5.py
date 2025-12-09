import pandas as pd
from diagramaDispersion import diagrama_dispersion
from resumenDescriptivo import resumen_descriptivo
import numpy as np


# --- Datos del Ejercicio ---
# A continuaci ́on se presentan los pesos ( kg) y las cantidades de combustible consumidas en rutas
# (km/naf) de 7 marcas de autom ́ovil elegidas al azar
datosPeso = [1443, 1568, 1465, 1811, 1109, 1136, 1040]
datosConsumoCombustible = [43, 46, 44, 39, 59, 55, 59]

# Unidad de análisis: 
# Variable:
# tipo:
# peso
# consumo
# poblacion: 
# muestra:

# a) Calcular los estad ́ısticos de posici ́on y de dispersi ́on que sean posibles para cada variable.
print("--- resumen_descriptivo ---")
print("--- Peso ---")
[media, mediana,q1_val,q3_val,min_val,max_val] = resumen_descriptivo(np.array(datosPeso), 'Peso automivil')
print("--- Combustible ---")
[media, mediana,q1_val,q3_val,min_val,max_val] = resumen_descriptivo(np.array(datosConsumoCombustible), 'Consumo combustible')

# b) ¿Cu ́al de las dos variables presenta m ́as variabilidad? Justificar.
# Peso posee una mayor variabilidad de los datos que consumo de nafta. El CV de peso es 20.68%
# lo que nos sugiere que hay gran dispersion de datos, datos no cercanos a la media
# datos pocos confiables

# c) Realizar el diagrama de dispersión usando
# Crear un DataFrame de pandas para usar .corr() y seaborn
df_autos = pd.DataFrame({
    'Peso (kg)': datosPeso,
    'Eficiencia (km/naf)': datosConsumoCombustible
})

print("--- ANALISIS BIVARIADO: PESO vs EFICIENCIA ---")
r_correlacion = diagrama_dispersion(
    df=df_autos, 
    x_col='Peso (kg)', 
    y_col='Eficiencia (km/naf)', 
    titulo='Relación entre el Peso del Automóvil y su Eficiencia de Combustible'
)
# d) ¿Qu ́e sugiere el resultado de un plan nacional para reducir el consumo de combustible impor-
# tado? A medidas que el peso sube la eficienca del combustible es menor