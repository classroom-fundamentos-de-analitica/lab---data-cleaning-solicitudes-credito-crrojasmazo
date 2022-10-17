"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re

def clean_data():
  with open('clusters_report.txt') as report:
    row = report.readlines()
  row = row[4:] #borrar primeras filas
  clusters = []
  cluster = [0, 0, 0, '']
  for fila in row:
    #limpieza
    if re.match('^ +[0-9]+ +', fila):
      number, cantidad, porcentaje, *words = fila.split()
      cluster[0] = int(number)
      cluster[1] = int(cantidad)
      cluster[2] = float(porcentaje.replace(',','.'))
      words = ' '.join(words)
      cluster[3] += words
    elif re.match('^\n', fila) or re.match('^ +$', fila):
      cluster[3] = cluster[3].replace('.', '') 
      clusters.append(cluster)
      cluster = [0, 0, 0, '']
    elif re.match('^ +[a-z]', fila):
      words = fila.split()
      words = ' '.join(words)
      cluster[3] += ' ' + words
      #exportar
  df = pd.DataFrame (clusters, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
  return df
