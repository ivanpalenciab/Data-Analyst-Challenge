from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine

users = Table("users",meta, Column("id",Integer, primary_key=True), Column("Name", String))

meta.create_all(engine)