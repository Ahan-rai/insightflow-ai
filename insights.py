from llm import llm


def explain_dataframe(df):

    prompt = f"""
You are a Senior Business Analyst.

Analyze this table and provide:

1. Executive Summary
2. Key Insights
3. Business Recommendations

Data:

{df.to_string()}
"""

    response = llm.invoke(prompt)

    return response.content