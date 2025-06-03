from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Engine, Session

Base = declarative_base()

# User Model Class

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String, nullable=False)

    posts = relationship("Post", back_populates='user')

    def __repr__(self):
        return f"Success: <User(id={self.id}: Name='{self.name}')>."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be an empty string.")
        
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValueError("Name must contain only letters and spaces.")
        self._name = name

    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        try:
            return session.query(cls).filter(cls._name.ilike(f"%{name}%")).all()
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        try:
            return session.query(cls).filter(cls.id == id_).first()
        finally:
            session.close()

    @classmethod
    def create(cls, session, name):
        user = cls()
        user.name = name
        session.add(user)
        session.commit()
        return user

    def update_name(self, session, new_name):
        self.name = new_name
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()



# Category Model Class

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String, nullable=False, unique=True)

    posts = relationship("Post", back_populates='category')

    def __repr__(self):
        return f"Success: <Category(id={self.id}: Name='{self.name}')>."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be an empty string.")
        self._name = name

    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        try:
            return session.query(cls).filter(cls._name.ilike(f"%{name}%")).all()
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        try:
            return session.query(cls).filter(cls.id == id_).first()
        finally:
            session.close()

    @classmethod
    def create(cls, session, name):
        category = cls()
        category.name = name
        session.add(category)
        session.commit()
        return category

    def update_name(self, session, new_name):
        self.name = new_name
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()



# Post Model Class

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String, nullable=False)
    _content = Column("content", Text, nullable=False)
    _user_id = Column("user_id", Integer, ForeignKey('users.id'), nullable=False)
    _category_id = Column("category_id", Integer, ForeignKey('categories.id'), nullable=False)

    user = relationship("User", back_populates = 'posts')
    category = relationship("Category", back_populates = 'posts')

    def __repr__(self):
        return f"Success: <Post(id={self.id}: Title ='{self.title}', User = '{self.user}'), Category = '{self.category}')>."
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be an empty string.")
        self._title = title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if not isinstance(content, str):
            raise TypeError("Content must be a string.")
        content = content.strip()
        if not content:
            raise ValueError("Content cannot be an empty string.")
        self._content = content

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if not isinstance(user_id, int):
            raise TypeError("User ID must be an integer.")
        session = Session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        if not user:
            raise ValueError(f"No User instance with ID {user_id}.")
        self._user_id = user_id

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer.")
        session = Session()
        category = session.query(Category).filter_by(id=category_id).first()
        session.close()
        if not category:
            raise ValueError(f"No Category instance with ID {category_id}.")
        self._category_id = category_id
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_title(cls, title):
        session = Session()
        try:
            return session.query(cls).filter(cls._title.ilike(f"%{title}%")).all()
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        try:
            return session.query(cls).filter(cls.id == id_).first()
        finally:
            session.close()

    @classmethod
    def create(cls, session, title, content, user_id, category_id):
        post = cls()
        post.title = title
        post.content = content
        post.user_id = user_id
        post.category_id = category_id
        session.add(post)
        session.commit()
        return post
    
    def update_post(self, session, new_title=None, new_content=None, new_user_id=None, new_category_id=None):
        if new_title is not None:
            self.title = new_title
        if new_content is not None:
            self.content = new_content
        if new_user_id is not None:
            self.user_id = new_user_id
        if new_category_id is not None:
            self.category_id = new_category_id
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()