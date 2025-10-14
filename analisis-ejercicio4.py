from boxplot import plot_boxplot
import numpy as np
from resumenDescriptivo import resumen_descriptivo
from valoresAtipicos import valores_atipicos
from histograma import histograma

# Un proveedor de red investiga la velocidad de descarga de su red. El n´umero de usuarios conectados
# es registrado en cincuenta localidades (miles de personas),

# a. se registra los datos
datos = [
    19.7, 18.7, 17.6, 15.9, 15.2, 17.1, 15.0, 18.8, 21.6, 11.9,
    17.2, 22.1, 18.5, 17.2, 18.6, 14.8, 21.7, 15.8, 16.3, 22.8,
    24.1, 13.3, 16.2, 17.5, 19.0, 23.9, 14.8, 22.2, 21.7, 20.7,
    13.5, 15.8, 13.1, 16.1, 21.9, 23.9, 19.3, 12.0, 19.9, 19.4,
    15.4, 16.7, 19.5, 16.2, 16.9, 17.1, 20.2, 13.4, 19.8, 17.7 
]
datosArray = np.array(datos)

# Población	Todas las localidades a las que el proveedor de red presta servicio.
# Muestra	Las 50 localidades seleccionadas para el estudio.
# Unidad de análisis: Una localidad
# Variable: nros de usuarios conectados (en miles), variable cuantitativa continua
# Nota: La variable es técnicamente discreta (es una cuenta), pero al tener decimales y un amplio rango de valores, se analiza como CUANTITATIVA CONTINUA.


# --- b. Resumen descriptivo ---
[media, mediana,q1_val,q3_val,min_val,max_val] = resumen_descriptivo(datosArray, 'Usuarios conectados')
print("-" * 30)

# --- c. Boxplots
plot_boxplot(
    datosArray, 
    mediana,
    q1_val,
    q3_val,
    title='Diagrama de Cajas de Usuarios por Localidad', 
    xlabel='Cantidad de Usuarios Conectados (en miles)',
    zoom_range=(11, 26)
),
print("-" * 30)

# --- d. Valores atípicos ---
# d) Calcular el rango intercuartílico. ¿Hay algún valor atípico? [respondido dentro de esa function]
valores_atipicos(q3_val,q1_val,datosArray)
print("-" * 30)

# --- e.  Histograma
# Histograma apoya la teoria de que los datos poseen una distrubución normal
# dado que la campana de gauss está centrada al medio con una leve asimetría positiva
histograma(
    datos,
    title='Histograma de Usuarios Conectados', 
    xlabel='Usuarios Conectados (en miles)',
    ylabel='Frecuencia (Cantidad de Localidades)', 
)