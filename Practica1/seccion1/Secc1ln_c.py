import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")

def seccion1_c(df, columna_estado_civil, output_file):
    """
    Esta función calcula la distribución porcentual de los estados civiles
    de los cuentahabientes y los grafica en un pie chart usando Seaborn.
    """

    # Contar la cantidad de ocurrencias de cada estado civil
    estado_civil_counts = df[columna_estado_civil].value_counts()

    # Calcular los porcentajes
    estado_civil_percent = estado_civil_counts / estado_civil_counts.sum() * 100

    # Crear el gráfico de pastel
    plt.figure(figsize=(8, 6))
    plt.pie(
        estado_civil_percent,
        labels=estado_civil_percent.index,
        autopct='%1.1f%%',
        colors=sns.color_palette("pastel"),
        startangle=140
    )

    plt.title("Distribución de Estados Civiles de Cuentahabientes")
    # Guardar el gráfico como un archivo de imagen
    plt.savefig(output_file)
    # Mostrar el gráfico
    plt.show()

# Llamar a la función para graficar y guardar la imagen
seccion1_c(df_banco, "marital", "estado_civil_pie_chart.png")
