# import fastapi
from platform import machine

from fastapi import FastAPI, Depends
# import the database session dependency function
# as per day 2
from sqlalchemy.orm import Session
# SessionLocal = machine that creates a database connection.
# Session = the actual database connection.


from database import get_db,Base,engine

# import the Task model
from model import Task

# schemas import
from schemas import TaskSchema


# connect to neon and checks whether the "task" table exists in the database, if not it will create the table
Base.metadata.create_all(bind=engine)

# here ,base contains all the database tables defination
# and engine contains the cloud database connection

# create a FastAPI object
app = FastAPI()

# home API
@app.get("/")
def home():

    return {"message": "Welcome to the Task Management API"}

# this api tell that  :fastapi is running and application is started succesfully

# now run the project using the command : uvicorn main:app --reload or python -m uvicorn main:app --reload

# as per day 2
# post method
@app.post("/create_task")
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    # create a new task object
    new_task = Task(
        task_title=task.task_title,
        description=task.description,
        assigned_to=task.assigned_to,
        priority=task.priority,
        status=task.status,
        due_date=task.due_date,
        created_by=task.created_by
    )
    # add the new task to the database
    db.add(new_task)
    # commit the changes to the database
    db.commit()
    # refresh the new task object to get the id
    db.refresh(new_task)
    # return the new task object
    return {"message": "Task created successfully"}

# the data sent from postman is first valdiated by the task schema and then it is sent to the database. 
# if it valid the values are then copied into the task model which represents the database table and then it is added (finally)to the database.

# get method
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    print("Total tasks:", len(tasks))
    for task in tasks:
        print(task.id, task.task_title)

    return {"tasks": tasks}

# ------------------------------------------------------------------------day 2 ------------------------------------------------------------------------------------------------------------------------
