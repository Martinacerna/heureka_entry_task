import pytest


from heureka_entry_task.controller import Controller
from heureka_entry_task.db.session import async_session
from heureka_entry_task.models import AstronautCreate


@pytest.mark.asyncio
async def test_create(astronaut_fixture):
    create_astrounaut = AstronautCreate(
        first_name=astronaut_fixture.first_name,
        last_name=astronaut_fixture.last_name,
        age=astronaut_fixture.age,
        nationality=astronaut_fixture.nationality,
        health_status=astronaut_fixture.health_status,
    )
    test_astronaut = await Controller(async_session).create(astronaut=create_astrounaut)
    assert test_astronaut.first_name == astronaut_fixture.first_name
    assert test_astronaut.health_status == astronaut_fixture.health_status


@pytest.mark.asyncio
async def test_update_astronaut(astronaut_fixture):
    controller = Controller(async_session)
    create_astrounaut = AstronautCreate(
        first_name=astronaut_fixture.first_name,
        last_name=astronaut_fixture.last_name,
        age=astronaut_fixture.age,
        nationality=astronaut_fixture.nationality,
        health_status=astronaut_fixture.health_status,
    )
    test_astronaut = await controller.create(astronaut=create_astrounaut)

    await controller.update_astronaut(
        id=test_astronaut.id,
        health_status=True,
        first_name="Aegir",
        last_name="Yuki",
        age=3,
        nationality="CZ",
    )

    get_astronaut = await controller.read_single_astronaut(id=test_astronaut.id)

    assert get_astronaut.first_name == "Aegir"
    assert get_astronaut.last_name == "Yuki"
    assert get_astronaut.age == 3


# next to do:
# - test delete
# - test read_single_astronaut
# - test read_all_astronauts

# in different file: test RabbitMQ - message published to queue, message consumed from queue
