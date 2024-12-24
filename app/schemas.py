from pydantic import BaseModel
from datetime import date
from typing import Optional


# Схемы для клиента
class ClientBase(BaseModel):
    name: str
    email: str
    phone: str


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int

    class Config:
        orm_mode = True


# Схемы для тура
class TourBase(BaseModel):
    name: str
    description: str
    price: float
    duration: int


class TourCreate(TourBase):
    pass


class TourUpdate(TourBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    duration: Optional[int] = None


class TourResponse(TourBase):
    id: int

    class Config:
        orm_mode = True


# Схемы для бронирования
class BookingBase(BaseModel):
    client_id: int
    tour_id: int
    booking_date: date
    number_of_people: int


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: int

    class Config:
        orm_mode = True
