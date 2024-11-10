# Utiliza uma imagem Python
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copia o código da aplicação
COPY . /app

# Expõe a porta da aplicação
EXPOSE 8000

# Comando de inicialização do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

