from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from langchain_community.utilities import SQLDatabase
from config import *

connection_url = URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USERNAME,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=int(MYSQL_PORT),
    database=MYSQL_DATABASE
)

engine = create_engine(connection_url)

db = SQLDatabase(engine)