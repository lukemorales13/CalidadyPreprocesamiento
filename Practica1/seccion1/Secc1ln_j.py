import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
def seccion1_j(df, columna_trabajo):
    """
    Genera una gráfica de barras mostrando la cantidad de cuentahabientes por tipo de trabajo.

    Parámetros:
    - df: DataFrame con los datos.
    - columna_trabajo: Nombre de la columna que contiene los tipos de trabajo.
    """

    # Contar la cantidad de cuentahabientes por trabajo
    job_counts = df[columna_trabajo].value_counts()

    # Crear la gráfica de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=job_counts.index, y=job_counts.values, palette="pastel")

    # Personalizar la gráfica
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Tipo de Trabajo")
    plt.ylabel("Cantidad de Cuentahabientes")
    plt.title("Distribución de Cuentahabientes por Trabajo")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Mostrar la gráfica
    plt.show()


# Llamar a la función para graficar
seccion1_j(df_banco, "job")
