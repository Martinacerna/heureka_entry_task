import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from heureka_entry_task.base import settings
from heureka_entry_task.db.db_models import Base

engine = create_async_engine(settings.database_url, echo=settings.echo_sql)
async_session = async_sessionmaker(engine, expire_on_commit=False)
