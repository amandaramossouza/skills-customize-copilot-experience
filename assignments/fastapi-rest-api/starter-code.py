"""
FastAPI REST API - Starter Code

Complete este código para construir uma API REST de gerenciamento de livros.
Siga os comentários para implementar cada seção.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# TODO: Defina o modelo Pydantic para um Livro
# Dica: Use type hints como str, int, float
# Dica: Use Field para adicionar validação (ex: gt=0 para maior que 0)


# TODO: Inicialize a aplicação FastAPI


# TODO: Crie uma lista para armazenar os livros em memória


# TODO: Implemente o endpoint GET / que retorna informações da API
# Exemplo: {"message": "API de Gerenciamento de Livros", "versao": "1.0"}


# TODO: Implemente o endpoint POST /livros para criar um novo livro


# TODO: Implemente o endpoint GET /livros para listar todos os livros


# TODO: Implemente o endpoint GET /livros/{livro_id} para obter um livro específico


# TODO: Implemente o endpoint PUT /livros/{livro_id} para atualizar um livro


# TODO: Implemente o endpoint DELETE /livros/{livro_id} para remover um livro


# Para executar: uvicorn starter-code:app --reload
# Acesse a documentação em: http://localhost:8000/docs
