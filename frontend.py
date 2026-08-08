import streamlit as st
from app import ask_ai
from visualization import draw_chart

st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightFlow AI")

st.write(
    "Ask questions about your SQL database using natural language."
)

question = st.text_input(
    "Ask your question",
    placeholder="Example: Show top 10 customers by revenue"
)

if st.button("🚀 Analyze"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        sql, df, insight = ask_ai(question)

        st.success("Analysis Complete")

        st.subheader("📝 Generated SQL")
        st.code(sql, language="sql")

        st.subheader("📋 Query Result")
        st.dataframe(df, use_container_width=True)

        st.subheader("📊 Visualization")

        fig = draw_chart(df)

        if fig is not None:
            st.pyplot(fig)

        st.subheader("💡 AI Business Insight")
        st.write(insight)