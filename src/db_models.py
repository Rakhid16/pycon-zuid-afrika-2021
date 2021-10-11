# coding: utf-8
from sqlalchemy import Column, MetaData, Table, Text

metadata = MetaData()


t_users_0 = Table(
    'users_0', metadata,
    Column('name', Text)
)


t_users_1 = Table(
    'users_1', metadata,
    Column('name', Text)
)