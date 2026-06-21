from pathlib import Path

from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja


from app.db.session import get_db as get_db  # noqa: F401

templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

jinjax = Jinja(templates)

