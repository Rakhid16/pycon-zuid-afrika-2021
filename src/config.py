from dotenv import load_dotenv
from os import path, environ

BASEDIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASEDIR, '.env'))

username = environ['username']
password = environ['password']
address = environ['address']
db_name = environ['db_name']

db_uri = f"postgresql://{username}:{password}@{address}/{db_name}"
async_orm_uri = f"postgresql+asyncpg://{username}:{password}@{address}/{db_name}"