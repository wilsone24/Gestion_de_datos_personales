from dotenv import load_dotenv
import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from database import SQLALCHEMY_DATABASE_URL

load_dotenv()

db_lc = SQLDatabase.from_uri(SQLALCHEMY_DATABASE_URL)

print(f"Dialect: {db_lc.dialect}")
print(f"Available tables: {db_lc.get_usable_table_names()}")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0,
)

toolkit = SQLDatabaseToolkit(db=db_lc, llm=llm)

agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)


def generate_response(question: str):
    try:
        result = agent.run(question)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
