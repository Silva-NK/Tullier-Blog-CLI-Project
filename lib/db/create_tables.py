from lib.db.models import Base
from lib.db.connection import Engine

# Drop all tables first
Base.metadata.drop_all(Engine)

# Create all tables as defined in models.py
Base.metadata.create_all(Engine)

print("Empty tables created.")