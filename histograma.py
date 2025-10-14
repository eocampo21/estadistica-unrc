from matplotlib import pyplot as plt
from numpy import ndarray

def histograma(datos: ndarray,title: str, xlabel: str, ylabel: str):
    """
    Genera y muestra un histograma de frecuencias absolutas para el conjunto de datos.

    Args (Argumentos):
        title (str): El título principal del gráfico.
        xlabel (str): La etiqueta del eje X (variable medida).
        ylabel (str): La etiqueta del eje Y (frecuencia/cantidad).
        datos (ndarray): El array de datos numéricos de NumPy a graficar.
    """
    # HISTOGRAMA
    plt.figure(figsize=(10, 6))
    
    # n= frequencias absolutas, bins= limites de cada rango, 
    # patches= objetos que representan barras del histograma
    n, bins, _ = plt.hist(datos, bins=5, edgecolor='black', color='lightblue')
    
    # Imprimir información del histograma para análisis
    print('Frecuencias absolutas (n):')
    print(n)
    print('Límites de los bins (bins):')
    print(bins)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(bins)
    plt.grid(axis='y', linestyle='--')
    plt.show() # Este comando abre la primera ventana.