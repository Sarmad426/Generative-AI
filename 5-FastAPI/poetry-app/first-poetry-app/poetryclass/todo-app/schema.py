"""
Fast API todo app schema
"""

from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session


class Todo(SQLModel, table=True):
    """
    Todo schema
    """

    id: int = Field(default=None, primary_key=True)
    title: str
    completed: bool = Field(default=False)
