from asyncpg import connect

from .config import db_uri
from .sync_plain_sql import data_from_db

# Query that will be executed asynchronously
async def async_db_ops() -> None:
    conn = await connect(db_uri)

    # GET DATA FROM DB
    data = data_from_db()
    print(len(data), "rows selected")
    
    ## INSERT TO users_0 TABLE
    await conn.executemany(
        "INSERT INTO users_0 (name) VALUES($1);", data)
    
    # INSERT TO users_1 TABLE
    await conn.executemany(
        "INSERT INTO users_1 (name) VALUES($1);", data)

    await conn.close()