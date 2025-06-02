from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Engine, Session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    posts = relationship("Post", back_populates = 'user')

    def __repr__(self):
        return f"Success: <User(id={self.id}: Name ='{self.name}')>."
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            users = session.query(cls).all()
            return users
        finally:
            session.close()
    
    @classmethod
    def find_by_name(cls, name):
        session = Session()
        try:
            users = session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
            return users
        finally:
            session.close()
    
    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        try:
            user = session.query(cls).filter(cls.id == id_).first()
            return user
        finally:
            session.close()



class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    posts = relationship("Post", back_populates = 'category')

    def __repr__(self):
        return f"Success: <Category(id={self.id}: Name ='{self.name}')>."
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            categories = session.query(cls).all()
            return categories
        finally:
            session.close()

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        try:
            categories = session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
            return categories
        finally:
            session.close()
    
    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        try:
            category = session.query(cls).filter(cls.id == id_).first()
            return category
        finally:
            session.close()



class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id =  Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship("User", back_populates = 'posts')
    category = relationship("Category", back_populates = 'posts')

    def __repr__(self):
        return f"Success: <Post(id={self.id}: Title ='{self.title}', User = '{self.user}'), Category = '{self.category}')>."
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            posts = session.query(cls).all()
            return posts
        finally:
            session.close()
    
    @classmethod
    def find_by_title(cls, title):
        session = Session()
        try:
            posts = session.query(cls).filter(cls.title.ilike(f"%{title}%")).all()
            return posts
        finally:
            session.close()
    
    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        try:
            post = session.query(cls).filter(cls.id == id_).first()
            return post
        finally:
            session.close()