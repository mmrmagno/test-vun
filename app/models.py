from sqlalchemy import Table, Column, String, MetaData

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("username", String(50), primary_key=True),
    column("password", String(100)),
)