import asyncio

import aio_pika

from heureka_entry_task.base import logger, settings
from heureka_entry_task.controller import Controller
from heureka_entry_task.db.session import async_session
from heureka_entry_task.models import AstronautCreate


async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    """
    Function to process the message from the queue and validate incoming data against Pydantic model AstronautCreate.
    """
    async with message.process():
        astronaut_message = AstronautCreate.model_validate_json(message.body)
        await Controller(async_session).create(astronaut_message)


async def main() -> None:
    """
    Main function to connect to the RabbitMQ server and consume the messages from the queue.
    """
    connection = await aio_pika.connect_robust(
        settings.consumer_connection,
    )
    logger.info("Consumer connected to RabbitMQ.")

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=settings.prefetch_count)

    # Declaring queue
    queue = await channel.declare_queue(settings.queue_name)

    await queue.consume(process_message)
    logger.info("Message consumed from queue.")

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()
        logger.info("Connection closed.")


if __name__ == "__main__":
    asyncio.run(main())
