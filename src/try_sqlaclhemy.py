from sqlalchemy.ext.asyncio import create_async_engine

from .config import async_orm_uri
from .db_models import t_users_1, t_users_0
from .sync_plain_sql import data_from_db

async def async_orm_ops() -> None:
    # Get the database session
    engine = create_async_engine(async_orm_uri)
    result = [{"name": i[0]} for i in data_from_db()]
    
    print(len(result), "rows selected")

    # Async db ops
    async with engine.begin() as ses:
        await ses.execute(t_users_0.insert(), result)       
        await ses.execute(t_users_1.insert(), result)
    
    await engine.dispose()
