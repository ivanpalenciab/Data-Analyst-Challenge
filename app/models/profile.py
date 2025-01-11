from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String,Date

from config.db import meta, engine

profiles = Table("profile",meta, 
        Column("id",Integer, primary_key=True), 
        Column("user_id", Integer),
        Column("onboarding_goal", String),
        Column("created_at",Date),
        Column("updated_at",Date),
        Column("views",Integer))


meta.create_all(engine)