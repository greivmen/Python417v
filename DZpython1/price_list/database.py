from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'Gimli.db'
engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all(engine)
