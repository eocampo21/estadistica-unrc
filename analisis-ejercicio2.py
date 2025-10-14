import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from valoresAtipicos import valores_atipicos
from resumenDescriptivo import resumen_descriptivo

# Configuración para mostrar el gráfico en el entorno de la notebook
sns.set_style('whitegrid')

# Leer la base de datos
df = pd.read_csv('./estadistica/unidades/StudentSurvey2.csv')

# a) Unidad de análisis, variables y dimensión
print("a) Análisis de la base de datos:")
print("-" * 30)
print(f"Dimensión de DB: {df.shape[0]} filas y {df.shape[1]} columnas.")
# Unidad de análisis: es un estudiante
# Variables y tipos de variable que se han medido:
"""
Variables y tipos de variable que se han medido:
-------------------------------------------------------------------------------------
| Variable Renombrada | Tipo de Variable | Clasificación
-------------------------------------------------------------------------------------
| Año | Categórica Ordinal | Indica un orden: FirstYear, Sophomore, Junior, etc.
-------------------------------------------------------------------------------------
| Género | Categórica Nominal | Categoría sin orden: M o F.
-------------------------------------------------------------------------------------
| Fuma | Categórica Nominal | Categoría sin orden: Yes o No.
-------------------------------------------------------------------------------------
| Premio | Categórica Nominal | Categoría sin orden: Olympic, Nobel, Academy, etc.
-------------------------------------------------------------------------------------
| SAT_Mas_Alto | Categórica Nominal | Categoría sin orden: Verbal o Math.
-------------------------------------------------------------------------------------
| Ejercicio_hs | Cuantitativa Discreta | Horas a la semana (se cuenta).
-------------------------------------------------------------------------------------
| TV_hs | Cuantitativa Discreta | Horas a la semana (se cuenta).
-------------------------------------------------------------------------------------
| Altura_in | Cuantitativa Continua | Medición física (permite decimales).
-------------------------------------------------------------------------------------
| Peso_lb | Cuantitativa Continua | Medición física (permite decimales).
-------------------------------------------------------------------------------------
| Hermanos | Cuantitativa Discreta | Cantidad (se cuenta).
-------------------------------------------------------------------------------------
| Orden_Nacimiento | Cuantitativa Discreta / Ordinal | Posición de nacimiento (se cuenta y establece un orden).
-------------------------------------------------------------------------------------
| SAT_Verbal | Cuantitativa Discreta | Puntaje (se cuenta en incrementos).
-------------------------------------------------------------------------------------
| SAT_Matematicas | Cuantitativa Discreta | Puntaje (se cuenta en incrementos).
-------------------------------------------------------------------------------------
| SAT_Total | Cuantitativa Discreta | Puntaje total.
-------------------------------------------------------------------------------------
| GPA | Cuantitativa Continua | Promedio de notas (permite decimales).
-------------------------------------------------------------------------------------
| Pulso | Cuantitativa Discreta | Pulsaciones por minuto (se cuenta).
-------------------------------------------------------------------------------------
| Piercings | Cuantitativa Discreta | Cantidad (se cuenta).
-------------------------------------------------------------------------------------
"""

# b) Renombrar variables
nombres_nuevos = {
    'Year': 'Año',
    'Gender': 'Genero',
    'Smoke': 'Fuma',
    'Award': 'Premio',
    'HigherSAT': 'SAT_Mas_Alto',
    'Exercise': 'Ejercicio_hs',
    'TV': 'TV_hs',
    'Height': 'Altura_in',
    'Weight': 'Peso_lb',
    'Siblings': 'Hermanos',
    'BirthOrder': 'Orden_Nacimiento',
    'VerbalSAT': 'SAT_Verbal',
    'MathSAT': 'SAT_Matematicas',
    'SAT': 'SAT_Total',
    'GPA': 'GPA',
    'Pulse': 'Pulso',
    'Piercings': 'Piercings'
}
df.rename(columns=nombres_nuevos, inplace=True)
print("\nb) Variables renombradas:")
print(df.head())

# c) Convertir Altura de pulgadas a centímetros
print(df['Altura_in'])
df['Altura_cm'] = df['Altura_in'] * 2.54
print("\nc) Columna 'Altura_cm' creada (primeros 5 valores):")
print(df[['Altura_in', 'Altura_cm']].head())
print("-" * 30)

# d) Representar gráficamente la variable Año
print("\nd) Gráfico de la variable Año:")
plt.figure(figsize=(8, 5))
df['Año'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribución de Estudiantes por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Estudiantes')
plt.xticks(rotation=0)
plt.show()
print("-" * 30)

# e) ¿Existe algún tipo de asociación entre Género y Fuma?
print("\ne) Asociación entre Género y Fuma:")
contingencia = pd.crosstab(df['Genero'], df['Fuma'])
print("\nTabla de contingencia:")
print(contingencia)
contingencia_porcentaje = pd.crosstab(df['Genero'], df['Fuma'], normalize='index') * 100
print("\nTabla de contingencia (en porcentajes):")
print(contingencia_porcentaje)
# Sí, existe una asociación. 
# Al comparar el porcentaje de estudiantes que fuman dentro de cada grupo de género, se observa que:
# El 9.47% de las mujeres fuma.
# El 13.99% de los hombres fuma.
# Dado que estas distribuciones son notablemente diferentes, se concluye que el género influye en el hábito de fumar.
print("-" * 30)

# f) ¿Hay valores atípicos de Altura?
# Preparamos los datos limpios una sola vez:
datos_altura_cm = df['Altura_cm'].dropna().values

[media, mediana,q1_val,q3_val,min_val,max_val] = resumen_descriptivo(datos_altura_cm, 'Altura en CM')

print("\nf) Búsqueda de valores atípicos en Altura:")
valores_atipicos(q3_val,q1_val,datos_altura_cm)
# Conclusión: El análisis confirma la existencia de un valor atípico en la altura (extremadamente alto)
# Valores Atípicos Altos: 210.82
print("-" * 30)

# g) ¿Cambia la distribución de Altura según Año?
print("\ng) Distribución de Altura según Año:")
plt.figure(figsize=(10, 6))
# sns se usa para Gráficos Agrupados
sns.boxplot(x='Año', y='Altura_cm', data=df.dropna(subset=['Año', 'Altura_cm']))
plt.title('Distribución de Altura por Año')
plt.xlabel('Año')
plt.ylabel('Altura (cm)')
plt.show()
# Conclusión: como las medianas y las dispersiones son prácticamente iguales para FirstYear, Sophomore, Junior y Senior, se concluye que la distribución de la altura es estable y no está asociada al año de estudio del estudiante.
print("-" * 30)

# h) ¿Los datos sugieren algún tipo de relación entre Peso y Altura?
print("\nh) Relación entre Peso y Altura:")
df_filtrado = df.dropna(subset=['Peso_lb', 'Altura_cm'])

plt.figure(figsize=(8, 6))
# Genera un Diagrama de Dispersión
sns.scatterplot(x='Peso_lb', y='Altura_cm', data=df_filtrado)
plt.title('Relación entre Peso y Altura')
plt.xlabel('Peso (lb)')
plt.ylabel('Altura (cm)')
plt.show()

correlacion = df_filtrado['Peso_lb'].corr(df_filtrado['Altura_cm'])
print(f"\nCoeficiente de correlación entre Peso y Altura: {correlacion:.2f}")
# Conclusión:  sí, el análisis sugiere una fuerte dependencia directa entre las variables,
# Esto es biológicamente esperado, ya que las personas más altas suelen tener mayor masa corporal. 