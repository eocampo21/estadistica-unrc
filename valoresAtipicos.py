from matplotlib.pylab import ndarray

def valores_atipicos(q3:float,q1:float,datos: ndarray):
    """
    Genera y muestra los valores atípicos (outliers) utilizando la regla del 1.5 * RIC.
    
    Args (Argumentos):
        q3 (float): El valor del Cuartil 3 (Q3), correspondiente al 75% de los datos.
        q1 (float): El valor del Cuartil 1 (Q1), correspondiente al 25% de los datos.
        datos (ndarray): El array de datos numéricos de NumPy para la detección de outliers.
            
    Returns:
        None: La función imprime el resultado directamente en la consola.
    """
    RIC = q3 - q1  # Rango Intercuartílico
    limite_inferior = q1 - 1.5 * RIC
    limite_superior = q3 + 1.5 * RIC

    outliers_bajos = datos[datos < limite_inferior]
    outliers_altos = datos[datos > limite_superior]

    print("\n--- Detección de Valores Atípicos ---")
    print(f"Rango Intercuartílico (RIC): {RIC:.2f}")
    print(f"Límite Inferior (LI = Q1 - 1.5*RIC): {limite_inferior:.2f}")
    print(f"Límite Superior (LS = Q3 + 1.5*RIC): {limite_superior:.2f}")
    mensaje_bajos = "No se encontraron valores atípicos bajos." if outliers_bajos.size == 0 else f"{outliers_bajos}"
    print(f"Valores Atípicos Bajos: {mensaje_bajos}")
    mensaje_altos = "No se encontraron valores atípicos altos." if outliers_altos.size == 0 else f"{outliers_altos}"
    print(f"Valores Atípicos Altos: {mensaje_altos}")