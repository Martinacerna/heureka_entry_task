import asyncio

import pytest
import pytest_asyncio
from sqlalchemy import text

from heureka_entry_task.db.db_models import Base
from heureka_entry_task.db.session import engine
from heureka_entry_task.models import Astronaut


@pytest_asyncio.fixture(scope="function", autouse=True)
async def create_tables():
    """
    Create tables in the database at the beginning of the tests
    :return:
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest.fixture(scope="session", autouse=True)
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
def astronaut_fixture():
    return Astronaut(
        id=1,
        first_name="Ramiro",
        last_name="Swanson",
        age=30,
        nationality="USA",
        health_status=True,
    )
