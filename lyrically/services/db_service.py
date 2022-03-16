from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Db_Service:

    def __init__(self) -> None:
        self.dialect = "mssql"
        self.driver = "PyODBC"
        self.username = "robin_test"
        self.password = "testing789"
        self.host = "localhost"
        self.port = ""
        self.database = "python_test"

        self.engine = create_engine(
            f"{self.dialect}+{self.driver}://{self.username}:{self.password}@{self.host}/{self.database}")

        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)
        self.Base = declarative_base()

    # def setup_db_connection(self):
    #     # Connecting to MSSQL server at localhost using PyODBC DBAPI
    #     self.engine = create_engine(
    #         f"{self.dialect}+{self.driver}://{self.username}:{self.password}@{self.host}/{self.database}")

    #     self.Session = sessionmaker()
    #     self.Session.configure(bind=engine)
    #     self.Base = declarative_base()
        
        
