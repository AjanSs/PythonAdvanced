from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from database import Base, engine
from models import Category, Recipe
from routers import categories, recipes


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Online Recipe Book API",
    description="An API to organise, search and manage recipes and categories.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(categories.router)
app.include_router(recipes.router)


@app.get("/", tags=["General"])
def home():
    return {"message": "Welcome to the Online Recipe Book API", "docs": "/docs"}


@app.get("/health", tags=["General"])
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"status": "healthy", "database": "connected"}
