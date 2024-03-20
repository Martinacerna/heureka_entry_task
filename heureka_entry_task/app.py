from contextlib import asynccontextmanager

from fastapi import FastAPI

from heureka_entry_task.base import logger
from heureka_entry_task.controller import Controller
from heureka_entry_task.db.db_models import Base
from heureka_entry_task.db.session import async_session, engine
from heureka_entry_task.models import AstronautCreate, Astronaut


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function to create the database tables when the app starts and delete them when the app stops.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
def ping() -> str:
    logger.info("Received ping, returning pong")
    return "pong"


@app.post("/create_astronaut")
async def create_astronaut(astronaut: AstronautCreate) -> AstronautCreate:
    await Controller(async_session).create(astronaut)
    logger.info("Astronaut created successfully")
    return astronaut


@app.delete("/delete_astronaut/{id}")
async def delete_astronaut(id: int) -> None:
    await Controller(async_session).delete(id)
    logger.info(f"Astronaut with id {id} deleted successfully.")


@app.get("/read_astronaut/{id}")
async def get_astronaut(id: int) -> Astronaut:
    return await Controller(async_session).read_single_astronaut(id)


@app.get("/read_all_astronauts")
async def get_all_astronauts(offset: int = 0, limit_num: int = 10) -> list[Astronaut]:
    return await Controller(async_session).read_all_astronauts(limit_num, offset)


@app.put("/update_astronaut/{id}")
async def update_astronaut(
    id: int,
    health_status: bool | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    age: int | None = None,
    nationality: str | None = None,
) -> None:
    await Controller(async_session).update_astronaut(
        id, health_status, first_name, last_name, age, nationality
    )
    logger.info(
        f"Astronaut's with {id} details were updated: health status: {health_status}, first name: {first_name}, last name: {last_name}, age: {age}, nationality: {nationality}."
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
