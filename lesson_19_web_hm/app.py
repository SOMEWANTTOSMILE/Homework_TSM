from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from flask import Flask

metadata = MetaData()
engine = create_engine('postgresql+psycopg2://Somwl:1548@localhost/lesson_19')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass


class Intake(Base):
    __tablename__ = "person_intake"
    id = Column("id", Integer(),  primary_key=True)
    user_name = Column("user", String(255), nullable=False, unique=True)
    food = Column("food", String(255), nullable=False)
    weight = Column("weight(grams)", Integer(), nullable=False,)
    proteins = Column("proteins", Integer(), nullable=False)
    fats = Column("fats", Integer(), nullable=False)
    carbohydrates = Column("carbohydrates", Integer(), nullable=False)


Base.metadata.create_all(engine)
