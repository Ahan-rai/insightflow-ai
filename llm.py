import os

from langchain_groq import ChatGroq

from config import *

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0
)