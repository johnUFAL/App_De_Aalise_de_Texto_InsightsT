from fastapi import FastAPI  # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from app.routers.analysis import analysis_router
from app.routers.auth import auth_router

#Instacia de criação da aplicação FastAPI
app = FastAPI()

#Inclusão dos roteadores na aplicação
app.include_router(analysis_router)
app.include_router(auth_router)

#Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
