SSYS Employee Manager API
A SSYS Employee Manager API é uma aplicação para gerenciar informações de funcionários da SSYS, com operações CRUD, autenticação baseada em token e geração de relatórios de idade e faixa salarial.

--Índice:
•Descrição do Projeto
•Pré-requisitos
•Instalação e Configuração
•Configuração do Banco de Dados
•Autenticação
•Endpoints da API
•Testando a API
•Executando com Docker
•Possíveis Erros e Soluções
•Descrição do Projeto
•O projeto SSYS Employee Manager API permite:

Criar, listar, atualizar e deletar funcionários (CRUD).
Gerar relatórios de idade (mais jovem, mais velho e média).
Gerar relatórios de faixa salarial (menor, maior e média).
Controlar o acesso à API com autenticação por token.
Pré-requisitos
Para rodar o projeto localmente, você precisa dos seguintes softwares instalados:

Python 3.10+
Django 4.2+
Django REST Framework
djangorestframework-authtoken
Docker e Docker Compose (opcional para ambiente com container)
Instalação e Configuração
Clone o repositório em sua máquina local:

bash
Copiar código
git clone https://github.com/seu_usuario/ssys-employee-manager.git
cd ssys-employee-manager
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Instale as dependências do projeto:

bash
Copiar código
pip install -r requirements.txt
Configuração do Banco de Dados
Execute as migrações do banco de dados para configurar o banco inicial:

bash
Copiar código
python manage.py migrate
Crie um superusuário para acessar o Django Admin:

bash
Copiar código
python manage.py createsuperuser
Inicie o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
A API estará acessível em http://localhost:8000.

Autenticação
Esta API usa autenticação por Token para proteger os endpoints. Siga os passos abaixo para gerar e usar um token:

Obter Token: Envie uma requisição POST para o endpoint /api-token-auth/ com o username e password do usuário.

Exemplo de requisição cURL:

bash
Copiar código
curl -X POST -d "username=seu_usuario&password=sua_senha" http://localhost:8000/api-token-auth/
Resposta esperada:

json
Copiar código
{
  "token": "seu_token_aqui"
}
Usar Token para autenticação: Inclua o token no cabeçalho Authorization das requisições protegidas, no formato Token <seu_token_aqui>.

Exemplo no Postman:
makefile
Copiar código
Key: Authorization
Value: Token seu_token_aqui
Endpoints da API
1. CRUD de Funcionários
GET /employees/ - Lista todos os funcionários.
POST /employees/ - Cria um novo funcionário.
GET /employees/{id}/ - Mostra detalhes de um funcionário específico.
PUT /employees/{id}/ - Atualiza as informações de um funcionário.
DELETE /employees/{id}/ - Remove um funcionário.
Exemplo de Requisição POST para /employees/
json
Copiar código
{
    "name": "Anakin Skywalker",
    "email": "skywalker@ssys.com.br",
    "department": "Architecture",
    "salary": 4000.00,
    "birth_date": "1983-01-01"
}
2. Endpoints de Relatórios
GET /reports/employees/age/ - Relatório de idade, incluindo o mais jovem, o mais velho e a média de idade.

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
GET /reports/employees/salary/ - Relatório salarial, com o menor, o maior e a média salarial.

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
Testando a API
Use ferramentas como Postman ou cURL para testar os endpoints da API.

Exemplo de Requisição cURL para listar funcionários:
bash
Copiar código
curl -H "Authorization: Token <seu_token_aqui>" http://localhost:8000/employees/
Exemplo de Requisição cURL para o relatório de idade:
bash
Copiar código
curl -H "Authorization: Token <seu_token_aqui>" http://localhost:8000/reports/employees/age/
Executando com Docker
Arquivo docker-compose.yml: O projeto inclui um docker-compose.yml para facilitar o ambiente de desenvolvimento com Docker.

Suba o ambiente de desenvolvimento com Docker Compose:

bash
Copiar código
docker-compose up --build
Isso irá iniciar o servidor na porta 8000, acessível em http://localhost:8000.

Para encerrar os containers:

bash
Copiar código
docker-compose down
Possíveis Erros e Soluções
Erro ao obter Token: Verifique se o usuário existe e as credenciais estão corretas.
Erro 401 Unauthorized: Assegure-se de que o token está incluído corretamente no cabeçalho Authorization.
Erro de conexão: Verifique se o servidor está em execução e disponível na porta 8000.
Este guia cobre os passos necessários para configurar, executar e testar a SSYS Employee Manager API.
