from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    author = Column(String(20))
    price = Column(Integer)
    publisher = Column(String(20))
   
Base.metadata.create_all(bind=engine) 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
