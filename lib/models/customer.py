# lib/models/customer.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from . import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=False)

    reservations = relationship(
        "Reservation",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Customer id={self.id} name='{self.name}' email='{self.email}'>"

    # --- simple validation (property-like constraints) ---
    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        return value.strip()

    @validates("email")
    def validate_email(self, key, value):
        if not value or "@" not in value:
            raise ValueError("Email must look like an email.")
        return value.strip().lower()

    # --- ORM helpers ---
    @classmethod
    def create(cls, session, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    @classmethod
    def get_all(cls, session):
        return session.query(cls).order_by(cls.id).all()

    @classmethod
    def find_by_id(cls, session, id_):
        return session.get(cls, id_)

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email.lower()).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
