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
from database import Database, Service, Credential


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

database = Database(config)

while True:
    options = ['show', 'add', 'delete']
    start_message = 'PASSWORD MANAGER'
    print(create_menu(menu_options=options, start_message=start_message))
    user_choice = input('>>> ')

    if user_choice == '1':
        # SHOW
        options = ['all credentials', 'specific credential', 'all services', 'specific service']
        submenu = 'show'
        print(create_menu(menu_options=options, submenu_name=submenu))
        user_choice = input('>>> ')

        if user_choice == '1':
            # TODO:
            # SHOW - ALL CREDENTIALS
            pass

        elif user_choice == '2':
            # TODO:
            # SHOW - SPECIFIC CREDENTIAL
            pass

        elif user_choice == '3':
            # SHOW - ALL SERVICES
            all_services = database.load_all_services()
            print('\n' + 'result'.upper().center(100, '-'))
            for service in all_services:
                print(f'Service: {service.name}')

        elif user_choice == '4':
            # TODO:
            # SHOW - SPECIFIC SERVICE
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
                if database.check_service_exists(new_service):
                    raise ServiceExists

                if database.add_service(new_service):
                    logging.info('Create service: %s -> OK', new_service)
                    print(f'\nCreate service: {new_service} -> OK')

            except ServiceExists:
                logging.error('%s ALREADY EXISTS', new_service)

        elif user_choice == '2':
            # ADD - CREDENTIAL
            if database.add_credential_to_service():
                logging.info('Create credential -> OK')
            else:
                logging.info('Create credential -> NOK')

    elif user_choice == '3':
        # TODO:
        # DELETE
        pass

    else:
        # EXIT
        break
