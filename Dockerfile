# 1º Estágio: Build - Usamos uma imagem completa para instalar as dependências
FROM python:3.10-slim as build-stage

# Variáveis de ambiente para otimizar o comportamento do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências de build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de dependências para o container
COPY requirements.txt .

# Instalar dependências (incluindo TensorFlow) com cache desabilitado
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 2º Estágio: Final - Usamos uma imagem menor e copiamos apenas o necessário
FROM python:3.10-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir diretório de trabalho
WORKDIR /app

# Instalar runtime dependencies mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar apenas as dependências instaladas do 1º estágio
COPY --from=build-stage /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin

# Copiar o código da aplicação para o contêiner final
COPY . .

# Expor a porta da aplicação Flask
EXPOSE 5000

# Usar Gunicorn para rodar o servidor Flask em produção
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]