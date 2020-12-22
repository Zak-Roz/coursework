from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    engine = create_engine('postgres+psycopg2://postgres:postgres@localhost:5432/coursework')
    Session = sessionmaker(bind=engine)
    Base = declarative_base()
except:
    print("Error")
    exit(1)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)