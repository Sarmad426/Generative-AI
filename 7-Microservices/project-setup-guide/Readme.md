# Setting up a FastAPI Project with Poetry

## Step 1: Install pipx

- Open your terminal.
- Install pipx using pip: `python -m pip install --user pipx`

## Step 2: Ensure pipx's binary directory is in your PATH

Run the following command to ensure pipx's binary directory is in your PATH:

```bash
python -m pipx ensurepath
```

## Step 3: Restart your terminal

Restart your terminal to apply the PATH update.

## Step 4: Install Poetry

Run the command:

```bash
pipx install poetry
```

## Step 5: Check the version of Poetry

To check the version, run:

```bash
poetry --version
```

## Step 6: Create a new project

Create a new project with Poetry:

```bash
poetry new uit-api-class --name uitclass
```

## Step 7: Navigate to the project folder

Open the subfolder inside the parent folder, in this case `uitclass`.

## Step 8: Create a main.py file

Create a new file named `main.py`.

## Step 9 (Optional): Check the Python version

To check the version of Python, run:

```bash
poetry run python --version
```

## Step 10: Add FastAPI and Uvicorn

Run the command:

```bash
poetry add fastapi "uvicorn[standard]"
```

## Step 10a (Optional): Check packages in pyproject.toml

Optionally, check the packages inside the `pyproject.toml` file.

## Step 11: Write the hello world code in main.py

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

## Step 12: Run the server

Run the server using Poetry:

```bash
poetry run uvicorn uitclass.main:app --host 0.0.0.0 --port 8000
```

## Step 13: Open the URLs

Open the following URLs in your browser:

- [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
- [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)
- [http://0.0.0.0:8000/openapi.json](http://0.0.0.0:8000/openapi.json)
or

- [http://localhost:8000](http://localhost:8000)
