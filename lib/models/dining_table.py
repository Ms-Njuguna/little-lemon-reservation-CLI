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
    
    