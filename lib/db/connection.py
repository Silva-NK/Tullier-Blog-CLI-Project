from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///lib/db/tullierdb.db"

Engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=Engine)