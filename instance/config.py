'''Config instance'''
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    f'mssql+pyodbc://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}'
    f'@{os.environ["DB_NAME"]}:1433/'
    f'{os.environ["DB_DATABASE"]}?driver=ODBC+Driver+17+for+SQL+Server')