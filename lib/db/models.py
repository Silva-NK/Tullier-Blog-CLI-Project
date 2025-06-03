from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Engine, Session

Base = declarative_base()


# User Model Class

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
    
    @classmethod
    def create(cls, session, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        
        if not name.strip():
            raise ValueError("Name cannot be an enpty string.")
        
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValueError("Name must contain only letters and spaces.")
        
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user
    
    def update_name(self, session, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
    
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Name cannot be an empty string.")
        
        if not all(char.isalpha() or char.isspace() for char in new_name):
            raise ValueError("Name must contain only letters and spaces.")
        
        self.name = new_name
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()


# Category Model Class

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

    @classmethod
    def create(cls, session, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        
        if not name.strip():
            raise ValueError("Name cannot be an enpty string.")
        
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category
    
    def update_name(self, session, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Name cannot be an enpty string.")
        
        self.name = new_name
        session.commit()
    
    def delete(self, session):
        session.delete(self)
        session.commit()


# Post Model Class

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

    @classmethod
    def create(cls, session, title, content, user_id, category_id):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be an enpty string.")
        
        content = content.strip() if isinstance(content, str) else ""
        if not content:
            raise ValueError("Content cannot be an empty string.")
        
        if user_id is None or str(user_id).strip() == "":
            raise ValueError("User ID cannot be empty.")
        if not isinstance(user_id, int):
            raise TypeError("User ID must be an integer.")
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            raise ValueError("No User instance with this User ID.")
        
        if category_id is None or str(category_id).strip() == "":
            raise ValueError("Category ID cannot be empty.")
        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer.")
        category = session.query(Category).filter_by(id=category_id).first()
        if not category:
            raise ValueError("No Category instance with this Category ID.")
        
        post = cls(title=title, content=content, user_id=user_id, category_id=category_id)
        session.add(post)
        session.commit()
        return post
    
    def update_post(self, session, new_title=None, new_content=None, new_user_id=None, new_category_id=None):
        if new_title is not None:
            if not isinstance(new_title, str):
                raise TypeError("Title must be a string.")
            new_title = new_title.strip()
            if not new_title:
                raise ValueError("Title cannot be an empty string.")
            self.title = new_title

        if new_content is not None:
            if not isinstance(new_content, str):
                raise TypeError("Content must be a string.")
            new_content = new_content.strip()
            if not new_content:
                raise ValueError("Content cannot be an empty string.")
            self.content = new_content
        
        if new_user_id is not None:
            if not isinstance(new_user_id, int):
                raise TypeError("User ID must be an integer.")
            user = session.query(User).filter_by(id=new_user_id).first()
            if not user:
                raise ValueError("No User instance with this ID.")
            self.user_id = new_user_id

        if new_category_id is not None:
            if not isinstance(new_category_id, int):
                raise TypeError("Category ID must be an integer.")
            category = session.query(Category).filter_by(id=new_category_id).first()
            if not category:
                raise ValueError("No Category instance with this ID.")
            self.category_id = new_category_id
        
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()