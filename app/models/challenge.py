from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String,Date

from config.db import meta, engine

challenges = Table("challenge",meta, 
        Column("id",Integer, primary_key=True), 
        Column("name", String),
        Column("description", String),
        Column("status",String),
        Column("opencall_objective",String),
        Column("created_at",Date))

meta.create_all(engine)