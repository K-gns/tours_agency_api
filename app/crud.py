from sqlalchemy.orm import Session
from sqlalchemy.future import select
from .models import Tour, Client, Booking
from .schemas import ClientCreate, TourCreate, TourUpdate, BookingCreate


# Создание тура
def create_tour(db: Session, tour: TourCreate):
    db_tour = Tour(name=tour.name, description=tour.description, price=tour.price, duration=tour.duration)
    db.add(db_tour)
    db.commit()
    db.refresh(db_tour)
    return db_tour

# Получение всех туров
def get_tours(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tour).offset(skip).limit(limit).all()

# Получение тура по ID
def get_tour_by_id(db: Session, tour_id: int):
    return db.query(Tour).filter(Tour.id == tour_id).first()

# Обновление тура
def update_tour(db: Session, tour_id: int, tour_update: TourUpdate):
    db_tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if db_tour:
        if tour_update.name:
            db_tour.name = tour_update.name
        if tour_update.description:
            db_tour.description = tour_update.description
        if tour_update.price is not None:
            db_tour.price = tour_update.price
        if tour_update.duration is not None:
            db_tour.duration = tour_update.duration
        db.commit()
        db.refresh(db_tour)
        return db_tour
    return None

# Удаление тура
def delete_tour(db: Session, tour_id: int):
    db_tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if db_tour:
        db.delete(db_tour)
        db.commit()
        return db_tour
    return None


# Создание клиента
def create_client(db: Session, client: ClientCreate):
    db_client = Client(name=client.name, email=client.email, phone=client.phone)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Получение всех клиентов
def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()

# Получение клиента по ID
def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


# Создание бронирования
def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(
        client_id=booking.client_id,
        tour_id=booking.tour_id,
        booking_date=booking.booking_date,
        number_of_people=booking.number_of_people
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# Получение всех бронирований
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Booking).offset(skip).limit(limit).all()

# Получение бронирования по ID
def get_booking_by_id(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

# Удаление бронирования
def delete_booking(db: Session, booking_id: int):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
        return db_booking
    return None
