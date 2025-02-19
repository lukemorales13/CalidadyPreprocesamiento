import pandas as pd
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")

def seccion1_a(df):
    import numpy as np
    """
    Calcula manualmente la media, desviación estándar, cuartiles Q1 y Q3
    para todas las columnas numéricas de un DataFrame.

    Parámetro:
    - df: DataFrame
    """

    for columna in df.select_dtypes(include=[np.number]).columns:
        # Calcular la media de la columna
        media = np.mean(df[columna])
        
        # Calcular la desviación estándar muestral de la columna
        desviacion = np.std(df[columna], ddof=1)
        
        # Calcular el primer cuartil (Q1) de la columna
        Q1 = np.percentile(df[columna], 25)
        
        # Calcular el tercer cuartil (Q3) de la columna
        Q3 = np.percentile(df[columna], 75)

        # Imprimir los resultados
        print(f"Campo: {columna}")
        print(f"Media: {media:.2f}")
        print(f"Desviación estándar: {desviacion:.2f}")
        print(f"Q1 (25%): {Q1:.2f}")
        print(f"Q3 (75%): {Q3:.2f}\n")

# Llamar a la función con el DataFrame
seccion1_a(df_banco)
