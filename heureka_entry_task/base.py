from pydantic_settings import BaseSettings
import logging


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    rabbitmq_connection: str = "amqp://guest:guest@127.0.0.1/"
    queue_name: str = "Heureka_astronaut"
    prefetch_count: int = 100
    routing_key: str = "Heureka_astronaut"


# Logger settings
# create logger and set level to INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
handler = logging.FileHandler("app.log")
handler.setLevel(logging.INFO)

# Create a logging format and add handler to the logger
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


settings = Settings()
