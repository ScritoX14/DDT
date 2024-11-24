# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el contenido del proyecto al contenedor
COPY . .

# Establecer el comando de inicio
CMD ["flask", "run", "--host=0.0.0.0", "--port=10000"]
