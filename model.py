# import requiured SQLAlchemy Columns
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

# import base class
from database import Base

# create Task table
class Task(Base):
    # table name
    __tablename__ = "tasks"
    # primary key column, auto-incremented

    id = Column(Integer, primary_key=True, index=True)

    # task title
    task_title = Column(String,nullable=False)

    # task description
    description = Column(String)

    # employee assigned
    assigned_to = Column(String)

    # priority level
    priority = Column(String)

    # task status
    status = Column(String)

    # due date
    due_date = Column(String)

    # created by
    created_by = Column(String)

# this file just defines the structure of the database table, it does not create the table in the database. The table will be created when we run the main.py file   