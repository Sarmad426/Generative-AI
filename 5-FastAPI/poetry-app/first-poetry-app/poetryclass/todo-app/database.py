"""
Fast API todo app database connection
"""

from sqlmodel import Session, create_engine

DB_FILE_NAME = "todo.db"
DB_URL = f"sqlite:///{DB_FILE_NAME}"


connect_args = {"check_same_thread": False}

engine = create_engine(DB_URL, echo=True, connect_args=connect_args)


def get_session():
    """
    Returns database session
    """
    with Session(engine) as session:
        yield session
