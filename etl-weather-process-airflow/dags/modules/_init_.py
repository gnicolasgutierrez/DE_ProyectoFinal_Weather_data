# Este archivo inicializa el módulo del proyecto, permitiendo que se importen
# las siguientes funciones desde otros archivos del proyecto.

# get_defaultairflow_args: Obtiene los argumentos predeterminados que se usarán en cada DAG.
from .utils import get_defaultairflow_args

# extraer_data: Función para extraer datos, en este caso, desde la API de OpenWeatherMap.
from .data_extract import extraer_data

# cargar_data: Función para cargar los datos procesados en Redshift.
from .data_load import cargar_data

# transformar_data: Función para transformar los datos después de la extracción.
from .data_transform import transformar_data

# send_email: Función para enviar correos electrónicos con alertas o notificaciones.
from .mail_sender import send_email
