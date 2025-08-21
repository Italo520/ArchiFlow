# project_service/Dockerfile (VERSÃO CORRIGIDA)

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app

# Copia e instala as dependências primeiro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta local para um subdiretório DENTRO do contêiner
COPY . ./project_service/

# Expõe a porta
EXPOSE 8002

# Executa o Gunicorn, dizendo a ele para entrar no subdiretório primeiro
CMD ["gunicorn", "--chdir", "project_service", "--bind", "0.0.0.0:8000", "wsgi:application"]