SSYS Employee Manager
SSYS Employee Manager é uma API para gerenciar informações de funcionários e gerar relatórios. A aplicação fornece endpoints para CRUD de funcionários, relatórios de faixa etária e salarial, além de autenticação de acesso para maior segurança.


1-Instalação
2-Configuração
3-Como Usar
4-Endpoints
5-Funcionários (CRUD)
6-Relatórios
7-Tecnologias Utilizadas


1-Instalação:
•Clone o repositório:
  git clone https://github.com/seu-usuario/ssys-employee-manager.git
  cd ssys-employee-manager
  
 •Configuração do Docker: Certifique-se de ter o Docker e Docker Compose instalados. Utilize o comando abaixo para iniciar os contêineres em ambiente de desenvolvimento:
    docker-compose up --build
    Migrações do banco de dados: Após iniciar o contêiner, execute as migrações para criar as tabelas do banco de dados:
    docker-compose exec web python manage.py migrate
  •Criação de Superusuário: Para acessar a API, crie um superusuário com o comando:
    docker-compose exec web python manage.py createsuperuser

2-Configuração:
  No arquivo .env, configure as variáveis de ambiente necessárias:
  DATABASE_URL: URL de conexão com o banco de dados.
  SECRET_KEY: Chave secreta do Django para segurança.
  DEBUG: Configuração para o modo de depuração.
  ALLOWED_HOSTS: Hosts permitidos para acessar a aplicação.
  Como Usar
  A aplicação pode ser acessada em http://localhost:8000 quando iniciada com Docker. Use um cliente como Postman ou cURL para fazer requisições aos endpoints.

3-Endpoints
  •Funcionários (CRUD)
    •Listar Funcionários
      GET /employees/
        Exemplo de Resposta:
        json
        Copiar código
        [
          {
            "id": 1,
            "name": "Anakin Skywalker",
            "email": "skywalker@ssys.com.br",
            "department": "Architecture",
            "salary": "4000.00",
            "birth_date": "1983-01-01"
          },
          ...
        ]
      • Criar Funcionário
         POST /employees/
          Exemplo de Request Body:
          json
          Copiar código
          {
            "name": "Leia Organa",
            "email": "organa@ssys.com.br",
            "department": "DevOps",
            "salary": 5000,
            "birth_date": "1980-01-01"
          }
          
  •Atualizar funcionário
    PUT /employees/<id>/
        Exemplo de Request Body:
        json
        Copiar código
        {
          "department": "Management"
        }
 •Deletar Funcionário
  DELETE /employees/<id>/
  
 •Detalhar Funcionário
    GET /employees/<id>/

•Relatórios
Relatório de Idade
  GET /reports/employees/age/
    Exemplo de Resposta:
    json
    Copiar código
    {
      "younger": {
        "id": 1,
        "name": "Anakin Skywalker",
        "email": "skywalker@ssys.com.br",
        "department": "Architecture",
        "salary": "4000.00",
        "birth_date": "1983-01-01"
      },
      "older": {
        "id": 2,
        "name": "Obi-Wan Kenobi",
        "email": "kenobi@ssys.com.br",
        "department": "Back-End",
        "salary": "3000.00",
        "birth_date": "1977-01-01"
      },
      "average": 40.0
    }

•Relatório de Salário
  GET /reports/employees/salary/
    Exemplo de Resposta:
    json
    Copiar código
    {
      "lowest": {
        "id": 2,
        "name": "Obi-Wan Kenobi",
        "email": "kenobi@ssys.com.br",
        "department": "Back-End",
        "salary": "3000.00",
        "birth_date": "1977-01-01"
      },
      "highest": {
        "id": 3,
        "name": "Leia Organa",
        "email": "organa@ssys.com.br",
        "department": "DevOps",
        "salary": "5000.00",
        "birth_date": "1980-01-01"
      },
      "average": 4000.00
    }


4-Configuração da Instância:
  •Instale Docker e Docker Compose na VM.

6-tecnologias Utilizadas:
•Django e Django REST Framework - Framework para criação de APIs.
•Docker - Containerização da aplicação.
•PostgreSQL - Banco de dados.

