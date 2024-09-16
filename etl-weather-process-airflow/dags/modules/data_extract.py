import os
import logging
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv('API_KEY')
CITIES = ['Tunuyán', 'Mendoza', 'Buenos Aires', 'Córdoba', 'Rosario', 'La Plata', 
          'Mar del Plata', 'San Miguel de Tucumán', 'Salta', 'Santa Fe']
API_URL_TEMPLATE = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
MIN_TEMPERATURE = -50
MAX_TEMPERATURE = 60

def extraer_data():
    """
    Función que extrae datos del clima de diversas ciudades desde la API de OpenWeatherMap.
    Retorna un DataFrame de Pandas con los datos obtenidos.
    """
    weather_data_list = []
    
    for city in CITIES:
        api_url = API_URL_TEMPLATE.format(city=city, api_key=API_KEY)
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Verificar si la respuesta es exitosa
            weather_data = response.json()

            # Validación de existencia de datos clave en la respuesta
            if 'main' in weather_data and 'weather' in weather_data:
                # Convertir temperatura de Kelvin a Celsius
                temperature = weather_data['main'].get('temp', 0) - 273.15
                
                # Validar temperatura
                if MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
                    humidity = weather_data['main'].get('humidity')
                    pressure = weather_data['main'].get('pressure')
                    weather_description = weather_data['weather'][0].get('description', 'Unknown')

                    # Validar que los datos sean completos
                    if humidity is not None and pressure is not None:
                        weather_data_list.append({
                            'city': city,
                            'temperature': round(temperature, 2),
                            'humidity': humidity,
                            'pressure': pressure,
                            'weather': weather_description,
                            'timestamp': datetime.now()
                        })
                    else:
                        logger.warning(f"Datos incompletos para {city}: Humidity o Pressure es None")
                else:
                    logger.warning(f"Temperatura fuera del rango para {city}: {temperature}°C")
            else:
                logger.warning(f"Datos meteorológicos incompletos para {city}")
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al obtener datos para {city}: {e}")

    # Convertir la lista de datos a un DataFrame de Pandas
    df = pd.DataFrame(weather_data_list)
    logger.info(f"Se han obtenido datos de {len(df)} ciudades.")
    
    return df
