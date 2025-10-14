# Proyecto de la materia Estadística

Este proyecto contiene análisis estadísticos de diferentes conjuntos de datos, implementados en Python. Incluye 4 ejercicios prácticos que utilizan módulos reutilizables para realizar análisis exploratorio de datos.

## Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd mi-proyecto-estadistica
```

### 2. Crear y activar el entorno virtual

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Este comando instalará automáticamente todas las librerías necesarias:
- **numpy**: Para cálculos numéricos y arrays
- **pandas**: Para manejo de datos y tablas
- **matplotlib**: Para crear gráficos
- **seaborn**: Para visualizaciones estadísticas avanzadas

## Ejecutar los Ejercicios

### Ejercicio 1: Análisis de Tiempos de Procesamiento de CPU
Analiza tiempos de procesamiento de 25 trabajos en una CPU, incluyendo tabla de frecuencias, histogramas y boxplots.

```bash
python analisis-ejercicio1.py
```

### Ejercicio 2: Análisis de Encuesta Estudiantil
Analiza una base de datos de estudiantes (`StudentSurvey2.csv`) con múltiples variables demográficas y académicas.

```bash
python analisis-ejercicio2.py
```

### Ejercicio 3: Análisis de Registro de Emails
Analiza el número de nuevas cuentas de email registradas durante 10 días consecutivos.

```bash
python analisis-ejercicio3.py
```

### Ejercicio 4: Análisis de Usuarios Conectados
Investiga la velocidad de descarga de una red analizando el número de usuarios conectados en 50 localidades.

```bash
python analisis-ejercicio4.py
```


## Componentes del Proyecto

El proyecto está organizado en módulos reutilizables que encapsulan funcionalidades estadísticas específicas:

### `resumenDescriptivo.py`
**Propósito:** Generar un resumen estadístico completo de un conjunto de datos.

**Funcionalidad:**
- Calcula media, mediana, cuartiles (Q1, Q3), mínimo y máximo
- Calcula desviación estándar muestral (con `ddof=1`)
- Calcula coeficiente de variación (CV)
- Interpreta la dispersión de los datos basándose en el CV
- Devuelve los valores calculados para uso posterior

**Uso típico:**
```python
[media, mediana, q1, q3, min_val, max_val] = resumen_descriptivo(datos, 'Unidad')
```

---

### `histograma.py`
**Propósito:** Crear histogramas de frecuencias absolutas personalizados.

**Funcionalidad:**
- Genera histogramas con 5 bins (rangos) por defecto
- Muestra frecuencias absolutas y límites de intervalos
- Personaliza título, etiquetas de ejes
- Incluye grid para mejor legibilidad

**Uso típico:**
```python
histograma(datos, title='Título', xlabel='Eje X', ylabel='Frecuencia')
```

---

### `boxplot.py`
**Propósito:** Crear diagramas de cajas (boxplots) con etiquetas informativas.

**Funcionalidad:**
- Genera boxplots horizontales personalizados
- Etiqueta cuartiles (Q1, Q2/mediana, Q3) directamente en el gráfico
- Resalta valores atípicos en color rojo
- Permite aplicar zoom al rango de interés
- Incluye grid horizontal para facilitar lectura

**Uso típico:**
```python
plot_boxplot(datos, mediana, q1, q3, 
             title='Título', 
             xlabel='Variable', 
             zoom_range=(min, max))
```

---

### `valoresAtipicos.py`
**Propósito:** Detectar valores atípicos usando el método del rango intercuartílico (RIC).

**Funcionalidad:**
- Calcula el rango intercuartílico (RIC = Q3 - Q1)
- Identifica outliers bajos 
- Identifica outliers altos 
- Imprime resultados detallados en consola

**Uso típico:**
```python
valores_atipicos(q3, q1, datos)
```

---

## Estructura del Proyecto

```
mi-proyecto-estadistica/
├── analisis-ejercicio1.py       # Ejercicio 1: Tiempos de CPU
├── analisis-ejercicio2.py       # Ejercicio 2: Encuesta estudiantil
├── analisis-ejercicio3.py       # Ejercicio 3: Emails registrados
├── analisis-ejercicio4.py       # Ejercicio 4: Usuarios conectados
├── boxplot.py                   # Componente para boxplots
├── histograma.py                # Componente para histogramas
├── resumenDescriptivo.py        # Componente para estadísticas descriptivas
├── valoresAtipicos.py           # Componente para detección de outliers
├── estadistica/
│   └── unidades/
│       ├── StudentSurvey2.csv   # Dataset del Ejercicio 2
│       └── [PDFs de referencia]
├── requirements.txt             # Dependencias del proyecto
├── venv/                        # Entorno virtual (no incluido en git)
├── .gitignore                   # Archivos ignorados por git
└── README.md                    # Este archivo
```

## Recursos Adicionales

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

