import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_email():
    """
    Envía un correo electrónico notificando que el ETL de datos meteorológicos ha sido completado exitosamente.
    """
    # Obtener las variables de entorno
    sender_email = os.getenv('SMTP_USER')
    receiver_email = os.getenv('EMAIL')
    password = os.getenv('SMTP_PASSWORD')
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = os.getenv('SMTP_PORT')
    subject = 'ETL Completed'  # Asignar un asunto predeterminado

    # Comprobar que todas las variables de entorno necesarias están presentes
    if not all([sender_email, receiver_email, password, smtp_host, smtp_port]):
        logger.error("Faltan variables de entorno necesarias para enviar el correo.")
        return

    # Crear el mensaje
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Cuerpo del mensaje
    text = "El ETL de datos meteorológicos ha sido completado exitosamente."
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        # Configurar el servidor SMTP y enviar el correo
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            if os.getenv('SMTP_STARTTLS') == 'True':
                server.starttls()  # Iniciar TLS si está habilitado
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        logger.info("Correo electrónico enviado exitosamente.")
    except Exception as e:
        # Manejar cualquier error durante el envío
        logger.error(f"Error al enviar el correo: {e}")
