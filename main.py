import os
import sqlalchemy
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = "ENTER YOUR OPEN AI KEY HERE"

# Create an SQLAlchemy engine for the MSSQL database
db_url = os.environ.get('DB_CONNECTION', 'mssql+pyodbc://ONKAR/WideWorldImporters?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
engine = sqlalchemy.create_engine(db_url, pool_recycle=3600)

# Create an instance of SQLDatabase
db = SQLDatabase(engine)

#
def get_all_table_names(engine):
    inspector = sqlalchemy.inspect(engine)
    table_names = []

    # Get a list of all schema names
    schema_names = inspector.get_schema_names()

    # Iterate through each schema and get the tables in that schema
    for schema_name in schema_names:
        tables = inspector.get_table_names(schema=schema_name)
        for table in tables:
            table_names.append(f"{schema_name}.{table}")

    return table_names

# Create an OpenAI instance
openai_instance = OpenAI(api_key=os.environ['OPENAI_API_KEY'], temperature=0)

# Create a SQLDatabaseToolkit instance using the SQLDatabase and OpenAI instances
toolkit = SQLDatabaseToolkit(db=db, llm=openai_instance)

# Now you can use the 'toolkit' to perform SQL-related operations on your MSSQL database
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

#agent_executor.run("""find all schemas in the database """)

def get_all_table_names(engine):
    inspector = sqlalchemy.inspect(engine)
    table_names = []

    # Get a list of all schema names
    schema_names = inspector.get_schema_names()
    

    # Iterate through each schema and get the tables in that schema
    for schema_name in schema_names:
        tables = inspector.get_table_names(schema=schema_name)
        for table in tables:
            table_names.append(f"{schema_name}.{table}")

    return schema_name
k = ''.join(get_all_table_names(engine))
print(k)

sql_query = """
Sales.Customers, Sales.Orders, and Sales.OrderLines
"""

q = "Sales.Invoices, Sales.OrderLines, Sales.Orders,"

# Execute the SQL query
result = agent_executor.run(sql_query)
print(result)
