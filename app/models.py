from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# Модель клиента
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

    # Связь с бронированиями
    bookings = relationship("Booking", back_populates="client")


# Модель тура
class Tour(Base):
    __tablename__ = "tours"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    duration = Column(Integer)  # длительность тура в днях

    # Связь с бронированиями
    bookings = relationship("Booking", back_populates="tour")


# Модель бронирования
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    tour_id = Column(Integer, ForeignKey("tours.id"))
    booking_date = Column(Date)
    number_of_people = Column(Integer)

    client = relationship("Client", back_populates="bookings")
    tour = relationship("Tour", back_populates="bookings")
