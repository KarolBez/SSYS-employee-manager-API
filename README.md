SSYS Employee Manager API
O SSYS Employee Manager API é uma aplicação desenvolvida para gerenciar informações de funcionários e relatórios, com autenticação para acesso seguro. A API permite operações de CRUD (Criar, Ler, Atualizar e Excluir) para gerenciar funcionários e possui endpoints para relatórios de idade e faixa salarial.

Sumário
Requisitos
Configuração do Projeto
Executando o Projeto
Endpoints
Autenticação
Exemplos de Requisições
Requisitos
Docker: Certifique-se de que o Docker está instalado em seu sistema.
Docker Compose: O Docker Compose deve estar disponível para facilitar a orquestração dos containers.
Configuração do Projeto
1. Clone o Repositório
Primeiro, clone este repositório em sua máquina local:

bash
Copiar código
git clone <URL-do-repositório>
cd ssys-employee-manager-api
2. Estrutura do Projeto
No diretório raiz do projeto, você encontrará os seguintes arquivos importantes:

Dockerfile: Define a imagem Docker para o projeto.
docker-compose.yml: Orquestra os serviços necessários (web e banco de dados).
requirements.txt: Lista de dependências do projeto.
manage.py: Comando principal para a aplicação Django.
3. Configurar Variáveis de Ambiente
Para configurar as variáveis de ambiente, crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

plaintext
Copiar código
# Django settings
DJANGO_SECRET_KEY='sua_chave_secreta'
DJANGO_DEBUG=True

# Database settings
POSTGRES_DB=ssys_db
POSTGRES_USER=ssys_user
POSTGRES_PASSWORD=ssys_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
Executando o Projeto
1. Construir e Iniciar os Containers
Para iniciar a aplicação e o banco de dados usando Docker Compose, execute:

bash
Copiar código
docker-compose up -d --build
Esse comando criará e iniciará os containers em segundo plano.

2. Aplicar Migrações do Banco de Dados
Depois que os containers estiverem ativos, execute as migrações do Django para configurar o banco de dados:

bash
Copiar código
docker-compose exec web python manage.py migrate
3. Criar um Superusuário (opcional)
Para acessar o Django Admin ou autenticar usuários, você pode criar um superusuário:

bash
Copiar código
docker-compose exec web python manage.py createsuperuser
Endpoints
A API possui os seguintes endpoints principais:

1. Employees CRUD
GET /employees/: Listar todos os funcionários.
POST /employees/: Criar um novo funcionário.
GET /employees/{id}/: Detalhes de um funcionário específico.
PUT /employees/{id}/: Atualizar dados de um funcionário.
DELETE /employees/{id}/: Excluir um funcionário.
2. Relatórios
GET /reports/employees/age/: Relatório de idade dos funcionários (mais novo, mais velho, média de idade).
GET /reports/employees/salary/: Relatório salarial dos funcionários (menor, maior e média salarial).
Autenticação
Esta API utiliza Token Authentication. Para acessar os endpoints protegidos, é necessário:

Obter um token de autenticação enviando uma requisição POST para /api-token-auth/ com username e password no corpo da requisição.

Inclua o token no cabeçalho Authorization nas próximas requisições, com o formato:

makefile
Copiar código
Authorization: Token SEU_TOKEN_AQUI
Exemplos de Requisições
1. Autenticação
Para obter um token de autenticação:

bash
Copiar código
curl -X POST http://localhost:8000/api-token-auth/ \
     -d "username=seu_usuario" \
     -d "password=sua_senha"
Resposta esperada:

json
Copiar código
{
    "token": "seu_token_gerado"
}
2. Listar Funcionários
Requisição:

bash
Copiar código
curl -X GET http://localhost:8000/employees/ \
     -H "Authorization: Token SEU_TOKEN_AQUI"
3. Criar um Funcionário
Requisição:

bash
Copiar código
curl -X POST http://localhost:8000/employees/ \
     -H "Authorization: Token SEU_TOKEN_AQUI" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Anakin Skywalker",
           "email": "skywalker@ssys.com.br",
           "department": "Architecture",
           "salary": "4000.00",
           "birth_date": "1983-01-01"
         }'
4. Relatório de Idade
Requisição:

bash
Copiar código
curl -X GET http://localhost:8000/reports/employees/age/ \
     -H "Authorization: Token SEU_TOKEN_AQUI"
Resposta esperada:

json
Copiar código
{
    "younger": {
        "id": "1",
        "name": "Anakin Skywalker",
        "email": "skywalker@ssys.com.br",
        "department": "Architecture",
        "salary": "4000.00",
        "birth_date": "1983-01-01"
    },
    "older": {
        "id": "2",
        "name": "Obi-Wan Kenobi",
        "email": "kenobi@ssys.com.br",
        "department": "Back-End",
        "salary": "3000.00",
        "birth_date": "1977-01-01"
    },
    "average": "40.00"
}
5. Relatório Salarial
Requisição:

bash
Copiar código
curl -X GET http://localhost:8000/reports/employees/salary/ \
     -H "Authorization: Token SEU_TOKEN_AQUI"
Resposta esperada:

json
Copiar código
{
    "lowest": {
        "id": "2",
        "name": "Obi-Wan Kenobi",
        "email": "kenobi@ssys.com.br",
        "department": "Back-End",
        "salary": "3000.00",
        "birth_date": "1977-01-01"
    },
    "highest": {
        "id": "3",
        "name": "Leia Organa",
        "email": "organa@ssys.com.br",
        "department": "DevOps",
        "salary": "5000.00",
        "birth_date": "1980-01-01"
    },
    "average": "4000.00"
}
Encerrando o Ambiente
Para parar os containers e liberar os recursos:

bash
Copiar código
docker-compose down
Esse README cobre desde a configuração inicial até o uso dos endpoints da API.






