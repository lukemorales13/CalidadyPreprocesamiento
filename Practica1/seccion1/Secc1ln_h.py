import pandas as pd
import numpy as np
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
def seccion1_g(df):
  import plotly.express as px
  """Realiza la gráfica de bigotes de balance y compara con la función describe()
  de pandas. Compara si ambos métodos indican las mismas observaciones  """
  for columna_numerica in range(len(df.describe().T)):
    print('Campo: ',df.describe().T['25%'].reset_index()['index'].iloc[columna_numerica])
    print("Media: ",df.describe().T['mean'].reset_index()['mean'].iloc[columna_numerica])
    print("Desviación estándar: ",df.describe().T['std'].reset_index()['std'].iloc[columna_numerica])
    print("Q1: ",df.describe().T['25%'].reset_index()['25%'].iloc[columna_numerica])
    print("Q2: ",df.describe().T['75%'].reset_index()['75%'].iloc[columna_numerica],'\n')

  for columna in df_banco.select_dtypes(include=[np.number]).columns:
    fig = px.box(df_banco, x=columna)
    fig.update_traces(orientation='h')
    fig.update_layout(height=300)
    fig.show()

  return

seccion1_g(df_banco)