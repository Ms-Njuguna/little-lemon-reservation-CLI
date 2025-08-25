# lib/models/table.py
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship, validates
from . import Base

class DiningTable(Base):
    __tablename__ = "dining_tables"