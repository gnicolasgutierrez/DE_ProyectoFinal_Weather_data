from datetime import timedelta

def get_defaultairflow_args():
    """
    Retorna un diccionario con los argumentos predeterminados para los DAGs en Airflow.
    """
    return {
        'owner': 'airflow',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }
