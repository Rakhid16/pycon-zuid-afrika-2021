from csv import reader as csv_reader

from asyncpg import connect

from .config import db_uri

# Read the .csv data
async def data_from_csv():
    with open('dummy_data.csv') as csv_file:
        data = [tuple(i) for i in csv_reader(csv_file)]
    
    return data

# Query that will be executed asynchronously
async def create_new_tables():
    conn = await connect(db_uri)
    data = await data_from_csv()

    # Drop table users_0 & users_1 if exists
    await conn.execute('''
        DROP TABLE IF EXISTS
        users_0, users_1''')

    # Create table users_0
    await conn.execute('''
        CREATE TABLE users_0(
            name text)''')

    # Create table users_1
    await conn.execute('''
        CREATE TABLE users_1(
            name text)''')

    # Insert data to users_0 table
    await conn.executemany(
        "INSERT INTO users_0 (name) VALUES ($1)",
        data)

    # Insert data to users_1 table
    await conn.executemany(
        "INSERT INTO users_1 (name) VALUES ($1)",
        data)

    # Close the connection
    await conn.close()
