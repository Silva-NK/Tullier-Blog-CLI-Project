from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    posts = relationship("Post", back_populates = 'user')

    def __repr__(self):
        return f"Success: <User(id={self.id}: Name ='{self.name}')>."
    

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    posts = relationship("Post", back_populates = 'category')

    def __repr__(self):
        return f"Success: <Category(id={self.id}: Name ='{self.name}')>."
    

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