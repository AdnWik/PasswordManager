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


config = load_config('config.yaml')
engine = create_engine('sqlite:///' + config['sqlalchemy']['database_name'],
                       echo=config['sqlalchemy']['echo'],
                       future=config['sqlalchemy']['future']
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
