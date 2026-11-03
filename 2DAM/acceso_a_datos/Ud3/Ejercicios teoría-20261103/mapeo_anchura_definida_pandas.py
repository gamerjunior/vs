
import pandas as pd

def ancho_fijo_pandas(fichero_origen3, anchos):
    return pd.read_fwf(fichero_origen3, widths=anchos)

anchos = [6, 16, 7]  # Num. Amigos Nombre Salario

fichero_origen3 = "ejemplo_ancho_fijo3.txt"
info_df = ancho_fijo_pandas(fichero_origen3, anchos)
print(info_df)
print(info_df.mean(axis=0, numeric_only=True))