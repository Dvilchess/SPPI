# Usa la imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia y instala las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el código del proyecto
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
