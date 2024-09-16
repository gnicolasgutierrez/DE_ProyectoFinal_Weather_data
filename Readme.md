    # Proyecto Final de Data Engineer

    ## Nota



    ## Instrucciones de Uso

    Para arrancar el proyecto, escribe en la terminal:

    ```bash
    docker-compose up

    ## Descripción del Proyecto
    Este proyecto de ingeniería de datos está diseñado para extraer, transformar y cargar datos meteorológicos en una base de datos Redshift utilizando Apache Airflow para la orquestación de tareas.

    ## Funcionamiento del Proyecto
    1. Extracción de Datos: Los datos meteorológicos se extraen desde la API de OpenWeatherMap. Esta etapa obtiene los datos más recientes para una serie de ciudades definidas en la configuración.

    2. Transformación de Datos: Los datos extraídos son transformados para ajustarse al formato requerido, incluyendo la conversión de temperaturas a grados Celsius y el redondeo de valores.

    3. Carga de Datos: Los datos transformados se cargan en una base de datos Redshift. Se maneja la creación de la tabla necesaria, la inserción en bloques y la eliminación de registros duplicados.

    ## Orquestación con Apache Airflow:

    1. Configuración: El proyecto utiliza Apache Airflow para gestionar el flujo de trabajo ETL. Este está configurado para ejecutar el proceso diariamente.
    2. Ejecución: Para probar el funcionamiento del DAG, accede a la interfaz de usuario de Apache Airflow con las credenciales predeterminadas (usuario: airflow, contraseña: airflow). Desde allí, puedes activar manualmente el DAG para verificar su funcionamiento.
    ## Estructura del Proyecto
    . dags/

     . dag_etl.py: Define el DAG (Directed Acyclic Graph) para Apache Airflow que orquesta el proceso ETL. Utiliza el operador PythonOperator para ejecutar la función etl() del módulo modules/main.py en un intervalo diario.
    . modules/

     . __init__.py: Inicializa el módulo del proyecto, permitiendo que se importen las funciones desde otros archivos del proyecto.
     . data_extract.py: Contiene la función extraer_data(), que extrae datos meteorológicos desde la API de OpenWeatherMap y los organiza en un DataFrame de Pandas.
     . data_load.py: Contiene la función cargar_data(), que carga el DataFrame transformado en una tabla en Redshift.
     . data_transform.py: Define la función transformar_data(), que transforma el DataFrame extraído, convirtiendo las temperaturas a grados Celsius y redondeando los valores.
     . mail_sender.py: Este archivo gestiona el envío de correos electrónicos para notificar el estado del DAG en Airflow.
     . utils.py: Contiene la función get_defaultairflow_args(), que proporciona los argumentos predeterminados para los DAGs de Airflow.
    . sql_files/

     . init.sql: Script SQL para crear el esquema y la tabla en la base de datos Redshift.
     . redshift_table.sql: Script SQL para crear la tabla en la base de datos Redshift.
    . docker-compose.yml: Configura los servicios necesarios para el proyecto, incluyendo la base de datos y el entorno de Airflow, utilizando Docker Compose.

    . Taskfile.yml: Define tareas para la configuración y manejo del proyecto, incluyendo la inicialización, el arranque y la limpieza del entorno.

    . .env: Archivo de configuración que contiene las variables de entorno necesarias para la conexión a la base de datos y el envío de correos electrónicos.

    ## Funciones y Tareas del DAG
    El DAG dag_etl.py automatiza un proceso ETL (Extracción, Transformación y Carga) de datos meteorológicos, ejecutándolo diariamente.

    ***Sistema de Alertas***
    El DAG cuenta con un sistema de alertas configurado para notificar el estado del proceso:

    . Alertas en caso de fallo: Si alguna tarea del DAG falla, se envía un correo electrónico con detalles del error.
    . Confirmaciones de éxito: Al completar correctamente todas las tareas, se envía un correo de confirmación.
    
    ***Sensores y Limpieza de Archivos Temporales***
    . Sensores: Verifican la existencia de archivos necesarios antes de continuar con las siguientes tareas.

     . extract_file_sensor: Verifica la existencia del archivo CSV extraído antes de proceder con la transformación.
     . transform_file_sensor: Verifica la existencia del archivo CSV transformado antes de cargar los datos.
    . Limpieza de Archivos Temporales: Una tarea específica elimina todos los archivos temporales generados durante el proceso.

    ***Resumen de Tareas***
    . Extracción de Datos (extract_task): Extrae los datos y los organiza en un DataFrame.
    . Transformación de Datos (transform_task): Transforma el DataFrame extraído y convierte las temperaturas.
    . Carga de Datos (load_task): Carga el DataFrame transformado en Redshift.
    . Sensores de Archivos (extract_file_sensor, transform_file_sensor): Aseguran que los archivos necesarios estén presentes antes de proceder.
    . Limpieza de Archivos Temporales (cleanup_tmp_files): Elimina archivos temporales generados durante el proceso.
    
    ##Instalación y Configuración
    ***Configuración Local del Proyecto***
    1. Clona el repositorio:

        git clone <url-del-repositorio>
        cd <nombre-del-repositorio>
    
    2. Crea un entorno virtual y actívalo:

        python -m venv venv
        Activa el entorno virtual:
     . En Windows:

        venv\Scripts\activate

     . En macOS y Linux:

        source venv/bin/activate

    3. Instala las dependencias:
     
        pip install -r requirements.txt
    
    4. Ejecuta el proyecto:

        docker-compose up
    . Configuración en GitHub Codespaces del Proyecto
        1. Abre el repositorio en GitHub Codespaces:

            Haz clic en el botón "Code" y selecciona "Open with Codespaces". Crea un nuevo Codespace.

        2. Ejecuta el proyecto:

            Ejecuta el siguiente comando en la terminal integrada de Codespaces:

             docker-compose up
             
    ##Control de Duplicados

    La generación de un ID único para el control de datos duplicados se realiza mediante un hash MD5 derivado del contenido de los datos. Esto asegura que cada registro tenga un identificador único basado en su contenido.

        import hashlib

        def generate_id(row):
         data_string = f"{row['city']}-{row['timestamp']}-{row['temperature']}-{row['humidity']}-{row['pressure']}-{row['weather']}"
         return hashlib.md5(data_string.encode()).hexdigest()
    
    ##Contribuciones
    Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

        1. Haz un fork del repositorio.
        2. Crea una rama para tu característica o corrección de errores.
        3. Envía un pull request con una descripción clara de los cambios.

    ##Licencia
    Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


    