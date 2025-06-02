
# 📘 FastAPI Todo API – Official Documentation

## 🗂️ Table of Contents
1. [Overview](#overview)
2. [Folder Structure](#folder-structure)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)
5. [API Endpoints](#api-endpoints)
6. [Database Configuration](#database-configuration)
7. [Models](#models)
8. [Schemas](#schemas)
9. [License](#license)

---

## 📌 Overview
This is a basic **FastAPI-based Todo API** project using **Tortoise ORM** and SQLite as the database. It provides functionality to create, read, update, and delete todo items.

---

## 📁 Folder Structure
```
fastapi/
├── api/
│   ├── models/              # Database Models (Tortoise ORM)
│   ├── routes/              # API Route Handlers
│   └── schemas/             # Pydantic Schemas
├── app/
│   └── main.py              # FastAPI app initialization
├── db.sqlite3               # SQLite database file
├── todo.db                  # Alternative or legacy database
├── requirements.txt         # Python dependencies
├── venv/                    # Python virtual environment
```

---

## ⚙️ Installation

1. **Clone or unzip the project:**

```bash
unzip fastapi.zip
cd fastapi
```

2. **(Optional) Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

1. **Start the FastAPI server:**

```bash
uvicorn app.main:app --reload
```

2. **Access the API Docs:**

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔧 API Endpoints

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/api/`          | Get all todos          |
| POST   | `/api/`          | Create new todo        |
| PUT    | `/api/{key}`     | Update a todo by ID    |
| DELETE | `/api/{key}`     | Delete a todo by ID    |

All endpoints expect/return JSON. The POST and PUT routes use `PostTodo` and `PutTodo` Pydantic schemas.

---

## 🗃️ Database Configuration

This app uses **SQLite** and **Tortoise ORM**.

Tortoise model is defined in:
```
api/models/todo.py
```

Database file:
- `db.sqlite3` or `todo.db`

---

## 📦 Models

### `Todo` (Tortoise ORM model)

```python
class Todo(Model):
    id = fields.IntField(pk=True)
    task = fields.CharField(max_length=100)
    done = fields.BooleanField(default=False, null=False)
```

---

## 📤 Schemas

Located in `api/schemas/todo.py`:

- `PostTodo`: For creating new todos
- `PutTodo`: For updating existing todos
- `GetTodo`: For output formatting

---

## 📄 License

This project is provided for educational/demo purposes. Use and modify freely.
