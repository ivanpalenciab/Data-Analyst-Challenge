import os

from dotenv import load_dotenv
from sqlalchemy import create_engine,MetaData


meta = MetaData()

load_dotenv()

password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")

engine = create_engine(f"postgresql://postgres:{password}@{host}:5434/prueba")
conn = engine.connect()