from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Blog_Model(Base):

    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    creater = relationship('User_Model', back_populates='blogs')

class User_Model(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog_Model', back_populates='creater')