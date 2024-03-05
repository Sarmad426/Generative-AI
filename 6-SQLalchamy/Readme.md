# Introduction to SQLAlchemy ORM

SQLAlchemy is a versatile Python library that simplifies database interactions by acting as an Object Relational Mapper (ORM). It bridges the gap between object-oriented code and relational database structures, allowing you to work with data using Python objects instead of raw SQL statements. This approach enhances code readability, maintainability, and reduces the risk of errors.

**Prerequisites:**

* Python 3.6 or later (recommended)
* A code editor or IDE (e.g., PyCharm, Visual Studio Code)
* An SQLite database (you can create one using a tool like SQLite Browser or command-line `sqlite3`)

**Installation**

Install SQLAlchemy using pip:

```bash
pip install sqlalchemy
```

**Creating a Basic Project Structure**

Organize your project by creating directories for your application and database:

```
your_project/
  app.py
  database/
    db.py
```

**Connecting to the Database**

1. **Import necessary modules:**

   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker
   ```

2. **Define the connection string:**

   ```python
   DATABASE_URL = 'sqlite:///your_project/database/your_database.db'
   engine = create_engine(DATABASE_URL)
   ```

   Replace `your_database.db` with your desired database name.

3. **Create a Session object (optional but recommended):**

   ```python
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   ```

   The `SessionLocal` object is used to interact with the database throughout your application.

**Creating Models (Defining Data Structures)**

1. **Import the `declarative_base` class:**

   ```python
   from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import relationship

   Base = declarative_base()
   ```

2. **Define a model class:**

   ```python
   class User(Base):
       __tablename__ = 'users'

       id = Column(Integer, primary_key=True)
       username = Column(String(50), unique=True, nullable=False)
       email = Column(String(120), unique=True, nullable=False)
       password = Column(String(80), nullable=False)

       # Example of a relationship (explained later)
       posts = relationship('Post', backref='author')
   ```

   * The `__tablename__` attribute defines the table name in the database.
   * Each column is represented by a `Column` object, specifying data type, constraints, and other options.
   * The `primary_key` attribute defines the primary key column (if applicable).

**Creating Tables (Schema Migration)**

1. **Import the `metadata` object:**

   ```python
   from sqlalchemy import MetaData
   ```

2. **Create a `metadata` instance:**

   ```python
   metadata = MetaData()
   ```

3. **Associate the model with the metadata:**

   ```python
   Base.metadata = metadata
   ```

4. **Create all tables (optional):**

   ```python
   # Use the engine to create all tables based on the models
   metadata.create_all(engine)
   ```

   This code snippet is optional if you want to create all tables defined by your models at once.

**Establishing a Database Connection (Using Sessions)**

1. **Create a database session:**

   ```python
   def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close()
   ```

   - This function creates a session and yields it for use, ensuring proper session management and closing.

2. **Import and use the `get_db` function in your application:**

   ```python
   from app import get_db

   with get_db() as db:
       # Database operations using the db object (explained later)
   ```

**CRUD Operations**

**1. Create (Insert)**

- Create a new object instance:

```python
user = User(username='alice', email='alice@example.com', password='password123')
```

- Add the object to the session and commit:

```python
with get_db() as db:
    db.add(user)
```
