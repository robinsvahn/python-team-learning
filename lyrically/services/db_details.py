from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/python_test?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server", echo=False)
    
Session = sessionmaker(bind=engine)

Base = declarative_base()
