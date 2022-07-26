from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0iFQzvkIb4wlxtcBu77x@database-back.ci9hvdjnsjob.sa-east-1.rds.amazonaws.com/db"
SQLALCHEMY_DATABASE_URL = "postgres://opc_user:3bDRVQvyXYV0h5fZxJAAUoCBJmSqLk4u@dpg-cbfldi1g7hp4t87dvmg0-a/opc"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()