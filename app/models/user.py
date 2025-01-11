from datetime import date

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String,Date,BigInteger

from config.db import meta, engine

users = Table("users",meta, 
        Column("id",Integer, primary_key=True), 
        Column("name", String),
        Column("identification_number", BigInteger),
        Column("slug",String),
        Column("video",String),
        Column("email",String),
        Column("created_at",Date),
        Column("updated_at",Date))

meta.create_all(engine)