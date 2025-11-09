from pydantic import BaseModel, Field
from datetime import datetime

class MovieBase(BaseModel):
    title: str
    genre: str
    year: int
    description: str
    duration_min: int
    director: str
    rating: float = Field(0.0, ge=0, le=10)

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int
    is_available: bool
    rented_at: datetime | None = None
    renter_name: str | None = None

    class Config:
        from_attributes = True

class RentRequest(BaseModel):
    renter_name: str

class ReturnResponse(BaseModel):
    id: int
    is_available: bool
