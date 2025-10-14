import numpy as np

from resumenDescriptivo import resumen_descriptivo
from valoresAtipicos import valores_atipicos
from boxplot import plot_boxplot

# El siguiente conjunto de datos representa el número de nuevas cuentas de email registradas durante
# diez días consecutivos:

# a. se registra los datos
email_registrados = [43, 37, 50, 51, 58, 105, 52, 45, 45, 10]
datosArray = np.array(email_registrados)

# Unidad de análisis: email registrados en 1 día,
# Variable: emails registrados
# tipo: cuantitativa discreta

# --- b. Resumen descriptivo ---
[media, mediana,q1_val,q3_val,min_val,max_val] = resumen_descriptivo(datosArray, 'Emails')
print("-" * 30)

# --- c. Hallar los valores atípicos.
valores_atipicos(q3_val,q1_val,datosArray)
print("-" * 30)

# --- d. Boxplots ---
plot_boxplot(datosArray, mediana, q1_val, q3_val,'Boxplot - Email registrados por día','Emails', zoom_range=(0, 110))
# ¿Cómo afecta la presencia de valores atípicos en las medidas descriptivas básicas (media, mediana, cuartiles y desvío estándar).
# Media (x)  y Desviación Estándar (s)
# Estas medidas se basan en la suma de todos los valores y son extremadamente sensibles a los valores atípicos.

# Mediana (Q2) y Cuartiles (Q1, Q3)
# Estas medidas se basan en la posición de los datos ordenados y son resistentes a los valores atípicos.