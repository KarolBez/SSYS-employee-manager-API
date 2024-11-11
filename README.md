SSYS Employee Manager
SSYS Employee Manager é uma API para gerenciar informações de funcionários e gerar relatórios. A aplicação fornece endpoints para CRUD de funcionários, relatórios de faixa etária e salarial, além de autenticação de acesso para maior segurança.


1-Instalação
2-Configuração
3-Como Usar
4-Relatórios
5-Tecnologias Utilizadas
6-Execução

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



4-Configuração da Instância:
  •Instale Docker e Docker Compose na VM.

5-tecnologias Utilizadas:
•Django e Django REST Framework - Framework para criação de APIs.
•Docker - Containerização da aplicação.
•PostgreSQL - Banco de dados.



