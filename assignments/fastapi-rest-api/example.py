"""
FastAPI REST API - Exemplo Completo

Este arquivo mostra uma solução completa para a tarefa.
Estude o código para entender como construir APIs REST com FastAPI.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# Modelo Pydantic para um Livro
class Livro(BaseModel):
    """Modelo de dados para um livro"""
    id: Optional[int] = None
    titulo: str = Field(..., min_length=3, description="Título do livro (mínimo 3 caracteres)")
    autor: str = Field(..., description="Autor do livro")
    ano_publicacao: int = Field(..., ge=1000, le=datetime.now().year, description="Ano de publicação")
    preco: float = Field(..., gt=0, description="Preço do livro (maior que 0)")


class LivroResponse(Livro):
    """Modelo de resposta com ID"""
    id: int


class ListaLivrosResponse(BaseModel):
    """Modelo de resposta para listagem de livros"""
    total: int
    skip: int
    limit: int
    livros: List[LivroResponse]


# Inicializar a aplicação FastAPI
app = FastAPI(
    title="API de Gerenciamento de Livros",
    description="Uma API REST para gerenciar uma biblioteca de livros",
    version="1.0.0"
)


# Simular um banco de dados com uma lista em memória
livros_db = []
contador_id = 1


@app.get("/")
def raiz():
    """Endpoint raiz que retorna informações da API"""
    return {
        "message": "Bem-vindo à API de Gerenciamento de Livros",
        "versao": "1.0.0",
        "endpoints": {
            "GET /docs": "Documentação interativa Swagger",
            "GET /livros": "Listar todos os livros",
            "POST /livros": "Criar um novo livro",
            "GET /livros/{id}": "Obter um livro específico",
            "PUT /livros/{id}": "Atualizar um livro",
            "DELETE /livros/{id}": "Deletar um livro"
        }
    }


@app.post("/livros", response_model=LivroResponse, status_code=201)
def criar_livro(livro: Livro):
    """Criar um novo livro na biblioteca"""
    global contador_id
    
    novo_livro = livro.dict()
    novo_livro["id"] = contador_id
    contador_id += 1
    
    livros_db.append(novo_livro)
    return novo_livro


@app.get("/livros", response_model=ListaLivrosResponse)
def listar_livros(skip: int = 0, limit: int = 10, autor: Optional[str] = None):
    """
    Listar livros com suporte a filtros e paginação
    
    - **skip**: Número de livros para pular
    - **limit**: Número máximo de livros a retornar
    - **autor**: Filtrar por autor (opcional)
    """
    # Filtrar por autor se fornecido
    livros_filtrados = livros_db
    if autor:
        livros_filtrados = [l for l in livros_db if autor.lower() in l["autor"].lower()]
    
    # Aplicar paginação
    livros_paginados = livros_filtrados[skip : skip + limit]
    
    return {
        "total": len(livros_filtrados),
        "skip": skip,
        "limit": limit,
        "livros": livros_paginados
    }


@app.get("/livros/{livro_id}", response_model=LivroResponse)
def obter_livro(livro_id: int):
    """Obter um livro específico pelo ID"""
    for livro in livros_db:
        if livro["id"] == livro_id:
            return livro
    
    raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não encontrado")


@app.put("/livros/{livro_id}", response_model=LivroResponse)
def atualizar_livro(livro_id: int, livro_atualizado: Livro):
    """Atualizar um livro existente"""
    for i, livro in enumerate(livros_db):
        if livro["id"] == livro_id:
            dados_atualizados = livro_atualizado.dict()
            dados_atualizados["id"] = livro_id
            livros_db[i] = dados_atualizados
            return livros_db[i]
    
    raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não encontrado")


@app.delete("/livros/{livro_id}", status_code=204)
def deletar_livro(livro_id: int):
    """Deletar um livro da biblioteca"""
    for i, livro in enumerate(livros_db):
        if livro["id"] == livro_id:
            livros_db.pop(i)
            return None
    
    raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não encontrado")


# Para executar: uvicorn example:app --reload
# Acesse a documentação em: http://localhost:8000/docs
# 
# Exemplos de requisições:
# 
# 1. Criar um livro (POST /livros):
#    {
#      "titulo": "Clean Code",
#      "autor": "Robert C. Martin",
#      "ano_publicacao": 2008,
#      "preco": 54.99
#    }
#
# 2. Listar livros (GET /livros)
#    GET /livros?skip=0&limit=10
#    GET /livros?autor=Robert
#
# 3. Obter livro (GET /livros/1)
#
# 4. Atualizar livro (PUT /livros/1):
#    {
#      "titulo": "Clean Code (Updated)",
#      "autor": "Robert C. Martin",
#      "ano_publicacao": 2008,
#      "preco": 49.99
#    }
#
# 5. Deletar livro (DELETE /livros/1)
