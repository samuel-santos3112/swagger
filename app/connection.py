from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

engine = create_engine('postgresql://postgres:psql@localhost:5432/api_swagger')
Session = sessionmaker(bind=engine)

Base = declarative_base()

