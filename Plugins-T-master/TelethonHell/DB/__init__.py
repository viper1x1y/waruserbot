# Plugins-T-master/TelethonHell/DB/__init__.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Read DB URI from environment variables
DATABASE_URL = os.environ.get("DB_URI") or os.environ.get("DATABASE_URL") or "sqlite:///./telethonhell.db"

# For sqlite we need the check_same_thread arg
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create engine and session factory
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Expose names expected by other modules
BASE = declarative_base()
SESSION = SessionLocal()
ENGINE = engine
