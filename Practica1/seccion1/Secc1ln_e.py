import pandas as pd
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
def seccion1_e(df):
  "Convierte la variable loan a numérica usando dummy"
  df = pd.get_dummies(df, columns=['loan'], prefix="loan", drop_first=True)
  return df

df_banco = seccion1_e(df_banco)
df_banco.head()
