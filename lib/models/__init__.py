# lib/models/__init__.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///little_lemon.db")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
Base = declarative_base()

# Import models so Alembic can find them via Base.metadata
# (we'll create these files in Step 3)
try:
    from .customer import Customer
    from .dining_table import DiningTable
    from .reservation import Reservation
    from .special_request import SpecialRequest
except Exception:
    # during first import before files exist
    pass
