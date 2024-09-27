from sqlalchemy import create_engine, MetaData
from databases import databases

DATABASE_URL = "postgresql://username:password@postgres:5432/dbname"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)