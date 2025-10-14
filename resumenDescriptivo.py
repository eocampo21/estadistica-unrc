from numpy import ndarray
import numpy as np

def resumen_descriptivo(datos: ndarray, message: str):
    """
    Genera y muestra un resumen de las principales estadísticas descriptivas para un conjunto de datos.
    
    Args (Argumentos):
        datos (ndarray): El array de datos numéricos de NumPy.
        message (str): La unidad de medida para etiquetar la salida (e.g., "usuarios conectados").
        
    Returns:
        list: Lista con [media, mediana, q1, q3, min_val, max_val].
    """
    print("Suma:", np.sum(datos)) 
    print("datos:", (datos))

    
    # --- Resumen descriptivo ---
    media = np.mean(datos)
    mediana = np.median(datos)
    q1_val = np.percentile(datos, 25)
    q3_val = np.percentile(datos, 75)
    min_val = np.min(datos)
    max_val = np.max(datos)

    # Desviación Estándar MUESTRAL (ddof=1)
    desviacion_estandar = np.std(datos, ddof=1)
    cv = (desviacion_estandar / media) * 100

    print("--- Resumen Descriptivo ---")
    print(f"Datos size {datos.size}")
    print(f"Media: {media:.2f} {message}")
    print(f"Mediana: {mediana:.2f} {message}")
    print(f"Cuartil Q1: {q1_val:.2f} {message}")
    print(f"Cuartil Q3: {q3_val:.2f} {message}")
    print(f"Desviación estándar: {desviacion_estandar:.2f} {message}")
    print(f"Coeficiente de variación: {cv:.2f}%")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    
    
    # --- INTERPRETACIÓN DEL DESVÍO ESTÁNDAR / CV ---
    
    # Se evalúa el CV (en porcentaje) para determinar la dispersión relativa.
    
    # --- INTERPRETACIÓN DEL DESVÍO ESTÁNDAR / CV ---
    
    if cv <= 10.0:
        interpretacion_desvio = (
            "La distribución tiene una dispersión muy baja. "
            "El desvío estándar representa una fracción insignificante de la media, "
            "indicando que los datos son extremadamente homogéneos (baja variabilidad)."
        )
    elif cv <= 20.0:
        interpretacion_desvio = (
            "La distribución tiene una dispersión baja a moderada. "
            "El desvío estándar es relativamente pequeño, sugiriendo que la "
            "mayoría de las observaciones están cercanas a la media."
        )
    else: # CV > 20.0
        interpretacion_desvio = (
            "La distribución tiene una dispersión moderada a alta. "
            "El desvío estándar es significativamente grande con relación a la media, "
            "lo que indica una variabilidad sustancial en los datos."
        )

    print("\n--- Interpretación de la Dispersión ---")
    print(f"Conclusión: {interpretacion_desvio}")
    
    return [media, mediana, q1_val, q3_val, min_val, max_val]