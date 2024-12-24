from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .crud import (create_client, get_clients, get_client_by_id, create_booking, get_bookings, get_booking_by_id,
                   create_tour, get_tours, get_tour_by_id, delete_tour, update_tour, delete_booking, )
from .schemas import ClientCreate, ClientResponse, BookingCreate, BookingResponse, TourCreate, TourResponse, TourUpdate

app = FastAPI()

# Клиенты
@app.post("/clients/", response_model=ClientResponse)
def create_client_endpoint(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@app.get("/clients/", response_model=list[ClientResponse])
def get_clients_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_clients(db, skip=skip, limit=limit)

@app.get("/clients/{client_id}", response_model=ClientResponse)
def get_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    client = get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Туры
@app.post("/tours/", response_model=TourResponse)
def create_tour_endpoint(tour: TourCreate, db: Session = Depends(get_db)):
    return create_tour(db, tour)

@app.get("/tours/", response_model=list[TourResponse])
def get_tours_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_tours(db, skip=skip, limit=limit)

@app.get("/tours/{tour_id}", response_model=TourResponse)
def get_tour_endpoint(tour_id: int, db: Session = Depends(get_db)):
    tour = get_tour_by_id(db, tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    return tour

@app.put("/tours/{tour_id}", response_model=TourResponse)
def update_tour_endpoint(tour_id: int, tour_update: TourUpdate, db: Session = Depends(get_db)):
    updated_tour = update_tour(db, tour_id, tour_update)
    if not updated_tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    return updated_tour

@app.delete("/tours/{tour_id}", response_model=TourResponse)
def delete_tour_endpoint(tour_id: int, db: Session = Depends(get_db)):
    deleted_tour = delete_tour(db, tour_id)
    if not deleted_tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    return deleted_tour

# Бронирования
@app.post("/bookings/", response_model=BookingResponse)
def create_booking_endpoint(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db, booking)

@app.get("/bookings/", response_model=list[BookingResponse])
def get_bookings_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_bookings(db, skip=skip, limit=limit)

@app.get("/bookings/{booking_id}", response_model=BookingResponse)
def get_booking_endpoint(booking_id: int, db: Session = Depends(get_db)):
    booking = get_booking_by_id(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.delete("/bookings/{booking_id}", response_model=BookingResponse)
def delete_booking_endpoint(booking_id: int, db: Session = Depends(get_db)):
    deleted_booking = delete_booking(db, booking_id)
    if not deleted_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return deleted_booking
