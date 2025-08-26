# Usa la imagen base de Python
FROM python:3.11-slim

# Instala debugpy para la depuración
RUN pip install debugpy

# Crea el directorio de la aplicación
WORKDIR /workspace

# Copia el requirements.txt
COPY ./requirements.txt ./requirements.txt

# Instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Al final, define el comando por defecto (lo podemos sobreescribir con docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
