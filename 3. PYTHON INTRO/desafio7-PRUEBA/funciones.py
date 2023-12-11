
import pandas as pd


# Primera función para filtrar por fechas
def filtrar_x_fechas(df, columna, fecha_inicio, fecha_fin):
    

    '''- Función que permite filtrar un DataFrame por fechas.
     - Parámetros:  indicar dataframe, columna para filtrar, fecha inicio y fecha fin. 
     - Retornar un DataFrame.'''

    dataframe_filtrado = df[(df[columna] >= fecha_inicio) & (df[columna] <= fecha_fin)]
    return dataframe_filtrado


# Segunda función para generar reporte
def generar_reporte(df, filas, columnas, valores, operacion):
    '''- Función que permite generar reportes.
     - Depende de parámetros de entrada como dataframe, filas, columnas, valores y medida (funcion_agrupadora). 
     - Debe utilizar fill_value = 0.
     - Retorna un DataFrame pivotado.'''
    reporte = pd.pivot_table(df, index=filas, columns=columnas, values=valores, aggfunc=operacion, fill_value=0)

    return reporte


# Tercera función para escribir en base de datos
def escribir_en_bbdd(df, nombre_tabla, engine, if_exists='fail'):
    '''- Función que permite escribir en la base de datos a través del guardado de un DataFrame.
    - Depende de parámetros de entrada como DataFrame, nombre de la tabla, engine y comportamiento en caso de que exista la tabla (if_exists).
    - Ojo: no se usa RETURN '''

    nueva_tabla = df.to_sql(nombre_tabla, engine, if_exists=if_exists)

    return nueva_tabla

