from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from sqlmodel import SQLModel

import app.models  # noqa: F401 - registers models with SQLModel metadata
from app.api.routers import bills
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # 1. Startup: Connect to resources
    SQLModel.metadata.create_all(engine)

    yield

     # 2. Shutdown: Clean up resources
    print("Application is shutting down...")
    print("Disconnecting from database...")


app = FastAPI(lifespan=lifespan)

app.include_router(bills.router, prefix="/api/v1")
