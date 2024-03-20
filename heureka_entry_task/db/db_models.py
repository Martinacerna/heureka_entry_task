from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import declarative_base

Base = declarative_base()  # model base class


class Astronaut(Base):
    __tablename__ = "astronaut"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int]
    nationality: Mapped[str]
    health_status: Mapped[bool]
