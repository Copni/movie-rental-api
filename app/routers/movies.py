from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("", response_model=List[schemas.MovieOut])
def list_movies(available: bool | None = Query(None), db: Session = Depends(get_db)):
    return crud.list_movies(db, available_only=available)

@router.get("/{movie_id}", response_model=schemas.MovieOut)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Film introuvable")
    return movie

@router.post("", response_model=schemas.MovieOut)
def create_movie(payload: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, payload)

@router.put("/{movie_id}", response_model=schemas.MovieOut)
def update_movie(movie_id: int, payload: schemas.MovieUpdate, db: Session = Depends(get_db)):
    movie = crud.update_movie(db, movie_id, payload)
    if not movie:
        raise HTTPException(status_code=404, detail="Film introuvable")
    return movie

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    if not crud.delete_movie(db, movie_id):
        raise HTTPException(status_code=404, detail="Film introuvable")
    return {"message": "Film supprimé"}

@router.put("/{movie_id}/rent", response_model=schemas.MovieOut)
def rent_movie(movie_id: int, payload: schemas.RentRequest, db: Session = Depends(get_db)):
    movie = crud.rent_movie(db, movie_id, payload.renter_name)
    if not movie:
        raise HTTPException(status_code=404, detail="Film introuvable")
    if movie.is_available:
        raise HTTPException(status_code=409, detail="Déjà loué")
    return movie

@router.put("/{movie_id}/return", response_model=schemas.ReturnResponse)
def return_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.return_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Film introuvable")
    return schemas.ReturnResponse(id=movie.id, is_available=movie.is_available)
