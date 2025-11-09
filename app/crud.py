from sqlalchemy.orm import Session
from datetime import datetime
from typing import Sequence
from app import models, schemas

# Fonction pour récupérer la liste des films, avec possibilité de filtrage
def list_movies(db: Session, available_only: bool | None = None) -> Sequence[models.Movie]:
    query = db.query(models.Movie)
    # Filtrage :
    if available_only:
        query = query.filter(models.Movie.is_available.is_(True))
    # Trie de la requête par titre
    return query.order_by(models.Movie.title).all()

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, data: schemas.MovieCreate):
    movie = models.Movie(**data.dict()) # Conversion d'un objet Pydantic vers un modèle SQLAlchemy
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def update_movie(db: Session, movie_id: int, data: schemas.MovieUpdate):
    movie = get_movie(db, movie_id)
    if not movie:
        return None
    for key, value in data.dict().items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int):
    movie = get_movie(db, movie_id)
    if not movie:
        return False
    db.delete(movie)
    db.commit()
    return True

def rent_movie(db: Session, movie_id: int, renter_name: str):
    movie = get_movie(db, movie_id)
    if not movie:
        return None
    if not movie.is_available:
        return movie
    movie.is_available = False
    movie.rented_at = datetime.utcnow()
    movie.renter_name = renter_name
    db.commit()
    db.refresh(movie)
    return movie

def return_movie(db: Session, movie_id: int):
    movie = get_movie(db, movie_id)
    if not movie:
        return None
    movie.is_available = True
    movie.rented_at = None
    movie.renter_name = None
    db.commit()
    db.refresh(movie)
    return movie
