import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def diagrama_dispersion(df: pd.DataFrame, x_col: str, y_col: str, titulo: str = 'Diagrama de Dispersión') -> float:
    """
    Genera un diagrama de dispersión con línea de regresión para analizar la relación lineal 
    entre dos variables cuantitativas y muestra el coeficiente de correlación.
    
    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        x_col (str): Nombre de la columna para el eje X (Variable Independiente).
        y_col (str): Nombre de la columna para el eje Y (Variable Dependiente).
        titulo (str): Título del gráfico.
        
    Returns:
        float: El Coeficiente de Correlación de.
    """
    
    # 1. Cálculo de la Correlación
    # Usa el método .corr() de pandas
    correlacion = df[x_col].corr(df[y_col])

    # 2. Generación del Gráfico
    plt.figure(figsize=(10, 6))
    
    # Usamos regplot para dibujar scatterplot y la línea de regresión
    sns.regplot(
        x=x_col, 
        y=y_col, 
        data=df, 
        color='darkblue', 
        scatter_kws={'s': 80, 'alpha': 0.7}, 
        line_kws={'color': 'red', 'linewidth': 2}
    )

    plt.title(f'{titulo}\nCorrelación r: {correlacion:.3f}', fontsize=14)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    
    # 3. Interpretación de la Correlación
    print("\n" + "=" * 50)
    print("Análisis Bivariado (Correlación)")
    print(f"Coeficiente de Correlación (r): {correlacion:.3f}")
    
    if correlacion > 0:
        conclusion = f"Asociación Positiva. A medida que {x_col} crece, {y_col} también lo hace. Cercana a +1."
    elif correlacion < 0:
        conclusion = f"Asociación Negativa . A medida que {x_col} crece, {y_col} decrece. Cercana a -1."
    else:
        # r es muy cercano a cero
        conclusion = f"No hay Asociación Lineal. El valor de {x_col} no predice el valor de {y_col}. Cercana a 0."
    print(f"Conclusión: {conclusion}")
    print("=" * 50)
    
    return correlacion

# Posibles valores
# | Coeficiente | Interpretación                                                       |
# | ----------- | -------------------------------------------------------------------- |
# | +1          | Relación lineal perfecta positiva (cuando una sube, la otra también) | Peso y altura
# | 0           | No hay relación lineal                                               |
# | –1          | Relación lineal perfecta negativa (cuando una sube, la otra baja)    | Valor venta auto y ańos