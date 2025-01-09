import pandas as pd
import numpy as np

def preprocessor_data(data:dict, columns_to_drop:list)->pd.DataFrame:
    """
    Preprocesa los datos eliminando columnas específicas, eliminando duplicados 
    y agregando una columna objetivo basada en la columna 'num'.

    Args:
        data (dict): Diccionario con los datos a procesar, donde las claves son nombres de columnas.
        columns_to_drop (list): Lista de nombres de columnas a eliminar. Si una columna no existe, se ignora.

    Returns:
        pd.DataFrame: DataFrame procesado con las columnas eliminadas, sin duplicados 
                      y con la columna objetivo 'Flag_problem_cardiaco' agregada.

    Raises:
        Exception: Si ocurre un error durante el procesamiento de los datos.
    """   
    try:
        df = pd.DataFrame([data])
        df = df.drop(columns=columns_to_drop, errors='ignore')  # Evita error si una columna no existe
        df = df.drop_duplicates()
        # Agregar la columna objetivo ('Flag_problem_cardiaco') en base a la columna 'num'
        df[target_column] = df['num'].apply(lambda x: 0 if x == 0 else 1)
        target = df[target_column] if target_column else None
        return df
    
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        raise
