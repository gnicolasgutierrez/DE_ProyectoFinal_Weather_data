import pandas as pd

def transformar_data(df):
    # Redondear las temperaturas a dos decimales
    df['temperature'] = df['temperature'].apply(lambda x: round(x, 2))
    
    # Agregar columna de diferencia con respecto al promedio global (Celsius)
    GLOBAL_AVERAGE_TEMP = 15  # Temperatura global promedio (en °C)
    df['temp_diff_from_global'] = df['temperature'] - GLOBAL_AVERAGE_TEMP
    
    # Categorizar temperaturas en 'frío', 'templado' y 'caliente'
    def categorize_temperature(temp):
        if temp < 0:
            return 'frío'
        elif 0 <= temp <= 25:
            return 'templado'
        else:
            return 'caliente'

    df['temp_category'] = df['temperature'].apply(categorize_temperature)
    
    # Eliminar filas con datos faltantes
    df.dropna(subset=['temperature', 'humidity', 'pressure'], inplace=True)
    
    # Normalización de la temperatura (valores entre 0 y 1)
    df['normalized_temperature'] = (df['temperature'] - df['temperature'].min()) / (df['temperature'].max() - df['temperature'].min())
    
    return df
