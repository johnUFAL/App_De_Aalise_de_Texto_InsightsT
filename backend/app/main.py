from fastapi import FastAPI, Request  # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from app.routers.analysis import analysis_router
from app.routers.auth import auth_router
from slowapi import Limiter, _rate_limit_exceeded_handler # type: ignore
from slowapi.util import get_remote_address # type: ignore
from slowapi.errors import RateLimitExceeded # type: ignore
from fastapi.responses import JSONResponse # type: ignore

#Instacia de criação da aplicação FastAPI
app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://insightstextanalysis.vercel.app",
]

#Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"^https://.*\.vercel\.app$",
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
    expose_headers=["Content-Length", "X-Request-ID"],
    max_age=600,
)


@app.get('/cors-check')
async def cors_check(request: Request):
    # Retorna o header Origin recebido para confirmar que o CORS está permitindo
    return JSONResponse({"origin_received": request.headers.get('origin')})

#Inicializar limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

#Health check endpoint
@app.get("/health")
@limiter.limit("100/minute")
async def health_check(request: Request):
    return {"status": "healthy"}

@app.get("/info")
async def info():
    db_type = "sqlite" if "sqlite" in str(__import__('app.core.config', fromlist=['DATABASE_URL']).DATABASE_URL) else "postgres"
    return {"environment": __import__('app.core.config', fromlist=['ENVIRONMENT']).ENVIRONMENT, "database": db_type}

#Exemplo endpoint com rate limiting
@app.get("/api/data")
@limiter.limit("10/minute")
async def get_data(request: Request):
    return {"data": "..."}

#Inclusão dos roteadores na aplicação
app.include_router(analysis_router)
app.include_router(auth_router)

#Root endpoint
@app.get("/")
async def root():
    return {"message": "InsightsT API", "status": "online"}