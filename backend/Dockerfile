# Usa uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Comando para rodar o servidor Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]