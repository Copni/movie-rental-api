from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine, SessionLocal
from app.models import Movie
from app.routers import movies as movies_router

app = FastAPI(title="Film Rental API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    if db.query(Movie).count() == 0:
        films = [
            Movie(title="Inception", genre="Sci-Fi", year=2010, description="Dreams within dreams", duration_min=148, director="Nolan", rating=8.8),
            Movie(title="The Matrix", genre="Action", year=1999, description="Simulation and reality", duration_min=136, director="Wachowski", rating=8.7),
        ]
        db.add_all(films)
        db.commit()
    db.close()

seed_data()

app.include_router(movies_router.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l’API de location de films !", "docs": "/docs"}
