from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Platform(Base):
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Developer(Base):
    __tablename__ = 'developer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    developer = Column(String, index=True)
    publisher = Column(String, index=True)
    tag = Column(String, index=True)
    platform = Column(String, index=True)