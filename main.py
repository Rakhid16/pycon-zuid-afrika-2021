import asyncio
from time import time

from src.sync_plain_sql import sync_db_ops
from src.db_init import create_new_tables


print("\nSync Plain SQL")
asyncio.run(create_new_tables())
for i in range(12):
    start = time()
    sync_db_ops()
    print(f"Insert into two tables took {time() - start} seconds")
