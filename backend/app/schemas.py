#padrão de dados para a aplicação
from datetime import datetime
from pydantic import BaseModel, Field # type: ignore
from typing import Optional, List

#Schema para criação de usuário
class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str = Field(min_length=8, max_length=64)
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

#Schema para retorno de dados do usuário
class UsuarioMeSchema(BaseModel):
    nome: str
    email: str
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

#Schema para análise de entidades (suporte)
class entidades(BaseModel):
    texto: str
    tipo: str

    class Config:
        from_attributes = True

#Schema para resposta da análise de texto
class AnalysisResponseSchema(BaseModel):
    id: Optional[int] = None
    texto_original: str
    sentimento: str
    palavra_mais_frequente: str
    entidades: List[entidades]
    lvl_legibilidade: str
    cont_palavras: int
    cont_caracteres: int
    cont_frases: int
    criado_em: Optional[datetime] = None

    class Config:
        from_attributes = True

#Schema para requisição de análise de texto
class AnalysisRequestSchema(BaseModel):
    texto_original: str
    salvar_historico: bool = True

    class Config:
        from_attributes = True

#Schema para login do usuário
class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True

#Schema para resposta de predição de tópicos
class TopicPrediction(BaseModel):
    topico: str
    confianca: float

#Schema para resposta de análise de tópicos (suporte)
class TopicResponse(BaseModel):
    texto: str
    topicos: List[TopicPrediction]
    topico_principal: str
