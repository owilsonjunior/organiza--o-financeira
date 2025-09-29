# Usa uma imagem base do Node.js para construir o aplicativo
FROM node:18-alpine

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de configuração do Node.js
COPY package.json ./

# Instala as dependências do projeto
RUN npm install

# Copia o restante dos arquivos do projeto
COPY . .

# Expõe a porta que o aplicativo React irá rodar
EXPOSE 3000

# Comando para iniciar o servidor de desenvolvimento
CMD ["npm", "start"]