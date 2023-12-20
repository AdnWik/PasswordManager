from os import path
import yaml
import logging
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
from database import create_database, Service, Credential


class ServiceExists(Exception):
    """ERROR - Service name already exists"""


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


# MAIN PROGRAM
config = load_config('config.yaml')
logging.basicConfig(level=logging.DEBUG)

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
            print('Enter new service name')
            new_service = input('>>> ')
            try:
                with Session(engine) as session:
                    matching_services = list(session.query(Service).filter(Service.name == new_service))

                    if matching_services:
                        raise ServiceExists

                    service = Service(name=new_service)
                    session.add(service)
                    session.commit()
                    logging.info('Create service: %s -> OK', new_service)
                    print(f'\nCreate service: {new_service} -> OK')

            except ServiceExists:
                logging.error('%s ALREADY EXISTS', new_service)

        elif user_choice == '2':
            # ADD - CREDENTIAL
            pass

        else:
            pass

    else:
        # EXIT
        break