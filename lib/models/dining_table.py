# lib/models/table.py
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship, validates
from . import Base

class DiningTable(Base):
    __tablename__ = "dining_tables"

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)   # visible table number
    location = Column(String, nullable=True)   # e.g., "Window", "Patio"
    capacity = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint("number", name="uq_table_number"),)

    reservations = relationship(
        "Reservation",
        back_populates="table",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Table #{self.number} cap={self.capacity} loc={self.location or '-'}>"
    
    @validates("capacity")
    def validate_capacity(self, key, value):
        if value is None or value < 1:
            raise ValueError("Capacity must be at least 1.")
        return int(value)

    @validates("number")
    def validate_number(self, key, value):
        if value is None or value < 1:
            raise ValueError("Table number must be a positive integer.")
        return int(value)
    
    # ORM helpers
    @classmethod
    def create(cls, session, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    @classmethod
    def get_all(cls, session):
        return session.query(cls).order_by(cls.number).all()

    @classmethod
    def find_by_id(cls, session, id_):
        return session.get(cls, id_)

    def delete(self, session):
        session.delete(self)
        session.commit()

        