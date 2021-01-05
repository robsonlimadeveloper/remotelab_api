'''Config instance'''
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    f'mysql+pymysql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}'
    f'@{os.environ["DB_NAME"]}:3306/'
    f'{os.environ["DB_DATABASE"]}?charset=utf8mb4')