# 📘 Assignment: Construindo APIs REST com framework FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a criar uma API REST completa usando FastAPI. Você desenvolverá endpoints para gerenciar recursos usando os métodos HTTP (GET, POST, PUT, DELETE), implementará validação de dados e documentação automática com Swagger.

## 📝 Tasks

### 🛠️ Criar uma API básica com FastAPI

#### Description
Configure um projeto FastAPI básico com um endpoint GET que retorna informações sobre a API. Este é o primeiro passo para construir qualquer aplicação com FastAPI.

#### Requirements
Completed program should:

- Importar e configurar a aplicação FastAPI
- Criar um endpoint GET simples que retorna um dicionário com informações da API
- Usar type hints do Python para documentar tipos de entrada e saída
- Executar a aplicação com `uvicorn` e acessar a documentação em `/docs`

### 🛠️ Implementar operações CRUD para gerenciar livros

#### Description
Crie endpoints para criar, ler, atualizar e deletar informações de livros. Implemente um modelo Pydantic para validação automática dos dados enviados na requisição.

#### Requirements
Completed program should:

- Definir um modelo Pydantic `Livro` com campos: `id`, `titulo`, `autor`, `ano_publicacao` e `preco`
- Implementar endpoint POST `/livros` para criar um novo livro
- Implementar endpoint GET `/livros` para listar todos os livros
- Implementar endpoint GET `/livros/{id}` para obter um livro específico
- Implementar endpoint PUT `/livros/{id}` para atualizar um livro existente
- Implementar endpoint DELETE `/livros/{id}` para remover um livro
- Usar uma lista em memória para armazenar os livros durante a execução

### 🛠️ Adicionar validação de dados e tratamento de erros

#### Description
Implemente validação de dados usando Pydantic com restrições personalizadas e retorne mensagens de erro apropriadas quando dados inválidos são enviados.

#### Requirements
Completed program should:

- Validar que o `titulo` não está vazio e tem no mínimo 3 caracteres
- Validar que o `preco` é um número positivo
- Validar que `ano_publicacao` está dentro de um intervalo razoável (1000 até o ano atual)
- Retornar status HTTP 404 quando um livro não é encontrado
- Retornar status HTTP 422 quando os dados enviados são inválidos
- Usar `HTTPException` para tratamento de erros apropriado

### 🛠️ Adicionar filtros e paginação (opcional)

#### Description
Implemente funcionalidades avançadas como filtros por autor e paginação na listagem de livros para criar uma API mais robusta e escalável.

#### Requirements
Completed program should:

- Aceitar parâmetro query `autor` para filtrar livros por autor
- Implementar paginação com parâmetros `skip` e `limit`
- Retornar o número total de livros e livros na página
- Manter compatibilidade com os endpoints anteriores
