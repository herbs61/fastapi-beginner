from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url="sqlite://todo.db",
    modules={"models": ["api.models.todo"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def index():
    return {"status": "todo api is running"}