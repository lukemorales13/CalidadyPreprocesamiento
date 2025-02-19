import pandas as pd
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
def seccion1_d(df):
  """Resuelve la pregunta:
  ¿Qué instrucción de pandas usas para filtrar los registros de los
  cuentahabientes mayores de 50 años cuyo trabajo es del área de
  Administración?"""
  print("""¿Qué instrucción de pandas usas para filtrar los registros de los
  cuentahabientes mayores de 50 años cuyo trabajo es del área de
  Administración? \n""")
  print("R = df_banco[(df_banco['age']>50) & (df_banco['job']=='management')] \n Se muestra un ejemplo del resultado")
  return df[(df['age']>50) & (df['job']=='management')].head()

seccion1_d(df_banco)