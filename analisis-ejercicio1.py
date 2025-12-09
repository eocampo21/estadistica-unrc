import numpy as np
from boxplot import plot_boxplot
from resumenDescriptivo import resumen_descriptivo
from histograma import histograma
import pandas as pd
from valoresAtipicos import valores_atipicos

# Los datos siguientes corresponden al tiempo ( seg.) necesario para procesar 25 trabajos en una CPU.

# Se registra los datos
tiempos = [1.17, 1.61, 1.16, 1.38, 3.53, 1.23, 0.82, 0.96, 2.01, 0.15, 2.11, 0.71, 0.02, 1.59, 0.19, 1.91, 2.16, 0.92, 0.75, 2.59, 3.07, 1.1, 3.76, 0.47, 4.75]
datosArray = np.array(tiempos)

# a) b)
# Unidad de análisis: 1 trabajo procesado por CPU
# Variable: tiempo de procesamiento
# tipo: cuantitativa continua
# poblacion: todos los posibles tiempos que esa CPU podría registrar.
# muestra: 25 trabajos seleccionados


# Resumen descriptivo
# g) Obtener un resumen descriptivo de los tiempos necesarios para procesar los 25 trabajos.
[media, mediana,q1_val,q3_val,min_val,max_val] = resumen_descriptivo(datosArray, 'Segundos')
print("-" * 30)


# c) Realizar una tabla de frecuencias organizando los datos en 5 intervalos y graficar adecuadamente.
datosArrayLen = len(datosArray)
intervalos = 5

# Definir los Límites de los Intervalos (Bins)
# El rango va de 0.02 a 4.75. Amplitud aprox 0.95
rango = max_val - min_val

# np.linspace crea 6 puntos equidistantes para definir 5 intervalos
# Agregamos una epsilon (ej. 1e-8) a max_val para GARANTIZAR la inclusión del máximo
epsilon = 1e-8
limites = np.linspace(min_val, max_val + epsilon, intervalos + 1)
print("-" * 30)

# 3. Generar la Tabla de Frecuencias (Usando Pandas)
# pd.cut crea los intervalos, value_counts cuenta las frecuencias
frecuencias_abs = pd.cut(
    datosArray, 
    bins=limites, 
    include_lowest=True  # Esto garantiza que el valor MÍNIMO se cuente!
).value_counts()

# Crear la tabla final de frecuencias
tabla_frecuencias = pd.DataFrame(frecuencias_abs).sort_index()
tabla_frecuencias.columns = ['Frecuencia Absoluta (fi)']
tabla_frecuencias['Frecuencia Relativa (fri)'] = tabla_frecuencias['Frecuencia Absoluta (fi)'] / datosArrayLen
tabla_frecuencias['Frecuencia Absoluta Acumulada (Fi)'] = tabla_frecuencias['Frecuencia Absoluta (fi)'].cumsum()
tabla_frecuencias['Frecuencia Relativa Acumulada (Fri)'] = tabla_frecuencias['Frecuencia Relativa (fri)'].cumsum()

print("--- TABLA DE FRECUENCIAS (5 INTERVALOS) ---")
print(tabla_frecuencias)
print('')

print("-" * 30)

# d) ¿Qué porcentaje de trabajos fueron procesados en menos de 3.80 segundos?
# El porcentaje de trabajos procesados en menos de 3.804 segundos es del 96%.

# e) ¿Qué cantidad de trabajos fueron procesados en al menos 1.92 segundos?
# La cantidad de trabajos que fueron procesados en al menos 1.92 segundos es de 8 trabajos.

# f) ¿Cómo se interpreta la frecuencia relativa del tercer intervalo?
# 16% de los trabajos se procesan entre 1.912 - 2.858 segundos

# h) Realizar un histograma y un diagrama de cajas.
# Histograma
histograma(
    datosArray,
    title='Histograma de Tiempos de Procesamiento con Frecuencias',
    xlabel='Tiempo (segundos)',
    ylabel='Cantidad de trabajos procesados'
)

# valores_atipicos
valores_atipicos(q3_val,q1_val,datosArray)

# Boxplots
plot_boxplot(
    datosArray, 
    mediana,
    q1_val,
    q3_val,
    title='Diagrama de Cajas de Tiempos de Procesamiento', 
    xlabel='Tiempo (segundos)',
    zoom_range=(0, 3.9)
), 