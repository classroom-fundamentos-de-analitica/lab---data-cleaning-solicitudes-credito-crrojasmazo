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
    df = pd.read_csv("solicitudes_credito.csv", sep=";" )

    
    
    #Eliminar  NA y duplicados
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)


    #titulos y las columnas 
    for column in df.columns:
        if df[column].dtypes == object:
            df[column] = df[column].str.lower()
            df[column] = df[column].str.replace('-', ' ')
            df[column] = df[column].str.replace('_', ' ')


    #fecha en formato correcto
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(
        lambda x: datetime.datetime.strptime(x, '%Y/%m/%d') 
        if re.match('^\d{4}\/', x) 
        else datetime.datetime.strptime(x, '%d/%m/%Y')
    )

    return df
