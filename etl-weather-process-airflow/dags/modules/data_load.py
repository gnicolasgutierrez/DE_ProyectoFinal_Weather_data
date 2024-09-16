import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Función para cargar los datos en la base de datos
def cargar_data(df):
    """
    Carga los datos extraídos y transformados en la base de datos Redshift.
    
    Parámetros:
    df (DataFrame): DataFrame con los datos a cargar en la base de datos.
    """
    # Construir la URL de conexión a la base de datos usando las variables de entorno
    DATABASE_URL = f"redshift+psycopg2://{os.getenv('USER')}:{os.getenv('PASSWORD')}@" \
                   f"{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DBNAME')}"

    # Crear el motor para la conexión a la base de datos
    engine = create_engine(DATABASE_URL)

    try:
        # Cargar los datos en Redshift utilizando el método to_sql de Pandas
        # Se asume que la tabla en Redshift ya existe y tiene la estructura adecuada.
        df.to_sql('weather_data', engine, index=False, if_exists='append')  # 'append' agrega los datos sin borrar la tabla
        logger.info(f"Datos insertados exitosamente en Redshift. Se cargaron {len(df)} registros.")
    except Exception as e:
        # Manejar cualquier error durante la inserción
        logger.error(f"Error al insertar datos en Redshift: {e}")

 
