"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import datetime
import re

def clean_data():
    
    #leer dataframe
    df = pd.read_csv("solicitudes_credito.csv", sep=";",  index_col = 0)

    
    
    #Eliminar  NA y duplicados
    df.dropna(axis = 0, inplace = True)
   

    
    #titulos y las columnas 
    for column in df.columns:
        if df[column].dtypes == object:
            df[column] = df[column].str.lower()
            df[column] = df[column].str.replace('-', ' ')
            df[column] = df[column].str.replace('_', ' ')

    #montos enteros
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    #fecha en formato correcto
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(
        lambda x: datetime.datetime.strptime(x, '%Y/%m/%d') 
        if re.match('^\d{4}\/', x) 
        else datetime.datetime.strptime(x, '%d/%m/%Y')
    )
    df.drop_duplicates(inplace = True)
    

    return df

