import logging

from sqlalchemy import text
from sqlmodel import Session
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.session import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@retry(
    stop=stop_after_attempt(60 * 5),
    wait=wait_fixed(1),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def wait_for_db() -> None:
    with Session(engine) as session:
        session.execute(text("SELECT 1"))


def main() -> None:
    logger.info("Waiting for database...")
    wait_for_db()
    logger.info("Database is ready")


if __name__ == "__main__":
    main()
