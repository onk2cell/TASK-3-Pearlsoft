# TASK-3-Pearlsoft
Task-3 
 implement functionalities that allow users to pose questions in plain English and receive relevant information from the database.

# connect your databse :
db_url = os.environ.get('DB_CONNECTION', 'mssql+pyodbc://ONKAR/WideWorldImporters?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
engine = sqlalchemy.create_engine(db_url, pool_recycle=3600)







here i have used mssql 

# 


## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example Queries](#example-queries)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## Prerequisites

- Python 3.x
- Required libraries and dependencies (e.g., Langchain, SQLAlchemy, OpenAI, etc.)
- Access to a Microsoft SQL Server database

## Getting Started

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Set up your OpenAI API key by setting the environment variable `OPENAI_API_KEY`.
4. Configure the database connection by modifying the `DB_CONNECTION` environment variable in the script to match your database details.

## Usage

1. **List Table Names**: You can list all table names in the database by executing the following code:

   ```python
   python list_tables.py
