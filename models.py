from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    contacts = relationship("Contact", back_populates="owner")

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    birthday = Column(Date)
    additional_info = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="contacts")

from sqlalchemy import Boolean

class User(Base):
    is_verified = Column(Boolean, default=False)

def add_contact(name: str, phone: str) -> None:
