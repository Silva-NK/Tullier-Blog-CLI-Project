from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = ''

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)