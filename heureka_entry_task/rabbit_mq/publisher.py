import asyncio

import aio_pika

from heureka_entry_task.base import logger, settings
from heureka_entry_task.models import AstronautCreate


async def main() -> None:
    """
    Main function to connect to the RabbitMQ server and publish the messages to the queue.
    """
    connection = await aio_pika.connect_robust(
        settings.rabbitmq_connection,
    )
    logger.info("Publisher connected to RabbitMQ")

    async with connection:

        model = AstronautCreate(
            first_name="Ruy",
            last_name="Lopez",
            age=30,
            nationality="USA",
            health_status=True,
        ).model_dump_json()
        channel = await connection.channel()

        # Declaring queue
        await channel.declare_queue(settings.routing_key)
        body = model.encode()
        await channel.default_exchange.publish(
            aio_pika.Message(body=body),
            routing_key=settings.routing_key,
        )
        logger.info(f"Message published to queue {settings.routing_key}.")


if __name__ == "__main__":
    asyncio.run(main())
