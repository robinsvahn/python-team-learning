from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# print("Version is: " + sqlalchemy.__version__)

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/python_test?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server", echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
