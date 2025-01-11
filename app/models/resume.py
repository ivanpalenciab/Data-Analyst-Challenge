from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String,Date

from config.db import meta, engine
from models.user import users

resumes = Table("resume",meta, 
        Column("id",Integer, primary_key=True), 
        Column("user_id", Integer,ForeignKey("users.id")),
        Column("name", String),
        Column("type",String),
        Column("video",String),
        Column("views",Integer),
        Column("created_at",Date))


meta.create_all(engine)