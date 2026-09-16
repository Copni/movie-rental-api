# Movie Rental API

A movie rental platform built around a REST API. The backend exposes movie
management endpoints; a lightweight Streamlit client consumes them over HTTP.

## Architecture

The API and the front-end are two separate processes that communicate only
through HTTP, so the interface can be replaced without touching the backend.

```text
app/
├─ main.py          # FastAPI entry point
├─ database.py      # SQLite connection and session handling
├─ models.py        # SQLAlchemy ORM models
├─ schemas.py       # Pydantic schemas (validation, serialisation)
├─ crud.py          # Business logic and database access
└─ routers/
   └─ movies.py     # REST endpoints under /movies

streamlit_app.py    # Streamlit client
```

## Stack

| Layer | Technology |
| --- | --- |
| API | FastAPI, Uvicorn (ASGI) |
| Persistence | SQLAlchemy ORM, SQLite |
| Validation | Pydantic |
| Front-end | Streamlit, Requests |

## Running it

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload     # API on http://127.0.0.1:8000
streamlit run streamlit_app.py    # UI on http://127.0.0.1:8501
```

Interactive API documentation is generated automatically at
`http://127.0.0.1:8000/docs`.

## What this project covers

- Layered design: routing, schemas, business logic and persistence are separated.
- Full CRUD over a relational model through an ORM rather than raw SQL.
- Input validation and response typing handled declaratively by Pydantic.
- A client that talks to the API exactly as any external consumer would.
