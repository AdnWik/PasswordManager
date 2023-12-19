from os import path
import yaml
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
from menu import create_menu


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


def load_config(filename) -> dict:
    """Load config from YAML file

    Args:
        filename (str): _filename_.yaml

    Returns:
        dict: dictionary with configuration
    """
    with open(filename, encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data


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


# MAIN PROGRAM
config = load_config('config.yaml')

if not path.exists(config['sqlalchemy']['database_name']):
    create_database(config)

engine = create_engine("sqlite:///" + config['sqlalchemy']['database_name'], echo=False, future=True)

while True:
    options = ['show', 'add']
    start_message = 'PASSWORD MANAGER'
    print(create_menu(menu_options=options, start_message=start_message))
    user_choice = input('>>> ')

    if user_choice == '1':
        # SHOW
        options = ['all', 'specific']
        submenu = 'show'
        print(create_menu(menu_options=options, submenu_name=submenu))
        user_choice = input('>>> ')

        if user_choice == '1':
            # SHOW - ALL
            with Session(engine) as session:
                services = session.query(Service).all()
                print('\n' + 'result'.upper().center(100, '-'))
                for service in services:
                    print(f'Service: {service.name}')

        elif user_choice == '2':
            # SHOW - SPECIFIC
            pass

        else:
            pass

    elif user_choice == '2':
        # ADD
        options = ['service', 'credential']
        submenu = 'add'
        print(create_menu(menu_options=options, submenu_name=submenu))
        user_choice = input('>>> ')

        if user_choice == '1':
            # ADD - SERVICE
            new_service = input('>>> ')
            try:
                with Session(engine) as session:
                    #services = session.query(Service).filter(Service.name == new_service)
                    #for service in services:
                    #   print(service.name)

                    service = Service(name=new_service)
                    session.add(service)
                    session.commit()

            except Exception:
                pass

            print(f'\nCreate service "{new_service}" -> OK')

        elif user_choice == '2':
            # ADD - CREDENTIAL
            pass

        else:
            pass

    else:
        # EXIT
        break



'''
    print('='*100)
    print('PASSWORD MANAGER\n')
    options = ['Add service', 'Add credential to service']
    for no, option in enumerate(options, 1):
        print(f'{no} - {option}')
    print('\n0 - EXIT\n')

    user_choice = int(input('>>> '))
    if user_choice == 1:
        # ADD NEW SERVICE
        print('Enter service name: ')
        new_service = input('>>> ')

        try:
            with Session(engine) as session:
                #services = session.query(Service).filter(Service.name == new_service)
                #for service in services:
                 #   print(service.name)

                service = Service(name=new_service)
                session.add(service)
                session.commit()

        except Exception:
            pass

        print(f'Create {new_service} -> OK')

    elif user_choice == 2:
        # ADD CREDENTIAL TO SERVICE
        pass

    else:
        # EXIT
        break
'''
