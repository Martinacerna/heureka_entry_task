from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from heureka_entry_task.db.db_models import Astronaut as DB_astronaut
from heureka_entry_task.models import Astronaut, AstronautCreate


class Controller:
    def __init__(self, async_session: async_sessionmaker[AsyncSession]) -> None:
        self.async_session = async_session

    async def create(
        self,
        astronaut: AstronautCreate,
    ) -> Astronaut:
        """
        Function to create an astronaut in the database.
        :return: type Astronaut, newly created astronaut
        """
        async with self.async_session() as session:
            db_astronaut = DB_astronaut(
                first_name=astronaut.first_name,
                last_name=astronaut.last_name,
                age=astronaut.age,
                nationality=astronaut.nationality,
                health_status=astronaut.health_status,
            )

            session.add(db_astronaut)
            await session.commit()
            return Astronaut(
                id=db_astronaut.id,
                first_name=db_astronaut.first_name,
                last_name=db_astronaut.last_name,
                age=db_astronaut.age,
                nationality=db_astronaut.nationality,
                health_status=db_astronaut.health_status,
            )

    async def delete(self, id: int) -> None:
        """
        Function to delete an astronaut with specific id from the database.
        """
        async with self.async_session() as session:
            id_to_delete = await session.get(DB_astronaut, id)
            if id_to_delete is None:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND, detail="Astronaut ID not found"
                )
            await session.delete(id_to_delete)
            await session.commit()

    async def read_single_astronaut(self, id: int) -> Astronaut:
        """
        Function to get data about an astronaut with specific id from the database.
        :return: type Astronaut
        """
        async with self.async_session() as session:
            db_astronaut = await session.get(DB_astronaut, id)
            return Astronaut(
                id=db_astronaut.id,
                first_name=db_astronaut.first_name,
                last_name=db_astronaut.last_name,
                age=db_astronaut.age,
                nationality=db_astronaut.nationality,
                health_status=db_astronaut.health_status,
            )

    async def read_all_astronauts(
        self,
        limit_num: int,
        offset: int = 0,
    ) -> list[Astronaut]:
        """
        Function to get data about all astronauts from the database.
        :param limit_num: int, maximal number of astronauts to return. If there is less astronauts in the database, all of them will be returned.
        :param offset: int, number of astronauts to skip
        """
        async with self.async_session() as session:
            stmt = select(DB_astronaut).limit(limit_num).offset(offset)
            db_rows = (await session.execute(stmt)).scalars()
            astronaut = [
                Astronaut(
                    id=db_row.id,
                    first_name=db_row.first_name,
                    last_name=db_row.last_name,
                    age=db_row.age,
                    nationality=db_row.nationality,
                    health_status=db_row.health_status,
                )
                for db_row in db_rows
            ]
            return astronaut

    async def update_astronaut(
        self,
        id: int,
        health_status: bool | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        age: int | None = None,
        nationality: str | None = None,
    ) -> None:
        """
        Function to update astronaut information in the database.
        """
        async with self.async_session() as session:
            select_astronaut = await session.get(DB_astronaut, id)
            select_astronaut.health_status = (
                health_status
                if health_status is not None
                else select_astronaut.health_status
            )
            select_astronaut.first_name = (
                first_name if first_name else select_astronaut.first_name
            )
            select_astronaut.last_name = (
                last_name if last_name else select_astronaut.last_name
            )
            select_astronaut.age = age if age else select_astronaut.age
            select_astronaut.nationality = (
                nationality if nationality else select_astronaut.nationality
            )
            await session.commit()
