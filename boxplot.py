import matplotlib.pyplot as plt
from numpy import ndarray
from typing import Optional, Tuple

def plot_boxplot(datos: ndarray, mediana: float, q1_val: float, q3_val: float, title: str, xlabel: str, zoom_range: Optional[Tuple[float, float]] = None):
    """
    Genera un diagrama de cajas (boxplot) horizontal con estilos personalizados 
    y etiquetas para los cuartiles.

    Args (Argumentos):
        datos (ndarray): El array de datos numéricos de NumPy a graficar.
        mediana (float): El valor de la mediana (Q2) usado para etiquetar.
        q1_val (float): El valor del Cuartil 1 (Q1) usado para etiquetar.
        q3_val (float): El valor del Cuartil 3 (Q3) usado para etiquetar.
        title (str): El título principal del gráfico.
        xlabel (str): La etiqueta del eje X (variable medida).
        zoom_range (Optional[Tuple[float, float]]): Una tupla (min_x, max_x) para 
            establecer los límites del eje X. None si no se especifica.
            
    Returns:
        None: La función muestra boxplot
    """
    
    plt.figure(figsize=(10, 4))
    
    # Plot the Boxplot
    plt.boxplot(
        datos,
        vert=False,    
        patch_artist=True,   
        boxprops=dict(facecolor='lightblue', color='blue'), 
        medianprops=dict(color='red', linewidth=2), 
        capprops=dict(color='blue'), 
        flierprops=dict(marker='o', markerfacecolor='red', markersize=8)
    )
    
    # Etiquetar Cuartiles
    plt.text(q1_val, 1.05, f"Q1: {q1_val:.2f}", ha='center')
    plt.text(mediana, 1.05, f"Mediana: {mediana:.2f}", ha='center', color='red')
    plt.text(q3_val, 1.05, f"Q3: {q3_val:.2f}", ha='center')
    
    
    # Aplicar Zoom
    if zoom_range:
        plt.xlim(zoom_range)
    else:
        # Se usa un zoom por defecto que abarca el rango de los datos si no se especifica uno.
        # Esto requiere importar numpy si esta es la única función en el archivo.
        import numpy as np 
        plt.xlim(np.min(datos) - 1, np.max(datos) + 1) 

    plt.title(title)
    plt.xlabel(xlabel)
    plt.yticks([]) 
    plt.grid(axis='x', alpha=0.75, linestyle='--')
    plt.show()