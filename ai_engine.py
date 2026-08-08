from database import db
from llm import llm


def generate_sql(question):

    schema = db.get_table_info()

    prompt = f"""
You are an expert MySQL developer.

Database Schema:
{schema}

Rules:
- Return ONLY valid MySQL SQL.
- No explanation.
- No markdown.
- Never write ```sql.
- Return only one SQL query.

Question:
{question}
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        sql = response.content[0]["text"]
    else:
        sql = response.content

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql