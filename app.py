from ai_engine import generate_sql
from utils import execute_sql
from insights import explain_dataframe


def ask_ai(question):

    # Generate SQL
    sql = generate_sql(question)

    # Execute SQL
    df = execute_sql(sql)

    # Generate Insight
    insight = explain_dataframe(df)

    # Return everything to Streamlit
    return sql, df, insight