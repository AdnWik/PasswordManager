from os import path
import yaml
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData
    )


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
        Column('service_name', String)
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
