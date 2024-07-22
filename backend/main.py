from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# CORS middleware hozzáadása
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://10.128.0.2:5173", "http://34.45.155.233:5173", "http://localhost", "https://frontend-weathered-resonance-3450.fly.dev"],  # A frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adatbázis URL megadása
DATABASE_URL = "sqlite:///./books.db"

# Adatbázis motor és session létrehozása
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Book modell definiálása
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Adatbázis táblák létrehozása (ha nem léteznek)
Base.metadata.create_all(bind=engine)

@app.get("/books")
def read_books():
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()
    return [book.name for book in books]
