# API CRUD de Programas

Esta é uma API RESTful desenvolvida com Django e Django REST Framework que permite a criação, leitura, atualização e exclusão (CRUD) de programas sendo eles filmes e séries.

## Recursos

- **Programas**: Representa filmes ou séries.

## Endpoints

- **Listar Programas**: `GET /api/programas/`
  - Retorna todos os programas cadastrados.

- **Criar Programa**: `POST /api/programas/`
  - Cria um novo programa.

- **Detalhes do Programa**: `GET /api/programas/{id}/`
  - Retorna detalhes de um programa específico.

- **Atualizar Programa**: `PUT /api/programas/{id}/`
  - Atualiza os detalhes de um programa existente.

- **Excluir Programa**: `DELETE /api/programas/{id}/`
  - Exclui um programa existente.

## Campos de Programa

- `titulo`: O título do programa.
- `tipo`: O tipo do programa, que pode ser 'Filme' ou 'Série'.
- `data_lancamento`: A data de lançamento do programa.
- `likes`: O número de curtidas que o programa recebeu.
- `dislikes`: O número de descurtidas que o programa recebeu.

## Autenticação

- A API usa autenticação básica. Os usuários devem fornecer credenciais válidas para acessar os endpoints.

## Exemplos de Uso

```http
POST /api/programas/
Content-Type: application/json

{
    "titulo": "Breaking Bad",
    "tipo": "Série",
    "data_lancamento": "2008-01-20",
    "likes": 1500,
    "dislikes": 100
}

PUT /api/programas/1/
Content-Type: application/json

{
    "likes": 1600
}

DELETE /api/programas/1

GET /api/programas/

GET /api/programas/1
````


# Requisitos

- Python 3.x

## Como Instalar e Executar

- Clone o repositório para sua máquina local:
git clone https://github.com/GustavoMarquesMartins/api-aluraflix

- Instale as dependências:
pip install -r requirements.txt

- Execute as migrações do banco de dados:
python manage.py migrate

- Crie um super usuário:
python manage.py createsuperuser

- Inicie o servidor de desenvolvimento:
python manage.py runserver

# Documentação

## URLs

- `/swagger/`
- `/redoc/`
