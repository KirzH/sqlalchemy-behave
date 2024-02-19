import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table


# Подключение к БД
class ConnectPostgreSql:

    def __init__(self):
        self.connection = None

    def connect(self):
        def connect(self):
            try:
                engine = create_engine("postgresql+psycopg2://postgres:q1w2e3@localhost/TestDatabase")
                return engine
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)


connect_postgresql = ConnectPostgreSql()
connect_postgresql.connect()


# Создание новой таблицы
class CreateTable:

    def create_table(self, engine):
        metadata = MetaData()

        my_table = Table('my_table', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String),
                         Column('age', Integer))

        metadata.create_all(engine)
