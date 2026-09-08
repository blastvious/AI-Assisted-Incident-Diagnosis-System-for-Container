from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = (
    "postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/order_db"
)

postgresql_engine = create_engine(DATABASE_URL,echo=True)

Session_local = sessionmaker(autoflush=False, bind=postgresql_engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = Session_local()

    try:
        yield db
    finally:
        db.close()