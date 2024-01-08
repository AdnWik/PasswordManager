from os import path
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    select
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


class Database:

    def __init__(self, config: dict) -> None:
        self.database_engine = Database.create_database(config)

    @staticmethod
    def create_database(config: dict):
        database_name = config['sqlalchemy']['database_name']
        echo = config['sqlalchemy']['echo']
        future = config['sqlalchemy']['future']

        meta = MetaData()
        engine = create_engine('sqlite:///' + database_name,
                               echo=echo,
                               future=future
                               )

        if not path.exists(database_name):
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
        return engine

    def load_all_services(self):
        try:
            with Session(self.database_engine) as session:
                all_services = session.query(Service).all()
        except Exception:
            pass

        return all_services

    def load_all_credentials(self):
        try:
            with Session(self.database_engine) as session:
                all_credentials = session.query(Credential).all()
        except Exception:
            pass

        return all_credentials

    def check_service_exists(self, service_to_find: str):
        try:
            with Session(self.database_engine) as session:
                if list(session.query(Service).filter(Service.name == service_to_find)):
                    return True
                return False

        except Exception:
            return False

    def add_service(self, new_service: str):
        service_to_add = Service(name=new_service)
        try:
            with Session(self.database_engine) as session:
                session.add(service_to_add)
                session.commit()
                return True
        except Exception:
            return False

    def add_credential_to_service(self):
        print('Select service to add credential:')
        all_services = Database.load_all_services(self)

        for no, service in enumerate(all_services, start=1):
            print(f'{no} - {service.name}')

        user_choice = int(input('\n>>> '))
        print(f'Enter LOGIN to service: {all_services[user_choice - 1].name}')
        login = input('>>> ')
        print(f'Enter PASSWORD to service: {all_services[user_choice - 1].name}')
        password = input('>>> ')
        credential_to_add = Credential(service_id=all_services[user_choice - 1].id, login=login, password=password)

        try:
            with Session(self.database_engine) as session:
                session.add(credential_to_add)
                session.commit()
                return True
        except Exception:
            return False

    def show_all_services(self):
        pass

    def show_all_credentials(self):
        all_credentials = None
        try:
            with Session(self.database_engine) as session:
                stmt = select(Credential)
                all_credentials = session.scalars(stmt).all()
                #all_credentials = session.query(Credential).all()

                return all_credentials

        except Exception as error:
            return error
