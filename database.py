from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/fastapi"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
try:
    
    conn = psycopg2.connect(host = 'localhost', database ='fastapi', user = 'postgres', password = '123456', cursor_factory = RealDictCursor)
    cursor = conn.cursor() 
    print("Successfull connection")

except Exception as error:
    print("connection not success and Error is ",error) 







