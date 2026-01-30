# Análise Inteligente - InsightsT 

**Aplicação full-stack para análise de texto com autenticação, histórico e análise de tópicos.**

> Este projeto é composto por um backend em **FastAPI** (Python) e um frontend em **React + Vite**. O deploy está planejado para ser feito no **Render.com**.

---

## Recursos principais

- Registro e autenticação de usuários (JWT)
- Análise de texto (NLP)
- Análise de tópicos
- Histórico de análises por usuário
- API RESTful com FastAPI
- Frontend moderno com React, Vite e Tailwind

---

## Stack Tecnológica

- Backend: Python, FastAPI, SQLAlchemy, Alembic
- Banco de dados (dev): SQLite (arquivo local)
- NLP: spaCy, pt_core_news_sm, outras dependências listadas em `backend/requeriments.txt`
- Frontend: React, Vite, Tailwind, Axios

---

## Requisitos

- Python 3.10+
- Node.js 16+
- npm ou yarn

---

## Rodando localmente

### Backend

1. Entre na pasta do backend:

```bash
cd backend
```

2. Crie e ative um ambiente virtual (exemplo com venv):

```bash
python -m venv .venv
# No Windows
.\.venv\Scripts\activate
# No macOS/Linux
source .venv/bin/activate
```

3. Instale dependências:

```bash
pip install -r requeriments.txt
```

4. Configure variáveis de ambiente (crie um arquivo `.env` na pasta `backend/`):

```
SECRET_KEY=uma_chave_secreta_supersegura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./analyses.db
```

5. (Opcional) Rode migrações Alembic:

```bash
alembic upgrade head
```

6. Inicie o servidor em modo de desenvolvimento:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A API ficará disponível em `http://localhost:8000`.


### Frontend

1. Entre na pasta do frontend:

```bash
cd frontend
```

2. Instale dependências:

```bash
npm install
# ou
# yarn
```

3. Inicie o servidor de desenvolvimento:

```bash
npm run dev
```

4. Acesse a aplicação em `http://localhost:5173`.

> Dica: para apontar o frontend para a API em produção, recomendo usar uma variável de ambiente Vite (`VITE_API_BASE_URL`) e alterar `frontend/src/services/api.js` para:

```js
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
```

Recompile com `npm run build` após a alteração.

---

## Testes

Para rodar os testes do backend:

```bash
cd backend
pytest
```

---

## Migrações / Banco de dados

- As migrations estão em `backend/alembic/`.
- Com `alembic` instalado, gere novas migrations (autogeradas) com:

```bash
alembic revision --autogenerate -m "sua mensagem"
alembic upgrade head
```

---

## Estrutura do projeto

- `backend/` — API (FastAPI)
  - `app/` — código da aplicação
  - `requeriments.txt` — dependências
  - `alembic/` — migrações
- `frontend/` — app React (Vite)

---

## Contribuições

Contribuições são bem-vindas! Abra issues ou PRs com descrições claras das mudanças.

---

## Licença

Veja o arquivo `LICENSE` do repositório.

---