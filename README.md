# report-service
 This service performs statistical reporting for the project.


## Connect Database

- pip install sqlalchemy
- pip install databases[sqlalchemy]
- example doc: https://fastapi.tiangolo.com/tutorial/sql-databases/
- ORMs

### File Structure
    └── src
        ├── __init__.py
        ├── crud.py
        ├── database.py
        ├── main.py
        ├── models.py
        └── schemas.py


### Step by step Connect DB

- Create a database URL for SQLAlchemy
- Create the SQLAlchemy engine
- Create a SessionLocal class
  - Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
  - But once we create an instance of the SessionLocal class, this instance will be the actual database session.
- Create a Base class.
  - Now we will use the function declarative_base() that returns a class.
  - Later we will inherit from this class to create each of the database models or classes (the ORM models):
- Create the database models
  - Now let's see the file  `sql_app/models.py`.
  - Create SQLAlchemy models from the `Base` class
  - Create model attributes/columns
  - Create the relationships
- Create the Pydantic models:
  - Now let's check the file  `sql_app/schemas.py`.
- CRUD utils
    - Now let's see the file `sql_app/crud.py`.
    - Read Data.
    - Create Data
- Main FastAPI app
- About `def` vs `async def`
- Migrations
- Review all the files

- run `uvicorn src.main:app` or `uvicorn src.main:app --reload`




