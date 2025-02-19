import pandas as pd
# Lectura del conjunto de datos.df_banco
df_banco = pd.read_csv("Practica1/seccion1/banco.csv")
def seccion1_b(df):
  """
  Localiza los datos faltantes y los imputa con alguna técnica vista
  Parámetro:
    - df: DataFrame con datos numéricos.
  """
  # importamos is_integer_dtype para verificar si una columna es
  from pandas.api.types import is_integer_dtype
  for i in df.columns:
    if df[i].isnull().sum() > 0:
      print(f"La columna {i} contiene {df[i].isnull().sum()} nulos")
  if not df.isnull().any().any():
    print("No hay nulos \n")
  else:
    for column in df.columns:
      if df[column].isnull().sum() > 0:
        if is_integer_dtype(df[column]):
          df[column].fillna(df[column].median(), inplace=True)
        else:
          df[column].fillna(df[column].mode()[0], inplace=True)
    print("Valores nulos imputados \n")
  print("Se revisa si existen valores 'inusuales' o que pudieran ser considerados como nulos, por ejemplo '-'")
  # revisamos si alguna columna no numérica tiene valores inusuales, dado que no hay nulos
  for columna in df.columns:
    if is_integer_dtype(df[columna]):
      pass
    else:
      print("Campo: ",columna)
      print(f"Los distintos valores que contiene la columna {columna} son: ")
      print(df[columna].unique())
      print(f" y son {len(df[columna].unique())} valores distintos \n")

seccion1_b(df_banco)