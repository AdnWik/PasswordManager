from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    )
from sqlalchemy.orm import declarative_base, relationship, Session, backref


Base = declarative_base()


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Credential(Base):
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship('Service', backref=backref('services', uselist=False))
    login = Column(String(50))
    password = Column(String(100))


def create_database(data):
    engine = create_engine('sqlite:///' + data['sqlalchemy']['database_name'],
                           echo=data['sqlalchemy']['echo'],
                           future=data['sqlalchemy']['future']
                           )
    meta = MetaData()

    services = Table(
        'services', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String, unique=True)
    )

    credentials = Table(
        'credentials', meta,
        Column('id', Integer, primary_key=True),
        Column('service_id', Integer),
        Column('login', String),
        Column('password', String)
    )

    meta.create_all(engine)
