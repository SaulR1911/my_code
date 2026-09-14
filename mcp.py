#La salud mental es un tema a considerar# 

import pandas as pd

df=pd.read_csv("AI_Data_Analyst\INEGI_suicidio_Mexico_2022_2024.csv")
print(df.head())
print("\nCOLUMNAS:")
print(df.columns)

print("\nTipos de Datos")
print(df.dtypes) 

print(df.shape)

print("\nSuicidios por Sexo")

resultado=df.groupby("sexo")["defunciones_suicidio"].sum()

print(resultado)

print("\nSuicidios por Año")

por_anio = df.groupby("anio")["defunciones_suicidio"].sum()

print(por_anio)

total = df["defunciones_suicidio"].sum()

#   df.groupby("sexo")["defunciones_suicidio"]
 #   .sum()
  #  .sort_values(ascending=False)
#)

#porcentaje = (por_sexo / total) * 100

#print("\nPARTICIPACIÓN POR SEXO:")
#print(porcentaje.round(2))

relacion=df.groupby(["anio","sexo"])["defunciones_suicidio"].sum()
print(relacion)

df_sexo = df[df["sexo"].isin(["Hombres","Mujeres"])]
por_sexo = (
    df_sexo.groupby("sexo")["defunciones_suicidio"]
    .sum()
)

total_sexo = por_sexo.sum()

porcentaje = (por_sexo / total_sexo) * 100

print(porcentaje.round(2))
