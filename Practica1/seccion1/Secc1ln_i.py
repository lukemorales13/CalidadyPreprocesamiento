import pandas as pd
import numpy as np
import plotly.express as px
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
# Lectura del conjunto de datos.df_banco
def seccion1_i(df, columna_edad, columna_balance):
    """
    Genera un scatter plot para visualizar la relación entre 'age' y 'balance'.
    También calcula el coeficiente de correlación de Pearson.

    Parámetros:
    - df: DataFrame con los datos.
    - columna_edad: Nombre de la columna de edad.
    - columna_balance: Nombre de la columna de balance.
    """

    # Calcular la correlación de Pearson
    correlacion = df[columna_edad].corr(df[columna_balance])
    print(f"Coeficiente de correlación de Pearson entre {columna_edad} y {columna_balance}: {correlacion:.2f}")

    # Generar el scatter plot con Plotly
    fig = px.scatter(df, x=columna_edad, y=columna_balance,
                     title="Relación entre Edad y Balance",
                     labels={columna_edad: "Edad", columna_balance: "Balance"},
                     trendline="ols",  # Agregar línea de tendencia
                     opacity=0.7)

    fig.show()

    print("¿Hay correlación entre las variables ‘age’ y ‘balance’ de los cuentahabientes? Resuelve esta pregunta mediante una gráfica de tipo scatter plot")
    print('No hay relación')


# Llamar a la función para analizar la correlación
seccion1_i(df_banco, "age", "balance")
