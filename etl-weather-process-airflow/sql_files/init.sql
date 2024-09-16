-- Crear esquema si no existe
CREATE SCHEMA IF NOT EXISTS weather_data_schema;

-- Crear tabla si no existe
CREATE TABLE IF NOT EXISTS weather_data_schema.weather_data (
    city VARCHAR(50),
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity INTEGER,
    pressure INTEGER,
    weather VARCHAR(100),
    PRIMARY KEY (city, timestamp)
);
