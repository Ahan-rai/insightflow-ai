import pandas as pd
from database import engine


def execute_sql(sql):
    """
    Executes a SQL query and returns a Pandas DataFrame.
    """
    return pd.read_sql(sql, engine)