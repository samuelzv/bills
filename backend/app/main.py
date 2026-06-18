from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from pathlib import Path

from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, Session, select

# import app.models  # noqa: F401 - registers models with SQLModel metadata
from app.api.routers import bills
# from app.api.routers import bills
from app.db.session import engine, get_db
from app.models.bill import Bill

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # 1. Startup: Connect to resources
    SQLModel.metadata.create_all(engine)

    yield

     # 2. Shutdown: Clean up resources
    print("Application is shutting down...")
    print("Disconnecting from database...")


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
app.include_router(bills.router, prefix="/api/v1")


@app.get("/")
async def index(request: Request, db: Session = Depends(get_db)):
    bills = [b.model_dump(mode="json") for b in db.exec(select(Bill)).all()]
    return templates.TemplateResponse(request, "bills.jinja-html", {"bills": bills})
