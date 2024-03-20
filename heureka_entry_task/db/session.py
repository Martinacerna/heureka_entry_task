import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from heureka_entry_task.base import settings
from heureka_entry_task.db.db_models import Base

engine = create_async_engine(settings.database_url, echo=settings.echo_sql)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def async_main() -> None:
    """
    Function to create the database tables.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(async_main())
