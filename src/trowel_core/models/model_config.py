from pydantic import BaseModel, Field

class Config(BaseModel):
    name: str
    sources: list[str] = Field(min_length=1)