
import pandas as pd


# - Una 

def filtrar_x_fechas(df, columna, fecha_inicio, fecha_fin):

    '''- Función que permite filtrar un DataFrame por fechas.
     - Parámetros:  indicar dataframe, columna para filtrar, fecha inicio y fecha fin. 
     - Retornar un DataFrame.'''


    return df[(df[columna] >= fecha_inicio) and (df[columna] <= fecha_fin)]



def generar_reporte(df, filas, columnas, valores, operacion):
    '''- Función que permite generar reportes.
     - Depende de parámetros de entrada como dataframe, filas, columnas, valores y medida (funcion_agrupadora). 
     - Debe utilizar fill_value = 0.
     - Retorna un DataFrame pivotado.'''
    reporte = pd.pivot_table(df, index=filas, columns=columnas, values=valores, aggfunc=operacion, fill_value=0)

    return reporte



def escribir_en_bbdd(df, nombre_tabla, engine, if_exists='fail'):
    '''- Función que permite escribir en la base de datos a través del guardado de un DataFrame.
    - Depende de parámetros de entrada como DataFrame, nombre de la tabla, engine y comportamiento en caso de que exista la tabla (if_exists).
    - Ojo: no se usa RETURN '''

    df.to_sql(nombre_tabla,engine, if_exists=if_exists)

