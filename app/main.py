from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine, SessionLocal
from app.models import Movie
from app.routers import movies as movies_router

app = FastAPI(title="Film Rental API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Autorisation de toutes les origines
    allow_methods=["*"], # Autorisation de toutes les méthodes HTTP
    allow_headers=["*"], # Autorisation de tous types d'en-têtes
)

# Le code suivant crée les tables dans la base de données si elles n'existent pas déjà.
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    try:
        if db.query(Movie).count() == 0:
            films = [
                Movie(title="Inception", genre="Sci-Fi", year=2010, description="Dreams within dreams", duration_min=148, director="Nolan", rating=8.8),
                Movie(title="The Matrix", genre="Action", year=1999, description="Simulation and reality", duration_min=136, director="Wachowski", rating=8.7),
            ]
            db.add_all(films)
            db.commit()
    finally:
        db.close()
seed_data()

app.include_router(movies_router.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l’API de location de films !", "docs": "/docs"}
