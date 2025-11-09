from sqlalchemy import String, Integer, Boolean, DateTime, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.database import Base

# Utilisation de la bibliothèque SQLAlchemy pour définir les attributs de la table movies
class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    genre: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    duration_min: Mapped[int] = mapped_column(Integer)
    director: Mapped[str] = mapped_column(String(150))
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    rented_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    renter_name: Mapped[str | None] = mapped_column(String(150), nullable=True)
