import asyncio
from time import time

from src.try_sqlaclhemy import async_orm_ops
from src.async_plain_sql import async_db_ops
from src.sync_plain_sql import sync_db_ops
from src.db_init import create_new_tables


print("Async Plain SQL")
asyncio.run(create_new_tables())
for i in range(7):
    start = time()
    asyncio.run(async_db_ops())
    print(f"Insert into two tables took {time() - start} seconds")

print("\nSync Plain SQL")
asyncio.run(create_new_tables())
for i in range(7):
    start = time()
    sync_db_ops()
    print(f"Insert into two tables took {time() - start} seconds")

print("\nAsync SQLAlchemy")
asyncio.run(create_new_tables())
for i in range(7):
    start = time()
    asyncio.run(async_orm_ops())
    print(f"Insert into two tables took {time() - start} seconds")