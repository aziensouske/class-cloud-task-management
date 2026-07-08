# import basemodel

from pydantic import BaseModel

# task creation schema
class TaskSchema(BaseModel):

    # task title
    task_title: str

    # task description
    description: str

    # employee assigned
    assigned_to: str

    # priority level
    priority: str

    # task status
    status: str

    # due date
    due_date: str

    # created by
    created_by: str


# this schema  validates the data before it enters the cloud databse
 