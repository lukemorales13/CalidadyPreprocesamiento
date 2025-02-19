import pandas as pd
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
# Lectura del conjunto de datos.df_banco
def seccion1_f(df):
  """¿Qué instrucción de pandas usas para filtrar sólo las columnas: contact,
  housing y day de personas cuyo valor de educación es ‘secondary’?"""
  print("¿Qué instrucción de pandas usas para filtrar sólo las columnas: contact,housing y day de personas cuyo valor de educación es ‘secondary’?\n")
  print("R = df_banco[df_banco['education']=='secondary'][['contact','housing']] \n Mostramos un ejemplo de la consulta")
  return df_banco[df_banco['education']=='secondary'][['contact','housing']].head()

seccion1_f(df_banco)