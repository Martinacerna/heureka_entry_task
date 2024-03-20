from pydantic import BaseModel, Field


class Astronaut(BaseModel):
    id: int = Field(
        description="Number of the the row in the Astronauts table.", example=1
    )
    first_name: str = Field(description="First name of the astronaut.", example="Aegir")
    last_name: str = Field(description="Last name of the astronaut.", example="Yuki")
    age: int = Field(description="Age of the astronaut.", example=3)
    nationality: str = Field(description="Nationality of the astronaut.", example="CZ")
    health_status: bool = Field(
        description="Informs about the health status of the person .", example="true"
    )


class AstronautCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    nationality: str
    health_status: bool
