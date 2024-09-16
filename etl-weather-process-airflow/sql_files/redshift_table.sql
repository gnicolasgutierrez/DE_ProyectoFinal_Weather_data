-- Eliminar tabla si existe
DROP TABLE IF EXISTS ngutierrez_coderhouse.weather_data;

-- Crear tabla
CREATE TABLE ngutierrez_coderhouse.weather_data (
    city VARCHAR(50),
    timestamp TIMESTAMP,
    temperature NUMERIC,
    humidity INTEGER,
    pressure INTEGER,
    weather VARCHAR(100),
    PRIMARY KEY (city, timestamp)
);
